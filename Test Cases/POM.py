from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.login_page import LoginPage

#Test Setup
browser = webdriver.Chrome()
test_value = 'Test passed'

#Test
log_page = LoginPage(driver=browser)
log_page.go()
log_page.user_name_field().web_element.
browser.quit()
print(test_value)