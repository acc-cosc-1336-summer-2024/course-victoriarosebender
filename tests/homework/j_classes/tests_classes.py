#

import unittest
from src.homework.j_classes.class_a import Die



class Test_Config(unittest.TestCase):

 

    def test_get_rolled_value(self):
        die = Die()
        die.roll()
        
        self.assertIn( die.get_roll_value(), range(1,7))
    
     
