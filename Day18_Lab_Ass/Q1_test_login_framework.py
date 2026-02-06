'''Question 7 – Automation Framework (POM) Write a Selenium automation framework that: 
1. Implements Page Object Model (POM) 
2. Separates page classes, test scripts, and configuration 
3. Creates reusable methods for common actions (click, input, select) 
4. Runs a test using pytest or unittest and prints results'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time

# 2️ – Configuration

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
BROWSER = "chrome"

# 3️ – Reusable common actions methodS
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def enter_text(self, element, value):
        element.clear()
        element.send_keys(value)

    def select_by_text(self, element, text):
        Select(element).select_by_visible_text(text)

# 1️ – Page Object Model (POM)

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")

    # Page Action
    def login(self, user, pwd):
        self.enter_text(self.driver.find_element(*self.username), user)
        self.enter_text(self.driver.find_element(*self.password), pwd)
        self.click(self.driver.find_element(*self.login_button))

#  4️ – pytest Setup & Test Execution

@pytest.fixture
def setup():
    if BROWSER == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(setup):
    driver = setup
    driver.get(URL)

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    time.sleep(3)

    assert "dashboard" in driver.current_url
    print(" Login Test Passed Successfully")
