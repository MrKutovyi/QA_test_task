from selenium import webdriver

from successful_login import *
from new_patient import *
from pages.base_element import BaseElement
from pages.med_page import LoginPage
from pages.med_page import MedPage
from selenium.webdriver.common.keys import Keys

# Test Setup
currentURL = None

# Test
# med_page = MedPage(driver=browser)
# med_page.go()
# med_page.new_request_button.click()
# med_page.patient_field.input_text('Alex Test')
# med_page.medication_field.input_text('h')
# med_page.medication_field.input_text('y')
# med_page.medication_field.input_text('d')
# med_page.medication_field.click()
# med_page.medication_field.input_text(Keys.ARROW_DOWN)
# med_page.medication_field.input_text(Keys.ARROW_DOWN)
# med_page.prescription_field.input_text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
#                                        'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ')
# med_page.prescription_date.click()
# med_page.prescription_date.input_text(Keys.ARROW_UP)
# med_page.prescription_date.input_text(Keys.ARROW_UP)
# med_page.prescription_date.input_text(Keys.ENTER)


