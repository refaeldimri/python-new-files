import inspect
import os

import pytest
from Shape.utilities import Utilities
import dotenv
from files.tools.numbers.simp import *


dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def test_simp():
    return Simp()


@pytest.mark.test_add_numbers
def test_add_numbers(test_simp):
    num1 = float(os.getenv("TEST_ADD_NUMBER_NUM1"))
    num2 = float(os.getenv("TEST_ADD_NUMBER_NUM2"))
    result = float(os.getenv("TEST_ADD_NUMBER_RESULTS"))
    try:
        assert test_simp.addNumbers(num1, num2) == result
        utilities.write_file(str(inspect.currentframe().f_code.co_name) + " " +
                             os.getenv("TEST_PASS") + " with param: " + "(" + str(num1) + ", " + str(num2) + ")" + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED") +
                             " with param: " + "(" + str(num1) + ", " + str(num2) + ")" + "\n")


def test_sub_numbers(test_simp):
    num1 = float(os.getenv("TEST_ADD_NUMBER_NUM1"))
    num2 = float(os.getenv("TEST_ADD_NUMBER_NUM2"))
    result = float(os.getenv("TEST_SUB_NUMBER_RESULTS"))
    try:
        assert test_simp.subNumbers(num1, num2) == result
        utilities.write_file(str(inspect.currentframe().f_code.co_name) + " " +
                             os.getenv("TEST_PASS") + " with param: " + "(" + str(num1) + ", " + str(num2) + ")" + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED") +
                             " with param: " + "(" + str(num1) + ", " + str(num2) + ")" + "\n")
