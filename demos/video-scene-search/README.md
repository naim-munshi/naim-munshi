# Whisper and CLIP Video Search

Small local CLI prototype for retrieving time windows from a video using sampled images and spoken content. Written as an AI-assisted portfolio experiment. This is source code with tested retrieval logic, **not yet a validated real-model demo**.

## Pipeline

1. Split a local video (maximum ten minutes) into fixed five-second windows.
2. Use Whisper `base` to translate speech to English with timestamps.
3. Encode each window's middle frame and overlapping transcript using CLIP ViT-B/32.
4. Encode an English query and rank windows by weighted image/text cosine similarity.
5. Print start/end timestamps, transcript and both component scores as JSON.

This is fixed-window retrieval, not learned scene-boundary detection. Scores are not probabilities. One frame can miss brief actions; transcripts crossing boundaries appear in both windows. CLIP truncates text beyond its token limit. Whisper can hallucinate on silence. English translation loses nuance; no Japanese query quality is claimed. Silent windows fall back to image-only scoring regardless of alpha.

## Run on Mac or Linux

Install Python 3.11 and FFmpeg first (`brew install ffmpeg` on Mac). From this directory:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdir -p private
python scene_search.py index /absolute/path/to/your-video.mp4 private/index.json --language ja
python scene_search.py search private/index.json "a person writing with their hand" --top-k 5
```

First use downloads model weights and needs internet access. Processing uses CPU and may be slow. Use only trusted local videos; no URL downloader or hosted server is provided. For a video with no audio track, use `index ... --silent`. Existing index files are not overwritten. Store indexes in `private/`: they contain transcripts, which may be sensitive. Do not commit videos, indexes, personal recordings or credentials.

## What was tested

```bash
python -m unittest -v
```

Seven dependency-free unit tests exercise window boundaries, timestamp overlap, visual/speech ranking, silent fallback and malformed parameters/vectors. These synthetic vectors are **not CLIP model outputs**. They do not establish model accuracy, media decoding compatibility or package compatibility. Real Whisper/CLIP inference has not been executed in the authoring environment because dependencies and weights are unavailable. Requirements are not a verified lockfile.

## Required acceptance before adding this as demonstrated CV experience

Record an original 30-60 second video with several distinct scenes and spoken descriptions. Run indexing and five English queries, including a visual-only and a speech-only query. Manually label relevant windows before scoring; record Recall@3, hardware, package versions, indexing time and query latency. Inspect timestamps against the video, log failures, and capture a short actual terminal/video walkthrough. Never invent these measurements. Keep raw private media out of Git; share only recordings you have permission to publish.

## Primary references

- https://github.com/openai/whisper
- https://github.com/openai/CLIP
