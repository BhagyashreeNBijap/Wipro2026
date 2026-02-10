import pytest
from Day20.driverfactory import get_driver


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_title(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_search(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("selenium grid")
    search_box.submit()
    assert "selenium grid" in driver.Title
    driver.quit()
