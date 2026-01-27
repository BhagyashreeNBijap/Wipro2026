'''Question 1 – Pytest Basics, Test Discovery & Assertions Pytest overview, Test discovery, Writing and running unit tests, Assert statements and exceptions
Requirements:
1. Write unit tests using Pytest conventions (test_*.py, test_ functions)
2. Demonstrate automatic test discovery

import pytest

def test_addition():
    assert 2+3 == 5

def test_sub():
    assert 8-2 == 6

def test_multiplication():
    assert 4*3 == 12

def test_division():
    assert 4/2 == 2

3. Use assert statements to validate results
def test_multiplication():
    assert 4 * 3 == 12

4. Write a test to validate that an exception is raised for division by zero
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(2, 0)

5. Execute tests using the pytest command
pytest




