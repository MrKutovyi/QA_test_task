from selenium import webdriver

from pages.base_element import BaseElement
from pages.login_page import LoginPage

# Test Setup
browser = webdriver.Chrome()

# Unsuccessful Login
log_page = LoginPage(driver=browser)
log_page.go()
log_page.user_name_field.input_text('hr.doctor@hospitalrun.io')
log_page.password_field.input_text('wrong')
log_page.login_button.click()
assert log_page.error_message.text == "Username or password is incorrect.", "The text is wrong"

browser.quit()
