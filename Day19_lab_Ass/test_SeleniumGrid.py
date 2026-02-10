from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Selenium Grid Hub URL
GRID_URL = "http://localhost:4444/wd/hub"

URL = "https://www.google.com"
EXPECTED_TITLE = "Google"

def run_test(options):
    # 1. Connect to Selenium Grid using RemoteWebDriver
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    try:
        # 3. Navigate to website and verify page title
        driver.get(URL)
        assert EXPECTED_TITLE in driver.title

        # 4. Print browser name and platform
        print("Browser Name:", driver.capabilities.get("browserName"))
        print("Platform:", driver.capabilities.get("platformName"))
        
    finally:
        driver.quit()

# 2. Run same test on multiple browsers
# Chrome
chrome_options = ChromeOptions()
chrome_options.set_capability("platformName", "WINDOWS")
run_test(chrome_options)

# Firefox
firefox_options = FirefoxOptions()
firefox_options.set_capability("platformName", "WINDOWS")
run_test(firefox_options)
