''' Handling Web Controls Write a Selenium script that: 
1. Fills text boxes 
2. Selects radio buttons and checkboxes 
3. Chooses an option from a drop-down list using the Select class 
4. Submits the form and verifies a confirmation message'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

wait = WebDriverWait(driver, 10)

# 1. Fill text boxes
driver.find_element(By.NAME, "my-text").send_keys("Bhagyashree")
driver.find_element(By.NAME, "my-password").send_keys("12345")

# 2. Select radio button and checkbox
driver.find_element(By.ID, "my-radio-1").click()
driver.find_element(By.ID, "my-check-1").click()

# 3. Select option from drop-down using Select class
dropdown = Select(driver.find_element(By.NAME, "my-select"))
dropdown.select_by_visible_text("Two")

# 4. Submit the form
driver.find_element(By.TAG_NAME, "button").click()

# Verify confirmation message
message = wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
)

if "Received!" in message.text:
    print("Form submitted successfully – Test Passed")
else:
    print("Test Failed")

# Close browser
driver.quit()
