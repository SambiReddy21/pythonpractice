# import unittest
# from selenium import webdriver


# class GoogleTestCase(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.addCleanup(self.driver.quit)

#     def test_page_title(self):
#         self.driver.get('https://www.google.com')
#         self.assertIn('Google', self.driver.title)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)




"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui


driver = webdriver.Firefox()
driver.get('https://facebook.com/')
#page_url=driver.find_elements_by_xpath("//a[@class='content']")
all_title = driver.find_elements_by_class_name("title")
title = [title.text for title in all_title]
print(title)

"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# Optional: Run Firefox in headless mode
options = Options()
# options.add_argument('--headless')  # Uncomment for headless mode

# Setup WebDriver with GeckoDriver
driver = webdriver.Firefox(service=Service("/snap/bin/firefox.geckodriver"))

try:
    driver.get('https://www.facebook.com/')
    
    # Example: Find all elements with the class 'title' (note: Facebook may not use this class)
    all_title = driver.find_elements(By.CLASS_NAME, "title")
    titles = [title.text for title in all_title]
    print(titles)
finally:
    driver.quit()


