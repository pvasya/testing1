import unittest
from geometry_calc import intersect_two_lines, EPS

class TestIntersection(unittest.TestCase):
    def test_intersect_at_point(self):
        res, pt = intersect_two_lines(1, 1, -2, 1, -1, 0)
        self.assertEqual(res, 'point')
        self.assertAlmostEqual(pt[0], 1.0)
        self.assertAlmostEqual(pt[1], 1.0)

    def test_parallel_lines(self):
        res, pt = intersect_two_lines(1, 1, -2, 1, 1, -4)
        self.assertEqual(res, 'parallel')
        self.assertIsNone(pt)

    def test_coincident_lines(self):
        res, pt = intersect_two_lines(1, 1, -2, 2, 2, -4)
        self.assertEqual(res, 'coincident')
        self.assertIsNone(pt)

    def test_vertical_and_horizontal(self):
        res, pt = intersect_two_lines(1, 0, -5, 0, 1, -3)
        self.assertEqual(res, 'point')
        self.assertEqual(pt, (5.0, 3.0))

if __name__ == "__main__":
    unittest.main()
