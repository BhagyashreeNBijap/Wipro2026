from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https:\\www.amazon.in")
time.sleep(5)
links=driver.find_elements(By.TAG_NAME,"a")

for link in links:
    url=link.get_attribute("href")
    text=link.text.strip()
    print(text)
