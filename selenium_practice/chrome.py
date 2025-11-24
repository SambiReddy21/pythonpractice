# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("www.gmail.com/login")

# driver.find_element(By.ID,"username").send_keys("testuser")
# driver.find_element(By.ID, "password").send_keys("pass123")
# driver.find_element(By.ID, "loginBtn").click()


# assert "Dashboard" in driver.title
# driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
options = Options()
# Uncomment the line below if you want to run it in headless mode
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.python.org")
    print("Page Title:", driver.title)
finally:
    driver.quit()  # Use quit() to ensure complete cleanup of browser process
