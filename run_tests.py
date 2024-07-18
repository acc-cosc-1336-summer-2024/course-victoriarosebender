import unittest



'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.j_classes import tests_classes ##edit the tests_dictionaries_and_sets AND i_dictionaries_sets sto the correct hw assignment

suite = unittest.TestLoader().loadTestsFromModule(tests_classes) ##edit the tests_dictionaries_and_sets to the correct hw assignment
unittest.TextTestRunner(verbosity=2).run(suite)
