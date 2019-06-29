from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

""" class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") """

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    BUTTON_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_ADD_TO_CART = (By.XPATH, ".//*[@id='messages']/div[1]/div/strong")
    #PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, ".alert-success .alertinner strong") - не уникален
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_TOTAL_SUM = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.XPATH, ".//*[@id='messages']/div[1]/div")