from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_element import BaseElement

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://demo.hospitalrun.io'

    def go(self):
        self.driver.get(self.url)

    def user_name_field(self):
        locator = (By.ID, 'identification')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    def password_field(self):
        locator = (By.ID, 'password')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    def login_button(self):
        locator = (By.CLASS_NAME, 'btn btn-lg btn-primary btn-block')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])