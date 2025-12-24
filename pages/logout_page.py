from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.hamburger_menu = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.home_url = "https://www.saucedemo.com/"

    def do_logout(self):
        self.wait.until(EC.visibility_of_element_located(self.hamburger_menu))
        self.click(self.hamburger_menu)
        self.wait.until(EC.visibility_of_element_located(self.logout_link))
        self.click(self.logout_link)
        self.logger.info(f"expected url: {self.home_url}")
        self.logger.info(f"Actual url after logout: {self.driver.current_url}")
        return self.driver.current_url == self.home_url
