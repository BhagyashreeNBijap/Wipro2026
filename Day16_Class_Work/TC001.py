from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
print("title is",driver.title)
driver.get("https://www.google.com/")
print("title is",driver.title)
time.sleep(5)
driver.back()
print("Title after back",driver.title)
driver.forward()
print("Title after forward",driver.title)
