from selenium import webdriver

from pages.login_page import LoginPage

#Test Setup
browser = webdriver.Chrome()

#Test
log_page = LoginPage(driver=browser)
log_page.go()
log_page.user_name_field.input_text('hr.doctor@hospitalrun.io')
log_page.password_field.input_text('HRt3st12')
log_page.login_button.click()

browser.quit()
