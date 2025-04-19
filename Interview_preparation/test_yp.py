"""
Pytest is a testing framework in python to write test cases easily.It is an ideal tool for unit testing,functional testing and integration testing.

Pytest automatically identifies the files which starts with test_* or *_test and then run them.
The test functions should start with prefix test_.Otherwise pytest don't consider as test functions.

-------------- keyfeatures--------------------

Simple syntax : Functions are written with plain assert statement,makes code easily to write and read
Parameterized tests : Same test can run with multiple sets of input
Automatic discovery : Pytest automatically detects and run the test files which starts with test_
Fixtures: Fixtures help to manage setup and teardown in testing environment,enables code reuse across mutiple tests.

------------- Writing and running tests with pytest -----------

In pytest tests are written as functions starting with test_ and using assert statement.

"""

def test_sum():
    assert 2+3 == 5, "sum should be 5"
    
def test_multiply():
    assert 4*5 == 20, "results should be 20"
    
"""
Ways To run : 
  1.pytest
  2.pytest test_sample.py
  3.pytest -k sample
         
If we give only pytest, then it detects all of the files starts with test_ in a directory and sub directories and run them.

... dots indicates tests are passed , each dot is one test

---------------------- Test Fixtures -----------------------------

Fixtures are functions used to manage setup and teardown across multiple tests in the test file , such as database connections,file I/o and other test dependencies.
Fixures are created by using @pytest.fixture decorator.
Then it can be used as argument to test functions.Means fixures can apply on tests.So before run the tests fixures will run and return the data to tests.
"""

import pytest

@pytest.fixture
def emp_data():
    return {"name" : "Ram" , "no" : 27}

def test_get_emp_data(emp_data):
    assert emp_data['name'] == "Ram","Emp is not in the records"
    assert emp_data["no"] == 27, "Emp number is not in the records"
    
"""
--------------------- parameterized tests -------------------------

Pytest allows to run same test with multiple sets of data by using @pytest.mark.parametrize decorator.

"""

import pytest

@pytest.mark.parametrize("a,b,expected_op" ,[(2,3,5),(6,7,13),(1,-1,0)])

def test_addition(a,b,expected_op):
    assert a+b == expected_op
    
@pytest.mark.parametrize("x,y",[(1,11),(3,33)])

def test_multiply(x,y):
    11 * x == y
    print("printed")
    
###---------------- Grouping tests into classes -----------------------

#We can organize the tests in class for better structure.Pytest can indentify and run them.

class TestMathOperations:

    def test_addition(self):
        assert 1 + 1 == 2

    def test_subtraction(self):
        assert 2 - 1 == 1
        
"""
----------------------------- Markers -------------------------------------

Markers are used to group the tests. We can use built-in markers or create custom makers to run the tests or skip the certain tests.

----- Built-in markers ----------

@pytest.mark.xfail : If we expected a test to fail then we can mark the test as xafil.If fails it prints "expectedly fail"(xfail) or passes unexpectedly then prints "unexpectedly passed"(xpass).

@pytest.mark.skip : If we want to skip certian tests to not run then we can amrk the tests as skip.

@pytest.mark.skipif : If we want to skip tests based on conditions then we can use it.

@pytest.mark.filterwarnings : To ignore warnings during the execution of tests.

@pytest.mark.usefixtures : To indicate certain tests to use one or more fixtures.

@pytest.mark.parametrize : To run same test with multiple sets of data.

"""
import pytest

@pytest.mark.xfail(reason="making test to fail")
def test_add():
    assert 3-2 == 9
    
@pytest.mark.xfail(reason= "Making test to fail")
def test_multiply():
    assert 3*4 == 12
    
@pytest.mark.skip(reason="skipping this test")
def test_show():
    print("skipping")
    assert False
    
@pytest.fixture
def setup_data():
    return{"name" : "Abhi"}

@pytest.mark.usefixtures("setup_data")
def test_getdata(setup_data):
    assert setup_data["name"] == "Ram"

