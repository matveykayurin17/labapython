import unittest
from src.calc import calc
class TestCalc(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calc('1+1'),2.0)
        self.assertEqual(calc('1-1/2'), 0.5)
        self.assertEqual(calc('2%1*1'),0.0)
        self.assertEqual(calc('5+1#2'),5.0)
