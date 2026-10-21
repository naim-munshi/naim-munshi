"""Local fixed-window video retrieval prototype, not temporal scene detection."""
import argparse
import json
import math
from pathlib import Path


def windows(duration, seconds):
    if not all(math.isfinite(x) and x > 0 for x in (duration, seconds)):
        raise ValueError('duration and window must be finite and positive')
    if duration > 600 or seconds < 1:
        raise ValueError('demo supports <=600 seconds and windows >=1 second')
    return [(i * seconds, min((i + 1) * seconds, duration))
            for i in range(math.ceil(duration / seconds))]


def transcript_for(segments, start, end):
    return ' '.join(s['text'].strip() for s in segments
                    if s['start'] < end and s['end'] > start).strip()


def cosine(a, b):
    if len(a) != len(b) or not a:
        raise ValueError('embedding dimensions must match')
    if not all(math.isfinite(v) for v in (*a, *b)):
        raise ValueError('nonfinite embedding')
    denom = math.sqrt(sum(x*x for x in a) * sum(x*x for x in b))
    if not denom:
        raise ValueError('zero embedding')
    return sum(x*y for x, y in zip(a, b)) / denom


def rank(records, query_vector, alpha=0.6, top_k=5):
    if not math.isfinite(alpha) or not 0 <= alpha <= 1 or top_k < 1:
        raise ValueError('alpha must be in [0,1], top-k must be positive')
    results = []
    for r in records:
        visual = cosine(query_vector, r['image_embedding'])
        speech = cosine(query_vector, r['text_embedding']) if r['text_embedding'] else None
        score = visual if speech is None else alpha * visual + (1-alpha) * speech
        results.append({'start': r['start'], 'end': r['end'], 'text': r['text'],
                        'score': score, 'visual_score': visual, 'speech_score': speech})
    return sorted(results, key=lambda r: (-r['score'], r['start']))[:top_k]


def load_clip():
    import clip
    import torch
    model, preprocess = clip.load('ViT-B/32', device='cpu')
    model.eval()
    return clip, torch, model, preprocess


def encode_text(text, engine):
    clip, torch, model, _ = engine
    with torch.no_grad():
        return model.encode_text(clip.tokenize([text], truncate=True)).float()[0].tolist()


def build(video, destination, seconds, language, silent):
    import cv2
    import whisper
    from PIL import Image
    video = Path(video).resolve(strict=True)
    if not video.is_file():
        raise ValueError('input must be a local video file')
    if destination.exists():
        raise ValueError('output already exists; choose a new index path')
    cap = cv2.VideoCapture(str(video))
    try:
        if not cap.isOpened():
            raise ValueError('cannot decode video')
        fps = cap.get(cv2.CAP_PROP_FPS)
        if not math.isfinite(fps) or fps <= 0:
            raise ValueError('invalid video FPS')
        duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
        spans = windows(duration, seconds)
        # Translate into English because standard CLIP is English-oriented.
        segments = [] if silent else whisper.load_model('base', device='cpu').transcribe(
            str(video), task='translate', language=language, fp16=False)['segments']
        engine = load_clip()
        _, torch, model, preprocess = engine
        records = []
        for start, end in spans:
            timestamp = (start + end) / 2
            cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
            ok, frame = cap.read()
            if not ok:
                raise ValueError(f'frame decode failed at {timestamp:.2f}s; index not written')
            picture = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            with torch.no_grad():
                vector = model.encode_image(preprocess(picture).unsqueeze(0)).float()[0].tolist()
            text = transcript_for(segments, start, end)
            records.append({'start': start, 'end': end, 'frame_time': timestamp, 'text': text,
                            'image_embedding': vector,
                            'text_embedding': encode_text(text, engine) if text else None})
        payload = {'schema': 1, 'clip_model': 'ViT-B/32', 'whisper_model': None if silent else 'base',
                   'speech_task': None if silent else 'translate', 'duration': duration,
                   'window_seconds': seconds, 'records': records}
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('x', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, allow_nan=False)
    finally:
        cap.release()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    commands = p.add_subparsers(dest='command', required=True)
    b = commands.add_parser('index')
    b.add_argument('video'); b.add_argument('output', type=Path)
    b.add_argument('--window', type=float, default=5)
    b.add_argument('--language', default=None)
    b.add_argument('--silent', action='store_true', help='explicitly skip audio for silent videos')
    q = commands.add_parser('search')
    q.add_argument('index', type=Path); q.add_argument('query', help='English query')
    q.add_argument('--alpha', type=float, default=.6); q.add_argument('--top-k', type=int, default=5)
    a = p.parse_args()
    if a.command == 'index':
        build(a.video, a.output, a.window, a.language, a.silent)
    else:
        if not a.query.strip():
            p.error('query cannot be empty')
        data = json.loads(a.index.read_text(encoding='utf-8'))
        if data.get('schema') != 1 or data.get('clip_model') != 'ViT-B/32':
            p.error('unsupported index format or model')
        results = rank(data['records'], encode_text(a.query, load_clip()), a.alpha, a.top_k)
        print(json.dumps(results, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
