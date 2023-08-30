import requests

from .base_page import BasePage
from .locators import LoginPageLocators, ProfilePageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('mankevichalina2+10@gmail.com')

    def go_to_login_with_invalid_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('mankevichalinaIn@gmail.com')

    def define_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys('tester1')

    def define_invalid_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys('tester')

    def apply_submit(self):
        login_submit = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        login_submit.submit()

    def check_response_for_login_with_invalid_email(self):
        response = requests.post('http://34.141.58.52:8080/#/login')
        status_code = response.status_code
        assert status_code == 405

    def check_warning_for_login_with_invalid_email(self):
        error_with_invalid_email_login = self.browser.find_element(*LoginPageLocators.INVALID_EMAIL_LOGIN_WARNING)
        assert error_with_invalid_email_login

    def check_response_for_login_with_invalid_password(self):
        response = requests.post('http://34.141.58.52:8080/#/login')
        status_code = response.status_code
        assert status_code == 405
        
    def open_main_page(self):
        main_page_link = self.browser.find_element(*ProfilePageLocators.MAIN_PAGE_LINK).click()







