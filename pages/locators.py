from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_CART = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_USER_ID = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_USER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_USER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators(object):
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_ADD_TO_CART = (By.XPATH, ".//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_TOTAL_SUM = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.XPATH, ".//*[@id='messages']/div[1]/div")

class CartPageLocators(object):
    MESSAGE_CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_IN_CART = (By.CLASS_NAME, "basket-items")