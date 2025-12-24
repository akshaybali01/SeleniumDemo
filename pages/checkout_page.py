from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.first_name_field=(By.NAME,"firstName")
        self.last_name_field=(By.ID,"last-name")
        self.zip_code_field=(By.ID,"postal-code")
        self.continue_buton = (By.ID,"continue")

    def click_checkout(self):
        self.driver.find_element(By.NAME,"checkout").click()

    def enter_checkout_details(self,firstname,lastname,zip):
        self.enter_text(self.first_name_field,firstname)
        self.enter_text(self.last_name_field, lastname)
        self.enter_text(self.zip_code_field, zip)
        self.click(self.continue_buton)
