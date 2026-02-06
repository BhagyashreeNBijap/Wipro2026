''' Handling iFrames and Windows Write a Selenium script that: 
1. Switches to an iframe and enters text in an input field inside it 
2. Switches back to the main content 
3. Opens a new browser window or tab 
4. Switches between windows and prints each window title 
5. Closes the child window and returns to the parent '''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://letcode.in/frame")

# 1: Switch to iframe and enter text

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

driver.find_element(By.NAME, "fname").send_keys("Bhagya")
driver.find_element(By.NAME, "lname").send_keys("N")


# 2: Switch back to main content

driver.switch_to.default_content()

# 3: Open a new browser window / tab

driver.execute_script("window.open('https://www.amazon.in','_blank');")
time.sleep(3)

# 4: Switch between windows and print titles

windows = driver.window_handles

parent_window = windows[0]
child_window = windows[1]

driver.switch_to.window(child_window)
print("Child Window Title:", driver.title)

driver.switch_to.window(parent_window)
print("Parent Window Title:", driver.title)

# 5: Close child window and return to parent

driver.switch_to.window(child_window)
driver.close()

driver.switch_to.window(parent_window)

# Close browser
driver.quit()
