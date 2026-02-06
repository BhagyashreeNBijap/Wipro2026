from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Day18.Loginpage_PageFactory import loginpage_PageFactory
from Day18.TC003_Login import loginobj

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(5)
loginobj=loginpage_PageFactory(driver)

loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")

loginobj.clicklogin()
