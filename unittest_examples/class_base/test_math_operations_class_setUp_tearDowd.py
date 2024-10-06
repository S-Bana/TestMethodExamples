import unittest
from .math_operations_class import Math


class TestMathOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Run befor, start class Math")

    def setUp(self):
        self.m1 = Math(5, 6)
        self.m2 = Math(9, 3)

    def test_add(self):
        self.assertEqual(self.m1.add(), 11)
        self.assertEqual(self.m2.add(), 12)

    def test_sub(self):
        self.assertEqual(self.m1.sub(), -1)
        self.assertEqual(self.m2.sub(), 6)

    def test_mul(self):
        self.assertEqual(self.m1.mul(), 30)
        self.assertEqual(self.m2.mul(), 27)

    def test_div(self):
        d = round(self.m1.div(), 3) # filter result to three decimal places , 0.833333333 --> 0.833
        self.assertEqual(d, 0.833)
        self.assertEqual(self.m2.div(), 3)
    
    def tearDown(self):
        print('Down')

    @classmethod
    def tearDownClass(cls):
        print("Run after, down class Math")


if __name__ == '__main__':
    unittest.main()
