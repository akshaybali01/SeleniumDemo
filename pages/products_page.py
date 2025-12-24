from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Verify "Products" page title is displayed
    def get_product_page_title(self):
        product_element = self.driver.find_element(By.XPATH, "//span[@class='title']")
        return product_element.text

    # Verify all products are displayed
    def get_all_product_names(self):
        all_products = []
        product_box = self.driver.find_element(By.CLASS_NAME, "inventory_list")
        products = product_box.find_elements(By.XPATH, ".//div[@class='inventory_item']")
        for product in products:
            product_name = product.find_element(By.XPATH, ".//div[@class='inventory_item_description']/div/a")
            all_products.append(product_name.text)

        return all_products

    def get_product_price_map(self):
        item_price = {}

        product_box = self.driver.find_element(By.CLASS_NAME, "inventory_list")
        products = product_box.find_elements(By.XPATH, ".//div[@class='inventory_item']")
        for product in products:
            product_name = product.find_element(By.XPATH, ".//div[@class='inventory_item_description']/div/a")
            # items.append(product_name.text)
            product_price = product.find_element(By.XPATH, ".//div[@class='inventory_item_description']/div[2]/div")
            # print(product_price.text)
            item_price.setdefault(product_name.text, product_price.text)
            # price.append(product_price.text)

        return item_price


