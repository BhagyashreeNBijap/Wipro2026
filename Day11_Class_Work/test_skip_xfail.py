import sys
import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True

@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 2 * 2 == 5
