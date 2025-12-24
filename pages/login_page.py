from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_text = (By.CSS_SELECTOR, ".error-message-container.error>h3")

    def do_login(self, url, username, password):
        self.driver.get(url)
        print(f"Login in with username: {username} ")
        # self.driver.find_element(*self.username_field).send_keys(username)
        # self.driver.find_element(*self.password_field).send_keys(password)
        # self.driver.find_element(*self.login_button).click()
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click(self.login_button)
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.url_contains("inventory.html"))
            return True
        except Exception as err:
            return False

    def do_invalid_login(self, url, username, password):
        self.driver.get(url)
        print(f"Login in with username: {username} ")
        # self.driver.find_element(*self.username_field).send_keys(username)
        # self.driver.find_element(*self.password_field).send_keys(password)
        # self.driver.find_element(*self.login_button).click()
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click(self.login_button)
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.visibility_of_element_located(self.error_text))
            assert "Sorry" in self.driver.find_element(*self.error_text).text, "Error message is not shown"
            return "fail"
        except Exception as err:
            return "pass"
