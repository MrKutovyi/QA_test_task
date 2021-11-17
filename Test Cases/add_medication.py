from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('http://demo.hospitalrun.io')
driver.maximize_window()
driver.implicitly_wait(20)
name_field = driver.find_element_by_css_selector("input[id='identification']")
name_field.send_keys('hr.doctor@hospitalrun.io')

password_field = driver.find_element_by_css_selector("input[id='password']")
password_field.send_keys('HRt3st12')

sign_in_button = driver.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-block']")
sign_in_button.click()

med_menu = driver.find_element_by_css_selector("span[class='mega-octicon octicon-file-text']")
#ActionChains(driver).move_to_element(med_menu).click().perform()
med_menu.click()

new_request = driver.find_element_by_xpath("//*[@id='ember1630']")
ActionChains(driver).move_to_element(new_request).context_click().perform()
# new_request.click()
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('http://demo.hospitalrun.io')
driver.maximize_window()
driver.implicitly_wait(20)
name_field = driver.find_element_by_css_selector("input[id='identification']")
name_field.send_keys('hr.doctor@hospitalrun.io')

password_field = driver.find_element_by_css_selector("input[id='password']")
password_field.send_keys('HRt3st12')

sign_in_button = driver.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-block']")
sign_in_button.click()

med_menu = driver.find_element_by_css_selector("span[class='mega-octicon octicon-file-text']")
#ActionChains(driver).move_to_element(med_menu).click().perform()
med_menu.click()

new_request = driver.find_element_by_xpath("//*[@id='ember1630']")
ActionChains(driver).move_to_element(new_request).context_click().perform()
# new_request.click()