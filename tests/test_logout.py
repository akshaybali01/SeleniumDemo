from pages.logout_page import LogoutPage
from utils.logger_util import create_logger
from pathlib import Path


def test_logout(logged_in_driver):
    driver, login_success = logged_in_driver
    assert login_success, "Login failed, Stoping the test execution"
    logout_page = LogoutPage(driver)
    logout_page.do_logout()
