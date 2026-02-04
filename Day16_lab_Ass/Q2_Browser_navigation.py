'''Question 4 – Browser Navigation Write a Selenium WebDriver script that: 
1. Opens a browser and navigates to https://example.com
2. Navigates to another page on the same site 
3. Uses back(), forward(), and refresh() 
4. Prints the page title after each navigation 
5. Closes the browser for this question from selenium import webdriver import time''''

from selenium import webdriver
import time

# Open browser
driver = webdriver.Chrome()
driver.maximize_window()

# 1️ Navigate to example.com
driver.get("https://example.com")
time.sleep(2)
print("Home Page Title:", driver.title)

# 2️ Navigate to another page on same site
driver.get("https://www.iana.org/domains/example")
time.sleep(2)
print("Second Page Title:", driver.title)

# 3Back navigation
driver.back()
time.sleep(2)
print("After Back Title:", driver.title)

# 4️ Forward navigation
driver.forward()
time.sleep(2)
print("After Forward Title:", driver.title)

# 5️ Refresh page
driver.refresh()
time.sleep(2)
print("After Refresh Title:", driver.title)

# Close browser
driver.quit()
