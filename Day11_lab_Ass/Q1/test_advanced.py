import pytest

# Parameterization

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (10, 20, 30),
    (-1, 1, 0)
])
def test_addition(a, b, expected):
    assert a + b == expected


#  CUSTOM CLI OPTION

def test_environment(env):
    print(f"\nRunning tests in {env} environment")
    assert env in ["dev", "test", "prod"]


# SKIP TEST

@pytest.mark.skip(reason="Feature under development")
def test_skip_example():
    assert True


#EXPECTED FAILURE

@pytest.mark.xfail(reason="Known bug: division by zero")
def test_expected_failure():
    assert 10 / 0 == 5


# CONDITIONAL SKIP

@pytest.mark.skipif(True, reason="Skipping due to environment condition")
def test_conditional_skip():
    assert True
