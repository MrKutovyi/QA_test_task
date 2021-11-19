from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage


class LoginPage(BasePage):

    url = 'http://demo.hospitalrun.io'\

    @property
    def user_name_field(self):
        locator = (By.ID, 'identification')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def password_field(self):
        locator = (By.ID, 'password')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def login_button(self):
        locator = (By.XPATH, '/html/body/div/div/form/div[2]/button')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def error_message(self):
        locator = (By.XPATH, "//div[@class='alert alert-danger form-signin-alert']")
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])



