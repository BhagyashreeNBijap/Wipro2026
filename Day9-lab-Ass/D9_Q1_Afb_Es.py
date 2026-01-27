'''#Question 1 – Automation Framework Basics & Environment Setup
Topics Covered:
Introduction to automation frameworks in Python, Setting up the development environment 
Design a basic Python automation testing framework.
Requirements:

1. Set up a virtual environment
python -m venv venv

to activate:  venv\Scripts\activate

2. Install required tools and libraries (e.g., pytest or unittest)
pip install pytest

3. Create a project structure for an automation framework (tests, utilities, configuration)
tests → Contains test scripts

utilities → Common reusable functions

config → Stores environment configuration

4. Explain the role of:
Test Runner: It execute test case and provide result
Test Report: Test reports show test execution results in a readable format
             It Shows passed/failed test cases 
             Execution time
Configuration File : configuration files store environment settings separately from code  
                     [ENV]="qa"
                     timeout = 10

5. Write a sample test case to validate a simple function
   import pytest
def add(a, b):
    return a + b

def test_add():
    result = add(2, 3)
    assert result == 5


 
