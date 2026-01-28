import pytest


def test_addition():
    assert 5 + 3 == 8

def test_subtraction():
    assert 5 - 3 == 0, "Subtraction result is incorrect"

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)
