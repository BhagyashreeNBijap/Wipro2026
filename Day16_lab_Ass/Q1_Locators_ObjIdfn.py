''' –Locators & Object Identification 
1. Finds elements using ID, Name, Class Name, XPath, and CSS Selector 
2. Enters text in input fields and clicks a submit button 
3. Validates a message displayed on the page'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestQ3Locators():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_locators_object_identification(self):
        driver = self.driver

        # Open site
        driver.get("https://tutorialsninja.com/demo/")

        # CSS Selector
        driver.find_element(By.CSS_SELECTOR, ".fa-user").click()
        driver.find_element(By.LINK_TEXT, "Register").click()

        # ID locator
        driver.find_element(By.ID, "input-firstname").send_keys("Bhagya")
        driver.find_element(By.ID, "input-lastname").send_keys("N")
        driver.find_element(By.ID, "input-email").send_keys("bhagya" + str(int(time.time())) + "@gmail.com")
        driver.find_element(By.ID, "input-telephone").send_keys("9901118482")
        driver.find_element(By.ID, "input-password").send_keys("abc@123")
        driver.find_element(By.ID, "input-confirm").send_keys("abc@123")

        # Name locator
        driver.find_element(By.NAME, "agree").click()

        # Class Name locator
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        # XPath locator + Validation
        success_text = driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        assert success_text == "Your Account Has Been Created!"
