import unittest
from src.homework.i_dictionaries_and_sets import get_p_distance
from src.homework.i_dictionaries_and_sets import get_p_distance_matrix 


'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.c_decisions import tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
unittest.TextTestRunner(verbosity=2).run(suite)
