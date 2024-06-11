import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

from src.examples.c_decisions.decisions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_options_ratio(self):
        self.assertEqual(get_options_ratio(10, 20), 0.5)
        self.assertEqual(get_options_ratio(10, 20), 0.5)

