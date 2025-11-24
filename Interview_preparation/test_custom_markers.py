
import pytest

@pytest.mark.great
def test_greater():
    num = 200
    assert num > 100

@pytest.mark.slow
def test_long_process():
    assert sum(range(1000000)) == 499999500000
    
#Running tests with markers : pytest -m <marker_name> <file_name>
#pytest -m great test_custom_markers.py

"""
---------------------- Test reporing and output -------------------

To se the detailed output of tests execution we can use below cmd
 pytest -v                             
 
It shows test function name and its state either passed or failed.

To see print statements output from test functions we can use below
 pytest -s


------------- running tests in parallel ----------------------

we can run tests parallelly on multiple CPU cores.We have to use plugin pytest-xdist . It is used to run lare test suites to spped up the process.

pytest -n 4 (Runs on  cpu cores)


---------------------- assert statement --------------------

assert statement is used for debugging and testing purposes.If condition evaluates to True then continues to execute otherwise gives AssertionError with default message.

assert statement compares actual result with expected output.

assert 2+3 == 5,"Result should be 5"

2+3 is actual result, 5 is expected output.And the message is to know the details about failed condition.

It is used in unit tests and pytest.

"""