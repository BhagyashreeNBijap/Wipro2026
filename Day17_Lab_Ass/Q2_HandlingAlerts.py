'''Handling Alerts and Pop-ups Write a Selenium script that: 
1. Triggers a JavaScript alert 
2. Accepts the alert and prints its message 
3. Dismisses a confirmation pop-up 
4. Enters text in a prompt alert and accepts it 
5. Verifies the result displayed on the page'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")

wait = WebDriverWait(driver, 10)

# 1. Trigger a simple JavaScript alert
driver.find_element(By.ID, "alertButton").click()

alert = wait.until(EC.alert_is_present())
print("Alert message:", alert.text)
alert.accept()

# 2. Trigger confirmation alert and dismiss it
confirm_btn = driver.find_element(By.ID, "confirmButton")
driver.execute_script("arguments[0].click();", confirm_btn)

confirm_alert = wait.until(EC.alert_is_present())
confirm_alert.dismiss()

# 3. Verify confirmation result on page
confirm_result = wait.until(
    EC.visibility_of_element_located((By.ID, "confirmResult"))
)
print("Confirmation result:", confirm_result.text)

# 4. Trigger prompt alert, enter text and accept it
prompt_btn = driver.find_element(By.ID, "promtButton")
driver.execute_script("arguments[0].click();", prompt_btn)

prompt_alert = wait.until(EC.alert_is_present())
prompt_alert.send_keys("Bhagyashree")
prompt_alert.accept()

# 5. Verify prompt result displayed on page
prompt_result = wait.until(
    EC.visibility_of_element_located((By.ID, "promptResult"))
)

if "Bhagyashree" in prompt_result.text:
    print("Prompt alert handled successfully – Test Passed")
else:
    print("Prompt alert handling failed – Test Failed")

# Close browser
driver.quit()
