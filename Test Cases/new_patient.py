from selenium import webdriver

from successful_login import *
from pages.base_element import BaseElement
from pages.med_page import LoginPage
from pages.patients_page import PatientsPage


# Test Setup
currentURL = None

# Test
patient_page = PatientsPage(driver=browser)
patient_page.go()
patient_page.new_patient_button.click()
