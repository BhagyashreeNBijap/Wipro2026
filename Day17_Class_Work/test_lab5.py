from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_opencart_register_account():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get('https://tutorialsninja.com/demo')
        driver.maximize_window()

        if driver.title != 'Your Store':
            print(f"Title mismatch: {driver.title}")

        driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        driver.find_element(By.LINK_TEXT, "Register").click()

        heading = driver.find_element(By.CSS_SELECTOR, "#content h1")
        assert heading.text == 'Register Account'

        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        warning_text = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        if "Warning: You must agree to the Privacy Policy!" in warning_text:
            print("Warning Message Verified Successfully!")

        firstname_input = driver.find_element(By.ID, "input-firstname")
        firstname_input.send_keys("a" * 33)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        fn_error = driver.find_element(By.CSS_SELECTOR, "#account div.text-danger")
        if "First Name must be between 1 and 32 characters!" in fn_error.text:
            print(f"First Name validation successful: {fn_error.text}")

        time.sleep(1)

        driver.find_element(By.ID, "input-firstname").clear()
        driver.find_element(By.ID, "input-firstname").send_keys("Bhagya")
        driver.find_element(By.ID, "input-lastname").send_keys("N")
        driver.find_element(By.ID, "input-email").send_keys(
            f"bhagya{int(time.time())}@gmail.com"
        )
        driver.find_element(By.ID, "input-telephone").send_keys("9901118482")

        password_val = "Bhagya@123"
        driver.find_element(By.ID, "input-password").send_keys(password_val)
        driver.find_element(By.ID, "input-confirm").send_keys(password_val)

        driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

        policy_checkbox = driver.find_element(By.NAME, "agree")
        if not policy_checkbox.is_selected():
            policy_checkbox.click()

        driver.find_element(By.CSS_SELECTOR, "input[value='Continue']").click()

        success_msg = driver.find_element(By.CSS_SELECTOR, "#content h1").text
        if success_msg == "Your Account Has Been Created!":
            print("Verification Successful: Account Created!")

        driver.find_element(By.LINK_TEXT, "Continue").click()
        driver.find_element(By.LINK_TEXT, "View your order history").click()

        if "Order History" in driver.title:
            print("Successfully navigated to Order History page.")

    finally:
        time.sleep(3)
        driver.quit()
