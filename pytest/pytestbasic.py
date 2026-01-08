# Pytest indepth
# Why pytest? Simple syntax and powerful fixtures good reporting , supports Ui
# and API and Unit tests
# Installing playwright with ci/cd is simple

#  Pytest is like testng + junit
# How pytest is declared? file starts with test_ or ends with _test.py
# Function starts with test_
# Classes starts with Test

# Example

def test_login():
    username = "sham"
    password = "Password123"

# Assertion in pytest
def test_sum():
    assert 10 +5 == 1

# Setup and teardown in pytest
import pytest
@pytest.fixture
def setup_teardown():
    # Setup code
    print("Setting up the test env")
    yield
    # Teardown code
    print("Tearing down the test env")

# How to use
def test_example(setup_teardown):
    print("Executing test")
    assert True

# Fixtures scopes
# Once per funcation/test
@pytest.fixture(scope="function")
def function_scope():
    print("Function scope setup")
    yield
    print("Function scope teardown")

# once per class
@pytest.fixture(scope="class")
def class_scope():
    print("Class scope setup")
    yield
    print("class scope teardown")

# Once per file
@pytest.fixture(scope="module")
def module_scope():
    print("Module setup")
    yield
    print("Module teardown")

# once per run
@pytest.fixture(scope="session")
def session_scope():
    print("Session setup")
    yield
    print("Session teardown")


# Pytest with data driven tests

import pytest
@pytest.mark.parametrize("input,expected", [
    (2,4),
    (3,9),
    (4,16)
])
def test_square(input, expected):
    assert input * input == expected

# Grouping tests in pytest
@pytest.mark.smoke
def test_smoke():
    assert True

@pytest.mark.regression
def test_regression():
    assert True

# To run specific group use -m option
# pytest -m smoke
# To run multiple groups use 'or' and 'and'
# pytest -m "smoke or regression"
# pytest -m "smoke and regression"
# To skip tests
import pytest

@pytest.mark.skip
def test_skip():
    assert True

@pytest.mark.skipif(condition=True)
def test_skipif():
    assert True

# To expect failures
import pytest
@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2

# To run pytest a file and generate report
# pytest pytestbasic.py --html=report.html
# To run in verbose mode
# pytest -v pytestbasic.py
# To run in parallel
# pytest -n 4 pytestbasic.py
# To capture logs in pytest
# pytest --log-cli-level=INFO pytestbasic.py
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def test_logging():
    logger.info("This is an info log")
    assert True
    logger.debug("This is a debug log")
    logger.error("This is an error log")

