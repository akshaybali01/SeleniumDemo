import allure

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_summary_page import CheckoutSummaryPage
from pages.login_page import LoginPage
import time

url = "https://www.saucedemo.com"


@allure.title("Test:Checkout")
@allure.description("Checkout and verify purchase")
def test_final_checkout(logged_in_driver):
    driver, login_success = logged_in_driver
    assert login_success, "Login failed, Stoping the test execution"
    cart_page = CartPage(driver)
    productnames = ["Sauce Labs Fleece Jacket", "Sauce Labs Bike Light"]
    cart_page.add_products_to_cart(productnames)
    assert len(productnames) == cart_page.get_cart_badge_count(), "Item count mismatch"
    cart_page.open_cart()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_checkout_details("akshay", "kumar", "41125")

    final_checkout_page = CheckoutSummaryPage(driver)
    checkoutpage_title = final_checkout_page.get_checkout_page_title()
    print("checkoutpage_title:", checkoutpage_title)
    item_list_shown = final_checkout_page.get_cart_items_on_summary_Page()
    print("items are:", item_list_shown)
    assert final_checkout_page.check_total_price(), "price is not matching"
    final_checkout_page.complete_the_purchase()
    assert "Thank you " in final_checkout_page.validate_purchase(), f"Thank you note not shown , actual={final_checkout_page.validate_purchase}"
