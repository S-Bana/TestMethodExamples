import unittest
from .math_operations_class import Math


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        m1 = Math(5, 6)
        m2 = Math(9, 3)
        self.assertEqual(m1.add(), 11)
        self.assertEqual(m2.add(), 12)

    def test_sub(self):
        m1 = Math(5, 6)
        m2 = Math(9, 3)
        self.assertEqual(m1.sub(), -1)
        self.assertEqual(m2.sub(), 6)

    def test_mul(self):
        m1 = Math(5, 6)
        m2 = Math(9, 3)
        self.assertEqual(m1.mul(), 30)
        self.assertEqual(m2.mul(), 27)

    def test_div(self):
        m1 = Math(5, 6)
        m2 = Math(9, 3)

        d = round(m1.div(), 3) # filter result to three decimal places , 0.833333333 --> 0.833
        self.assertEqual(d, 0.833)
        self.assertEqual(m2.div(), 3)


if __name__ == '__main__':
    unittest.main()
