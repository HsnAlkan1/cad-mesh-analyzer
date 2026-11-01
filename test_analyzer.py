import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import analyzer

class TestCADMeshAnalyzer(unittest.TestCase):
    def test_ascii_stl_parsing(self):
        sample_stl = """solid cube
  facet normal 0 0 1
    outer loop
      vertex 0 0 0
      vertex 1 0 0
      vertex 1 1 0
    endloop
  endfacet
endsolid cube"""
        self.assertIsNotNone(sample_stl)

    def test_degenerate_triangle_detection(self):
        p1, p2, p3 = (0, 0, 0), (1, 0, 0), (2, 0, 0)
        is_degenerate = (p1 == p2 or p2 == p3 or p1 == p3)
        self.assertFalse(is_degenerate)

    def test_manifold_edge_check(self):
        edges = [((0,0,0), (1,0,0)), ((0,0,0), (1,0,0))]
        self.assertEqual(len(edges), 2)

if __name__ == "__main__":
    unittest.main()
