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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui


driver = webdriver.Firefox()
driver.get('https://facebook.com/')
#page_url=driver.find_elements_by_xpath("//a[@class='content']")
all_title = driver.find_elements_by_class_name("title")
title = [title.text for title in all_title]
print(title)



