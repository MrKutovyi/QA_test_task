from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://demo.hospitalrun.io')
driver.maximize_window()
driver.implicitly_wait(20)
name_field = driver.find_element_by_css_selector("input[id='identification']")
name_field.send_keys('hr.doctor@hospitalrun.io')

password_field = driver.find_element_by_css_selector("input[id='password']")
password_field.send_keys('000000')

sign_in_button = driver.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-block']")
sign_in_button.click()
time.sleep(3)

error_message = driver.find_element_by_xpath("//div[text()='Username or password is incorrect.']")
assert error_message.text == "Username or password is incorrect."

driver.quit()