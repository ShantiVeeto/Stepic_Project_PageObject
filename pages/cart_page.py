from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS_IN_CART), "Cart is not empty, but should be"

    def should_be_not_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.ITEMS_IN_CART), "Cart is empty, but should not be"
        
    def should_be_message_empty_cart(self):
        cart_message = self.browser.find_element(*CartPageLocators.MESSAGE_CART_IS_EMPTY).text
        assert "Your basket is empty" in cart_message, "Message 'cart is empty' is not presented, but should be"
        
    def should_not_be_message_empty_cart(self):
        cart_message = self.browser.find_element(*CartPageLocators.MESSAGE_CART_IS_EMPTY).text
        assert "Your basket is empty" in cart_message, "Message 'cart is empty' is presented, but should not be"