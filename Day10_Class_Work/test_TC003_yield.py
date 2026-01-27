import pytest

@pytest.mark.smoke
def test_smoke():
    assert True

@pytest.fixture()

def setup_teardown():
    print("setup")
    yield
    print("teardown")


def test_example(setup_teardown):
    print("test1 running")

def test_example1(setup_teardown):
    print("test2 running")
