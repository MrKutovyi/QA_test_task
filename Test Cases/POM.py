from selenium import webdriver

from pages.login_page import LoginPage

#Test Setup
browser = webdriver.Chrome()

#Successfull Login
# log_page = LoginPage(driver=browser)
# log_page.go()
# log_page.user_name_field.input_text('hr.doctor@hospitalrun.io')
# log_page.password_field.input_text('HRt3st12')
# log_page.login_button.click()
# browser.quit()

#Unsuccessfull Login
log_page = LoginPage(driver=browser)
log_page.go()
log_page.user_name_field.input_text('hr.doctor@hospitalrun.io')
log_page.password_field.input_text('wrong')
log_page.login_button.click()
assert log_page.error_message.text == "Username or password is incorrect.", 'The text is wrong'
# browser.quit()