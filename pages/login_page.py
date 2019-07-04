from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "Word login in url is not presented"
        #assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        #assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        #assert True
    
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_USER_ID)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_USER_PASSWORD)
        input_password.send_keys(password)
        input_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_USER_PASSWORD_CONFIRM)
        input_password_confirm.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON_SUBMIT)
        button_submit.click()