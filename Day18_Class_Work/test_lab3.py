from selenium import webdriver  
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.support.ui import Select, WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

driver = webdriver.Edge() 
driver.maximize_window() 
driver.get("https://tutorialsninja.com/demo/")  

wait = WebDriverWait(driver, 10) 

desktops = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))  
actions = ActionChains(driver) 
actions.move_to_element(desktops).perform()  

mac = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mac")))  
mac.click()  

sort_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "input-sort"))))  
sort_dropdown.select_by_visible_text("Name (A - Z)")  

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick=\"cart.add('41', '1');\"]"))).click()  

driver.quit()  
