import pytest

@pytest.mark.parametrize("a,b,result", [(1,2,3), (3,4,7)])
def test_add(a, b, result):
    assert a + b == result
    
def test_substraction():
    assert 3-2 == 1

#Fixtures
#Reusable components to set up state before tests run (like connections, mocks, configurations).    
import pytest

@pytest.fixture
def sample_dict():
    return {"key": "value"}

def test_key(sample_dict):
    assert sample_dict["key"] == "value"    
    
#Powerful Assertions
#pytest shows detailed output when assertions fail, making debugging easier.
def test_list():
    my_list = [1, 2, 3]
    assert 4 in my_list 
    
    