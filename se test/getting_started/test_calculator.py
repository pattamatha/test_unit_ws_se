from calculator import Calculator
from unittest.mock import Mock, patch
import pytest

@pytest.fixture
def instance():
    # setup phase before yield
    cal_instance = Calculator()
    yield cal_instance
    # teardown goes after "yield"

def test_add_positive_number(instance):
    result = instance.add(4, 3)

    assert result == 7

def test_add_negative_number(instance):
    result = instance.add(-1, -1)
    assert result == -2

def test_multiply_number(instance):
    result = instance.multiply(2, 6)

    assert result == 12

def test_devide_number(instance):
    result = instance.divide(6, 2)

    assert result == 3

def test_devide_b_zero(instance):
    with  pytest.raises(Exception) as e:
        result = instance.divide(4, 0)
    assert str(e.value) == "b cannot be zero"

@patch('calculator.AnotherClass')
def test_use_external(mock_anotherclass, instance):
    mock_instance = mock_anotherclass.return_value

    def mock_cases(value):
        if value <= 0:
            return True
        else:
            return False
        
    mock_instance.some_method.side_effect = mock_cases
    assert instance.use_external(6) == False
    assert instance.use_external(0) == True