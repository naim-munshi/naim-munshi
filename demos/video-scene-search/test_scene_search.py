import unittest
from scene_search import windows, transcript_for, cosine, rank

class RetrievalTests(unittest.TestCase):
    def test_final_partial_window(self):
        self.assertEqual(windows(11,5), [(0,5),(5,10),(10,11)])
    def test_invalid_duration(self):
        for n in (0, -1, float('nan'), 601):
            with self.assertRaises(ValueError): windows(n,5)
    def test_boundary_overlap(self):
        s=[{'start':0,'end':5,'text':'one'},{'start':5,'end':7,'text':'two'}]
        self.assertEqual(transcript_for(s,5,10),'two')
    def test_weight_changes_ranking(self):
        rows=[dict(start=0,end=5,text='a',image_embedding=[1,0],text_embedding=[0,1]),
              dict(start=5,end=10,text='b',image_embedding=[0,1],text_embedding=[1,0])]
        self.assertEqual(rank(rows,[1,0],1)[0]['start'],0)
        self.assertEqual(rank(rows,[1,0],0)[0]['start'],5)
    def test_silent_fallback(self):
        r=dict(start=0,end=5,text='',image_embedding=[1,0],text_embedding=None)
        self.assertEqual(rank([r],[1,0],0)[0]['score'],1)
    def test_invalid_embeddings(self):
        for a,b in [([0,0],[1,0]),([1],[1,0]),([float('nan')],[1])]:
            with self.assertRaises(ValueError): cosine(a,b)
    def test_invalid_parameters(self):
        for a,k in [(float('nan'),1),(-1,1),(2,1),(.5,0)]:
            with self.assertRaises(ValueError): rank([], [1],a,k)

if __name__ == '__main__': unittest.main()
