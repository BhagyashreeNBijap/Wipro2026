from selenium import webdriver
import time

def test_open_orangehrm_chrome():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)

    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

    driver.quit()
