import time

import allure
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pathlib import Path

from utils.json_util import read_json

url = "https://www.saucedemo.com"
user_data = [{"firstname": "Demo123", "lastname": "seldemo", "zip": 123123}]


@pytest.fixture(params=user_data)
def get_user_testdata(request):
    return request.param


@allure.title("Test: Enter details on checkout page")
def test_checkout(logged_in_driver, get_user_testdata):
    first_name = get_user_testdata["firstname"]
    last_name = get_user_testdata["lastname"]
    zip = get_user_testdata["zip"]
    driver, login_success = logged_in_driver
    assert login_success, "Login failed , stoping the test execution"
    cart_page = CartPage(driver)
    productnames = ["Sauce Labs Fleece Jacket", "Sauce Labs Bike Light"]
    cart_page.add_products_to_cart(productnames)
    cart_page.open_cart()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_checkout_details(first_name, last_name, zip)
