from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Optional
chrome_options.add_argument("--disable-notifications")

# Specify path to chromedriver if it's not in PATH
# For example: '/usr/bin/chromedriver'
service = Service('/usr/bin/chromedriver')

# Create driver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Always use full URL with protocol
driver.get("https://www.gmail.com")

# Add wait to allow page to load (use WebDriverWait in real-world apps)
time.sleep(10)

try:
    # Attempting to login Gmail this way will fail because it's not a static login page,
    # but for demonstration, keeping your structure
    driver.find_element(By.ID, "identifierId").send_keys("chsambireddy@gmail.com")
    driver.find_element(By.ID, "password").send_keys("pass123")
    driver.find_element(By.ID, "identifierNext").click()
    time.sleep(3)

    # Gmail doesn't use "password" ID directly, so below will fail
    # Add custom logic with waits to proceed further

    # Example assertion - change depending on actual page
    assert "Gmail" in driver.title

finally:
    driver.quit()