#

import unittest
from src.homework.j_classes.class_a import Die



class Test_Config(unittest.TestCase):

 

    def test_get_rolled_value(self):
        needed_tests = 3
        counter = 0
        die = Die()

        while counter < needed_tests:
        
            die.roll()
        
            self.assertIn( die.get_roll_value(), range(1,7))

            counter += 1

    
     
