import unittest
from my_calculator import calculate

class TestMyCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(2, 3, '+'), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(6, 4, '-'), 2)

    def test_multiplication(self):
        self.assertEqual(calculate(2, 3, 'x'), 6)

    def test_multiply_decimal(self):
        self.assertEqual(calculate(1.5, 3, 'x'), 4.5)

    def test_division(self):
        self.assertEqual(calculate(6, 2, '/'), 3)

    def test_divid_by_zero(self):
        self.assertEqual(calculate(1234567898765432, 0, '/'), 'Error')


if __name__ == '__main__':
    unittest.main()