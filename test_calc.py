import unittest
import calculator as calc

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.add(1.5, 5), 6.5)
    def test2(self):
        self.assertEqual(calc.subtract(5, 4), 1)
    def test3(self):
        self.assertEqual(calc.divide(6.5, 2), 3.25)
    def test4(self):
        self.assertEqual(calc.multiply(2.5, 3), 7.5)

if __name__ == "__main__":
    unittest.main()