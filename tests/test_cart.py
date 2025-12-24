import allure

from pages.cart_page import CartPage
from pages.login_page import LoginPage
import time

url = "https://www.saucedemo.com"
productnames = ["Sauce Labs Fleece Jacket", "Sauce Labs Bike Light"]


@allure.title("Test:Add items to cart")
@allure.description("Adding items to cart")
def test_add_items_to_cart(logged_in_driver):
    driver, login_success = logged_in_driver
    assert login_success, "Login failed — stopping test execution"
    cart_page = CartPage(driver)
    cart_page.add_products_to_cart(productnames)
    assert len(productnames) == cart_page.get_cart_badge_count(), "Item count mismatch"
    cart_page.open_cart()
