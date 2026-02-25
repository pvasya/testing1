import unittest
from geometry_calc import validate_params

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.N = 48
        self.valid_params = {
            'a': 1, 'b': 1, 'x01': 0, 'y01': 0, 'a1': 1, 'b1': 1,
            'x02': 0, 'y02': 0, 'a2': 1, 'b2': 1
        }

    def test_valid_params(self):
        validate_params(self.valid_params, self.N)

    def test_non_integer_raises_error(self):
        params = self.valid_params.copy()
        params['a'] = 1.5
        with self.assertRaises(ValueError) as cm:
            validate_params(params, self.N)
        self.assertIn('Non-integer value', str(cm.exception))

    def test_string_raises_error(self):
        params = self.valid_params.copy()
        params['b'] = "2"
        with self.assertRaises(ValueError):
            validate_params(params, self.N)

    def test_exceed_max_raises_error(self):
        params = self.valid_params.copy()
        params['x01'] = 200
        with self.assertRaises(ValueError) as cm:
            validate_params(params, self.N)
        self.assertIn('outside of range', str(cm.exception))

    def test_below_min_raises_error(self):
        params = self.valid_params.copy()
        params['y01'] = -200
        with self.assertRaises(ValueError) as cm:
            validate_params(params, self.N)
        self.assertIn('outside of range', str(cm.exception))

if __name__ == "__main__":
    unittest.main()
