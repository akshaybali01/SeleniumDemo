from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def click(self,locator):
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)
