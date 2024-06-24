import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
from src.examples.d_repetition.repetition import test_config
 
class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())



    def test_factorial(self):
        self.assertEqual(get_factorial(4), 24)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(6), 120)

    def test_sum_odd_num(self):
        self.assertEqual(sum_odd_numbers(7), 16)
        self.assertEqual(sum_odd_numbers(9), 25)
        self.assertEqual(sum_odd_numbers(10), 25)

