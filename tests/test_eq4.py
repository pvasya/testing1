import unittest
from geometry_calc import eq4_to_ABC

class TestEq4(unittest.TestCase):
    def test_basic_conversion(self):
        A, B, C = eq4_to_ABC(2, 3)
        self.assertEqual((A, B, C), (3.0, 2.0, -6.0))

    def test_negative_values(self):
        A, B, C = eq4_to_ABC(-2, 2)
        self.assertEqual((A, B, C), (2.0, -2.0, 4.0))

    def test_large_values(self):
        A, B, C = eq4_to_ABC(148, 148)
        self.assertEqual((A, B, C), (148.0, 148.0, -148.0 * 148.0))

    def test_zero_a_raises_error(self):
        with self.assertRaises(ValueError):
            eq4_to_ABC(0, 3)

    def test_zero_b_raises_error(self):
        with self.assertRaises(ValueError):
            eq4_to_ABC(3, 0)

if __name__ == "__main__":
    unittest.main()
