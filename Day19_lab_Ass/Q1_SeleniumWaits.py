'''1.Selenium Waits		
Write a Selenium script that:		
1. Demonstrates implicit wait	
2. Demonstrates explicit wait for an element to become clickable		
3. Demonstrates fluent wait with a polling interval		
4. Prints a message when the element is available for interaction	'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Implicit Wait
driver.implicitly_wait(10)
print("Implicit wait applied")

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Click Enable button
enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
enable_btn.click()

# 2. Explicit Wait – wait until textbox is clickable
wait = WebDriverWait(driver, 10)
textbox = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
)
print("Explicit wait: Textbox is clickable")

# 3. Fluent Wait – polling interval
fluent_wait = WebDriverWait(
    driver,
    timeout=15,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

textbox = fluent_wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
)

# 4. Print Message
print("Fluent wait: Element is available for interaction")

textbox.send_keys("Selenium Waits Working")

time.sleep(3)
driver.quit()
