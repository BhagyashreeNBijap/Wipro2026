'''Question 2 – Unit Testing & Test Driven Development (TDD)
Implement Test Driven Development (TDD) for a simple calculator module.
Requirements:  

1. Write unit test cases first for operations: Addition Subtraction Multiplication Division
2. Use a Python unit testing framework (unittest or pytest)

**test_Q2_Calculator.py
import pytest
from Q2_Calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

3. Implement the calculator functions to make the tests pass
Q2_Calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

4. Demonstrate handling of edge cases (e.g., division by zero)
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
5. Explain the TDD cycle: Red → Green → Refactor
Red:
    Write test cases first
    Run tests → They fail
Green:
    Write minimum code to pass the tests.
    Run tests → They pass.
Refactor:
    Improve code structure without changing behavior.
    Optimize readability and performance

