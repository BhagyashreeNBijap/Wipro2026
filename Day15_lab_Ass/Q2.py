from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestQues2:
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self, method):
        self.driver.quit()

    def test_ques2(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        username = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username.send_keys("Admin")

        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        dashboard_header = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.oxd-text--h6"))
        )

        assert dashboard_header.text == "Dashboard"
