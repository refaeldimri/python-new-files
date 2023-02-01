import unittest
from files.tools.col import Col
from files.tools.numbers.simp import Simp
from files.tools.numbers.comp import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        init the variables
        :return None
        """
        self.col = Col()
        self.simp = Simp()

    def test_comp_sum_of_digits(self):
        assert sum_of_digits(123) == 6

    def test_simp_add(self):
        assert self.simp.addNumbers(6, 7) == 13

    def test_simp_sub(self):
        assert self.simp.subNumbers(6, 7) == -1

    def test_call_func_before_call_simp(self):
        assert sum_of_digits(123) == "You Can not use this function before you use at least one simp class's function"

    def test_call_func_after_call_simp(self):
        self.simp.addNumbers(4, 34)
        assert sum_of_digits(123) == 6




