'''Question 2 – Setup/Teardown, Fixtures & conftest.py 
1. Implement xUnit-style methods (setup_module, teardown_module, setup_function, teardown_function)''

import pytest

def setup_module():
    print("\nSetup before module")

def teardown_module():
    print("\nTeardown after module")

def setup_function():
    print("\nSetup before each test")

def teardown_function():
    print("\nTeardown after each test")

def test_add():
    assert 2 + 3 == 5

def test_sub():
    assert 5 - 3 == 2

#2. Create reusable fixtures for test data and resources
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]


#3. Move common fixtures to a conftest.py file
import pytest

@pytest.fixture(scope="module")
def db_connection():
    print("\nConnecting to DB")
    yield "DB Connected"
    print("\nClosing DB Connection")

4. Demonstrate fixture scope (function, module)
@pytest.fixture(scope="function")
def func_fixture():
    return "Function Level"

@pytest.fixture(scope="module")
def module_fixture():
    return "Module Level"

5. Use fixtures in multiple test file
def test_user(db_connection):
    assert db_connection == "DB Connected"


def test_order(db_connection):
    assert db_connection == "DB Connected"
