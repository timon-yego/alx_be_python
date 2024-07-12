import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()


    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-8, 3), -5)
        self.assertEqual(self.calc.add(7, 3), 10)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(-1, -3), 3)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(9, 0), None)
        self.assertEqual(self.calc.divide(0, 4), 0)

if __name__ == "__main__":
    unittest.main()