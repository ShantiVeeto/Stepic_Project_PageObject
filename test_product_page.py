from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import time
import pytest
#import faker #для запуска нужна дополнительная библиотека faker

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.item_add_to_cart()
    #page.solve_quiz_and_get_code()
    page.should_be_message_add_to_cart()
    page.should_be_message_total_of_cart()
    time.sleep(2)
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        #f = faker.Faker() #для запуска нужна дополнительная библиотека faker
        #email = f.email() #для запуска нужна дополнительная библиотека faker
        email = str(time.time()) + "@fakemail.org"
        password = "Jj200276!"
        login_page.register_new_user(email, password)
        time.sleep(2)
        login_page.should_be_authorized_user()
        self.browser = browser

    def test_user_cant_see_success_message(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(self.browser, link)
        page.open()
        time.sleep(2)

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(self.browser, link)
        page.open()
        page.item_add_to_cart()
        time.sleep(2)
        #page.solve_quiz_and_get_code()
        page.should_be_message_add_to_cart()
        page.should_be_message_total_of_cart() 

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    time.sleep(2)
    cart_page.should_be_empty_cart()
    cart_page.should_be_message_empty_cart()