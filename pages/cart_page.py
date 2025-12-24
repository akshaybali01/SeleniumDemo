from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_products_to_cart(self, items):
        product_box = self.driver.find_element(By.CLASS_NAME, "inventory_list")
        products = product_box.find_elements(By.XPATH, ".//div[@class='inventory_item']")
        for product in products:
            product_name = product.find_element(By.XPATH, ".//div[@class='inventory_item_description']/div/a").text

            if product_name in items:
                add_to_cart_button = product.find_element(By.XPATH,
                                                          ".//div[@class='inventory_item_description']/div[2]/button")

                add_to_cart_button.click()

    def get_cart_badge_count(self):
        return int(self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text)

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()