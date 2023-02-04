import inspect
import json
import pytest
from files.tools.col import Col
from Shape.utilities import Utilities
import dotenv
from files.tools.numbers.comp import *


dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def test_col():
    return Col()


@pytest.mark.test_compress
def test_compress(test_col):
    try:
        assert test_col.compress(json.loads(os.getenv("FILES_TO_ZIP"))) == \
               int(os.getenv("TRUE_TEST_COMPRESS"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS") + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED") + "\n")
