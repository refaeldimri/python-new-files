import inspect
import os

import pytest
from Shape.shapes.calc import Calc
from Shape.utilities import Utilities
import dotenv
from files.tools.numbers.comp import *


dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def test_comp():
    return Simp()


@pytest.mark.test_sum_digits
def test_sum_digits(test_comp):
    param = int(os.getenv("PARAM_SUM_DIGITS"))
    result = test_comp.addNumbers(int(os.getenv("TEST_SUM_DIGITS_NUMBER_ONE")),
                                  int(os.getenv("TEST_SUM_DIGITS_NUMBER_TWO")))
    try:
        assert sum_of_digits(param) == result
        utilities.write_file\
            (str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS") + str(param) + "\n")
    except AssertionError:
        utilities.write_file\
            (str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED") + str(param) + "\n")


@pytest.mark.test_sum_digits_neg
def test_sum_digits_neg(test_comp):
    param = os.getenv("PARAM_SUM_DIGITS")
    result = 6
    try:
        assert sum_of_digits(param) == result
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(param) + "\n")
    except PermissionError as e:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(param) + ". " + str(e) + "\n")

