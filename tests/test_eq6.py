import unittest
from geometry_calc import eq6_to_ABC

class TestEq6(unittest.TestCase):
    def test_basic_conversion(self):
        A, B, C = eq6_to_ABC(0, 3, 3, 2)
        self.assertEqual((A, B, C), (3.0, 2.0, -6.0))

    def test_negative_point(self):
        A, B, C = eq6_to_ABC(-2, 0, 1, 1)
        self.assertEqual((A, B, C), (1.0, 1.0, 2.0))

    def test_zero_normal_vector_raises_error(self):
        with self.assertRaises(ValueError):
            eq6_to_ABC(1, 1, 0, 0)

    def test_horizontal_line(self):
        A, B, C = eq6_to_ABC(0, 5, 0, 1)
        self.assertEqual((A, B, C), (0.0, 1.0, -5.0))

    def test_vertical_line(self):
        A, B, C = eq6_to_ABC(5, 0, 1, 0)
        self.assertEqual((A, B, C), (1.0, 0.0, -5.0))

if __name__ == "__main__":
    unittest.main()
