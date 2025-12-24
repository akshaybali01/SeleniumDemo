import allure

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

url = "https://www.saucedemo.com"


@allure.title("Test:Verify product list")
@allure.description("Verify that product list is shown after login")
def test_products(logged_in_driver):
    driver, login_success = logged_in_driver
    assert login_success, "Login failed, Stoping the test execution"
    product_page = ProductsPage(driver)
    title = product_page.get_product_page_title()
    assert "Products" in title, "Products title is missing"
    all_products = product_page.get_all_product_names()
    # print(all_products)
    price = product_page.get_product_price_map()
    # print(price)

    for k, v in price.items():
        print(k, v)
