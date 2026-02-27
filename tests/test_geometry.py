import unittest
from geometry_calc import analyze_three_lines, EPS

class TestGeometry(unittest.TestCase):
    def setUp(self):
        self.N = 48

    # Class A: Coincident (6 tests)
    def test_class_a_1(self):
        params = {'a': -148, 'b': -148, 'x01': -148, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': -148, 'y02': 0, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'coincident')

    def test_class_a_2(self):
        params = {'a': 148, 'b': 148, 'x01': 148, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': 148, 'y02': 0, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'coincident')

    def test_class_a_3(self):
        params = {'a': 5, 'b': 5, 'x01': 2, 'y01': 3, 'a1': 1, 'b1': 1, 'x02': 2, 'y02': 3, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'coincident')

    def test_class_a_4(self):
        params = {'a': 1, 'b': 1, 'x01': -147, 'y01': 148, 'a1': 1, 'b1': 1, 'x02': 147, 'y02': -146, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'coincident')

    def test_class_a_5(self):
        params = {'a': -147, 'b': -147, 'x01': -148, 'y01': 1, 'a1': 1, 'b1': 1, 'x02': -147, 'y02': 0, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'coincident')

    def test_class_a_6(self):
        params = {'a': 147, 'b': 147, 'x01': 147, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': 146, 'y02': 1, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'coincident')

    # Class B: No Intersection (6 tests)
    def test_class_b_1(self):
        params = {'a': -148, 'b': -148, 'x01': -148, 'y01': -147, 'a1': 1, 'b1': 1, 'x02': -148, 'y02': -146, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'no_intersection')

    def test_class_b_2(self):
        params = {'a': 148, 'b': 148, 'x01': 148, 'y01': 147, 'a1': 1, 'b1': 1, 'x02': 148, 'y02': 146, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'no_intersection')

    def test_class_b_3(self):
        params = {'a': 1, 'b': 1, 'x01': 0, 'y01': 2, 'a1': 1, 'b1': 1, 'x02': 0, 'y02': 3, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'no_intersection')

    def test_class_b_4(self):
        params = {'a': -148, 'b': -148, 'x01': 0, 'y01': 2, 'a1': 1, 'b1': 1, 'x02': 0, 'y02': 3, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'no_intersection')

    def test_class_b_5(self):
        params = {'a': -148, 'b': -148, 'x01': -147, 'y01': -147, 'a1': 1, 'b1': 1, 'x02': 0, 'y02': 2, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'no_intersection')

    def test_class_b_6(self):
        params = {'a': 148, 'b': 148, 'x01': 147, 'y01': 147, 'a1': 1, 'b1': 1, 'x02': 0, 'y02': 2, 'a2': 1, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'no_intersection')

    # Class C: One Point (6 tests)
    def test_class_c_1(self):
        params = {'a': -148, 'b': -148, 'x01': -148, 'y01': 0, 'a1': 1, 'b1': 0, 'x02': -148, 'y02': 0, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'one_point')

    def test_class_c_2(self):
        params = {'a': 148, 'b': 148, 'x01': 148, 'y01': 0, 'a1': 1, 'b1': 0, 'x02': 148, 'y02': 0, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'one_point')

    def test_class_c_3(self):
        params = {'a': 2, 'b': 2, 'x01': 1, 'y01': 1, 'a1': 1, 'b1': 0, 'x02': 1, 'y02': 1, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'one_point')

    def test_class_c_4(self):
        params = {'a': -146, 'b': -146, 'x01': -147, 'y01': 1, 'a1': 1, 'b1': 2, 'x02': -147, 'y02': 1, 'a2': 2, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'one_point')

    def test_class_c_5(self):
        params = {'a': -148, 'b': -148, 'x01': -147, 'y01': -1, 'a1': 3, 'b1': 4, 'x02': -147, 'y02': -1, 'a2': 4, 'b2': 3}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'one_point')

    def test_class_c_6(self):
        params = {'a': 148, 'b': 148, 'x01': 147, 'y01': 0, 'a1': 1, 'b1': 0, 'x02': 1, 'y02': 1, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'one_point')

    # Class D: Two Points (6 tests)
    def test_class_d_1(self):
        params = {'a': -148, 'b': -148, 'x01': -147, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': -148, 'y02': 0, 'a2': 1, 'b2': 0}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'two_points')

    def test_class_d_2(self):
        params = {'a': 148, 'b': 148, 'x01': 147, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': 148, 'y02': 0, 'a2': 1, 'b2': 0}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'two_points')

    def test_class_d_3(self):
        params = {'a': 50, 'b': 50, 'x01': 25, 'y01': 10, 'a1': 1, 'b1': 1, 'x02': 10, 'y02': 0, 'a2': 1, 'b2': 0}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'two_points')

    def test_class_d_4(self):
        params = {'a': -147, 'b': -147, 'x01': 5, 'y01': 5, 'a1': 1, 'b1': 1, 'x02': 147, 'y02': 0, 'a2': 1, 'b2': 0}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'two_points')

    def test_class_d_5(self):
        params = {'a': -148, 'b': -148, 'x01': -147, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': 5, 'y02': 0, 'a2': 1, 'b2': 0}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'two_points')

    def test_class_d_6(self):
        params = {'a': 148, 'b': 148, 'x01': 147, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': 5, 'y02': 0, 'a2': 1, 'b2': 0}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'two_points')

    # Class E: Three Points (6 tests)
    def test_class_e_1(self):
        params = {'a': -148, 'b': -148, 'x01': -148, 'y01': -148, 'a1': 1, 'b1': 0, 'x02': -148, 'y02': -148, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'three_points')

    def test_class_e_2(self):
        params = {'a': 148, 'b': 148, 'x01': 148, 'y01': 148, 'a1': 1, 'b1': 0, 'x02': 148, 'y02': 148, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'three_points')

    def test_class_e_3(self):
        params = {'a': 50, 'b': 30, 'x01': 0, 'y01': 0, 'a1': 1, 'b1': 0, 'x02': 0, 'y02': 0, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'three_points')

    def test_class_e_4(self):
        params = {'a': -147, 'b': -147, 'x01': 0, 'y01': 0, 'a1': 1, 'b1': 0, 'x02': 147, 'y02': 0, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'three_points')

    def test_class_e_5(self):
        params = {'a': -148, 'b': -148, 'x01': -147, 'y01': -147, 'a1': 1, 'b1': 0, 'x02': 0, 'y02': 0, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'three_points')

    def test_class_e_6(self):
        params = {'a': 148, 'b': 148, 'x01': 147, 'y01': 147, 'a1': 1, 'b1': 0, 'x02': 0, 'y02': 0, 'a2': 0, 'b2': 1}
        res = analyze_three_lines(params, self.N)
        self.assertEqual(res['case'], 'three_points')

    # Invalid Inputs (9 tests)
    def test_invalid_a_zero(self):
        params = {'a': 0, 'b': 3, 'x01': 0, 'y01': 3, 'a1': 3, 'b1': 2, 'x02': 2, 'y02': 0, 'a2': 6, 'b2': 4}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_invalid_normal_vector_1(self):
        params = {'a': 2, 'b': 3, 'x01': 0, 'y01': 3, 'a1': 0, 'b1': 0, 'x02': 2, 'y02': 0, 'a2': 6, 'b2': 4}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_invalid_range_a(self):
        params = {'a': 200, 'b': 3, 'x01': 0, 'y01': 3, 'a1': 3, 'b1': 2, 'x02': 2, 'y02': 0, 'a2': 6, 'b2': 4}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_invalid_b_zero(self):
        params = {'a': 2, 'b': 0, 'x01': 0, 'y01': 3, 'a1': 3, 'b1': 2, 'x02': 2, 'y02': 0, 'a2': 6, 'b2': 4}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_invalid_normal_vector_2(self):
        params = {'a': 2, 'b': 3, 'x01': 0, 'y01': 3, 'a1': 1, 'b1': 1, 'x02': 2, 'y02': 0, 'a2': 0, 'b2': 0}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_invalid_type_string(self):
        params = {'a': "abc", 'b': 3, 'x01': 0, 'y01': 3, 'a1': 1, 'b1': 1, 'x02': 2, 'y02': 0, 'a2': 1, 'b2': 1}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_invalid_type_float(self):
        params = {'a': 1.5, 'b': 3, 'x01': 0, 'y01': 3, 'a1': 1, 'b1': 1, 'x02': 2, 'y02': 0, 'a2': 1, 'b2': 1}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_exceed_max_y01(self):
        params = {'a': 2, 'b': 3, 'x01': 0, 'y01': 300, 'a1': 1, 'b1': 1, 'x02': 2, 'y02': 0, 'a2': 1, 'b2': 1}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

    def test_below_min_x02(self):
        params = {'a': 2, 'b': 3, 'x01': 0, 'y01': 0, 'a1': 1, 'b1': 1, 'x02': -300, 'y02': 0, 'a2': 1, 'b2': 1}
        with self.assertRaises(ValueError):
            analyze_three_lines(params, self.N)

if __name__ == "__main__":
    unittest.main()
