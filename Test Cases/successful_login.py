from selenium import webdriver

from pages.base_element import BaseElement
from pages.login_page import LoginPage

# Test Setup
browser = webdriver.Chrome()
currentURL = None

# Successful Login
log_page = LoginPage(driver=browser)
log_page.go()
log_page.user_name_field.input_text('hr.doctor@hospitalrun.io')
log_page.password_field.input_text('HRt3st12')
log_page.login_button.click()
# log_page.check_url()
currentURL = log_page.getCurrentUrl()
print(log_page.currentURL)
# assert browser.current_url == "http://demo.hospitalrun.io/#/patients"
browser.quit()
