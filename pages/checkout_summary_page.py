import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutSummaryPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)

    def get_checkout_page_title(self):
        return self.driver.find_element(By.CLASS_NAME,"title").text

    def get_cart_items_on_summary_Page(self):
        items=[]
        cart_list = self.driver.find_element(By.CLASS_NAME,"cart_list")
        products = cart_list.find_elements(By.XPATH,".//div[@class='cart_item']")
        for product  in products:
            product_name = product.find_element(By.XPATH,".//div[@class='cart_item_label']/a").text
            items.append(product_name)
        return items

    def check_total_price(self):
        price = {}
        actual_price_shown = self.driver.find_element(By.CLASS_NAME,"summary_total_label").text
        actual_price_shown = float(actual_price_shown.split("$")[1])
        print("actual_price_shown",actual_price_shown)
        cart_list = self.driver.find_element(By.CLASS_NAME, "cart_list")
        products = cart_list.find_elements(By.XPATH, ".//div[@class='cart_item']")
        for product in products:
            product_name = product.find_element(By.XPATH, ".//div[@class='cart_item_label']/a").text
            price_shown = product.find_element(By.XPATH, ".//div[@class='cart_item_label']/div[2]/div").text
            print(price_shown)
            price.setdefault(product_name,price_shown[1:])
        print(price)
        total_item_price = 0
        for v in price.values():
            total_item_price=total_item_price+float(v)
        print(price)
        print("****")
        tax_amount = self.driver.find_element(By.CLASS_NAME,"summary_tax_label").text
        tax_amount = float(tax_amount.split("$")[1])
        print("taxx amount is ",tax_amount)
        print("total_item_price=",total_item_price)
        expected_total_amount = round((total_item_price+tax_amount),2)
        print("expected_total_amount",expected_total_amount)
        print("actual_price_shown",actual_price_shown)
        #print(expected_total_amount)
        return expected_total_amount==actual_price_shown

    def complete_the_purchase(self):
        self.driver.find_element(By.ID,"finish").click()

    def validate_purchase(self):
        return self.driver.find_element(By.XPATH,"//div[@id='checkout_complete_container']/h2").text

