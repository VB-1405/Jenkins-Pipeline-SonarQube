import pytest
from mathutils_py import MathUtils

@pytest.fixture
def math_utils():
    return MathUtils()

def test_add(math_utils):
    assert math_utils.add(1, 2) == 3
    assert math_utils.add(-1, 1) == 0
    assert math_utils.add(0, 0) == 0
    assert math_utils.add(-5, -3) == -8
    
def test_subtract(math_utils):
    assert math_utils.subtract(5, 2) == 3
    assert math_utils.subtract(2, 5) == -3
    assert math_utils.subtract(0, 0) == 0
    assert math_utils.subtract(-5, -3) == -2
    
def test_multiply(math_utils):
    assert math_utils.multiply(2, 3) == 6
    assert math_utils.multiply(-2, 3) == -6
    assert math_utils.multiply(0, 5) == 0
    assert math_utils.multiply(-4, -2) == 8
    
def test_divide(math_utils):
    assert math_utils.divide(10, 2) == 5.0
    assert math_utils.divide(7, 2) == 3.5
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        math_utils.divide(1, 0)
    assert math_utils.divide(-10, 2) == -5.0
    assert math_utils.divide(0, 5) == 0.0