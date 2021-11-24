from selenium import webdriver

from successful_login import *
from new_patient import *
from pages.base_element import BaseElement
from pages.med_page import LoginPage
from pages.med_page import MedPage


# Test Setup
currentURL = None

# Test
med_page = MedPage(driver=browser)
med_page.go()
med_page.new_request_button.click()
