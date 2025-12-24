from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger_util import create_logger



class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.logger = create_logger(self.__class__.__name__)

    def click(self,locator):
        self.logger.info(f"Clicking on {locator}")
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,text):
        self.logger.info(f"Entering {text} in {locator}")
        self.driver.find_element(*locator).send_keys(text)
