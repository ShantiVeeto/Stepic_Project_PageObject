#from selenium.webdriver.common.by import By
import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import time

class ProductPage(BasePage):
    def item_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_CART), "Button add to cart is not presented"
        button_cart = self.browser.find_element(*ProductPageLocators.BUTTON_CART)
        button_cart.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        """#включение второго алерта 
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
            return True
        except NoAlertPresentException:
            print("No second alert presented")
            return False """
    
    def should_be_message_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_CART), "Message product add to cart is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_add_to_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART).text
        assert product_name == product_add_to_cart, "Mismatch product name added to cart"

    def should_be_message_total_of_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART_TOTAL_SUM), "Message cart total sum is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        cart_total_sum = self.browser.find_element(*ProductPageLocators.CART_TOTAL_SUM).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == cart_total_sum, "Mismatch product price and cart total"