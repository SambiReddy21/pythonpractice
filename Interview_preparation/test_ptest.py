import pytest

@pytest.fixture
def test_data():
    return {"name": "sagar", "age": 45}

    
def test_addition(test_data):
    assert test_data["name"] == "sagar","name is not correct"