from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .login_page import LoginPage


class MedPage(BasePage):

    url = 'http://demo.hospitalrun.io/#/medication'

    @property
    def new_request_button(self):
        locator = (By.XPATH, '//div[1]/div[1]/div/button[1]')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def patient_field(self):
        locator = (By.ID, 'patientTypeAhead-ember2684')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def medication_field(self):
        locator = (By.ID, 'inventoryItemTypeAhead-ember2751')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def prescription_field(self):
        locator = (By.ID, 'prescription-ember2783')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def prescription_date(self):
        locator = (By.ID, 'display_prescriptionDate-ember3325')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def quantity_field(self):
        locator = (By.ID, 'quantity-ember2825')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def refils_field(self):
        locator = (By.ID, 'refills-ember3335')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def add_button(self):
        locator = (By.CLASS_NAME, 'btn btn-primary on-white disabled-btn')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def med_pop_up(self):
        locator = (By.CLASS_NAME, 'modal-content')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def pop_up_button(self):
        locator = (By.CLASS_NAME, 'btn btn-primary on-white')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def success_message(self):
        locator = (By.CLASS_NAME, 'modal-body')
        return BaseElement(self.driver, by=locator[0], value=locator[1])
