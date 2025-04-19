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


options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://python.org")
print(driver.title)
driver.close()
