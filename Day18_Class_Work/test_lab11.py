from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.support.ui import Select, WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  


class HomePage:
    def __init__(self, driver):
        self.driver = driver  
        self.wait = WebDriverWait(driver, 10)  

        self.desktops = (By.LINK_TEXT, "Desktops") 
        self.mac = (By.PARTIAL_LINK_TEXT, "Mac") 
        self.search_box = (By.NAME, "search")  
        self.search_button = (By.CSS_SELECTOR, "button.btn-default") 

    def open_mac_page(self):
        desktops_menu = self.wait.until(EC.visibility_of_element_located(self.desktops))  
        ActionChains(self.driver).move_to_element(desktops_menu).perform()  
        self.wait.until(EC.element_to_be_clickable(self.mac)).click()  

    def search_product(self, product_name):
        self.wait.until(EC.presence_of_element_located(self.search_box)).send_keys(product_name)  
        self.driver.find_element(*self.search_button).click() 


class MacPage:
    def __init__(self, driver):
        self.driver = driver  
        self.wait = WebDriverWait(driver, 10)  

        self.heading = (By.TAG_NAME, "h2")  
        self.sort_dropdown = (By.ID, "input-sort")  
        self.add_to_cart = (By.XPATH, "//button[@onclick=\"cart.add('41', '1');\"]")  
        self.search_criteria = (By.ID, "input-search")  
        self.description_checkbox = (By.NAME, "description")  
        self.search_button = (By.ID, "button-search")  

    def verify_mac_heading(self):
        assert self.wait.until(EC.visibility_of_element_located(self.heading)).text == "Mac"  

    def sort_by_name_az(self):
        Select(self.wait.until(EC.presence_of_element_located(self.sort_dropdown))).select_by_visible_text("Name (A - Z)")  

    def add_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart)).click()  

    def advanced_search(self):
        criteria_box = self.wait.until(EC.presence_of_element_located(self.search_criteria)) 
        criteria_box.clear()  # clears Search Criteria
        self.driver.find_element(*self.description_checkbox).click()  
        self.driver.find_element(*self.search_button).click()  


driver = webdriver.Edge()  
driver.maximize_window()  
driver.get("https://tutorialsninja.com/demo/")  

home = HomePage(driver)  
mac = MacPage(driver)  

home.open_mac_page()  
mac.verify_mac_heading()  
mac.sort_by_name_az()  
mac.add_product_to_cart()  
home.search_product("Monitors")  
mac.advanced_search()  

driver.quit()  
