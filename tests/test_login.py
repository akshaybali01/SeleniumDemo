from pickletools import pyset

import allure
import pytest
from pathlib import Path
from pages.login_page import LoginPage
from utils.login_data_util import get_login_data

url = "https://www.saucedemo.com"
file_path = Path(__file__).parent.parent / "data/login_data.json"
valid_users = get_login_data(file_path, "valid")
invalid_users = get_login_data(file_path, "invalid")


@allure.title("Test:login test - valid user")
@allure.description("verify that user is able to login with valid users only")
@pytest.mark.parametrize("data", valid_users)
def test_valid_login(setup_driver, data):
    driver = setup_driver
    login_page = LoginPage(driver)

    user_name = data["username"]
    password = data["password"]
    result = login_page.do_login(url, user_name, password)
    assert result, f"Login failed, current url is {driver.current_url}"
    print("Page title is ", driver.title)


@allure.title("Test:login test-invalid user")
@allure.description("verify that user is not able to login with invalid users")
@pytest.mark.parametrize("data", invalid_users)
def test_invalid_login(setup_driver, data):
    driver = setup_driver
    login_page = LoginPage(driver)
    user_name = data["username"]
    password = data["password"]
    expected = data["expected"]
    result = login_page.do_invalid_login(url, user_name, password)
    assert result == expected, f"Login should fail with this user {user_name}"
