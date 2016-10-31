import unittest
from bisection import Bisection


class TestBisection(unittest.TestCase):
    def setUp(self):
        self.bisectionObject = Bisection("3x**2+5x", 'x')

    def test_should_get_interval(self):
        self.assertEqual(6, self.bisectionObject.getInterval(7, 5))

    def test_should_be_below_to_zero(self):
        self.assertEqual(False, self.bisectionObject.below_to_zero(7, -5))

    def test_should_calculate_absolute_error(self):
        self.assertEqual(2, self.bisectionObject.get_absolute_error(4, 2))

    def test_should_calculate_percentual_error(self):
        self.assertEqual(50.0, self.bisectionObject.get_percentual_error(4, 2))

    def _test_should_solve_equation(self):
        self.assertEqual(8, self.bisectionObject.solve(8))

    def test_should_solve_bisection(self):
        self.assertEqual('Cannot solve bisection', self.bisectionObject.solveBisection(0, 0, -1))


if __name__ == '__main__':
    unittest.main()
