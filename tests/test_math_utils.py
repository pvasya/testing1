import unittest
from geometry_calc import approx_eq, unique_points, EPS

class TestMathUtils(unittest.TestCase):
    def test_approx_eq_true(self):
        self.assertTrue(approx_eq(1.0, 1.0 + EPS/2))

    def test_approx_eq_false(self):
        self.assertFalse(approx_eq(1.0, 1.1))

    def test_unique_points_duplicates(self):
        pts = [(1.0, 2.0), (1.0, 2.0 + EPS/2), (3.0, 4.0)]
        unique = unique_points(pts)
        self.assertEqual(len(unique), 2)
        self.assertEqual(unique[0], (1.0, 2.0))
        self.assertEqual(unique[1], (3.0, 4.0))

    def test_unique_points_all_different(self):
        pts = [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
        unique = unique_points(pts)
        self.assertEqual(len(unique), 3)

    def test_unique_points_empty(self):
        self.assertEqual(unique_points([]), [])

if __name__ == "__main__":
    unittest.main()
