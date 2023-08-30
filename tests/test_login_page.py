from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_execute_valid_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located(LoginPageLocators.SUCCESS_LOGIN_SIGN))
    browser.save_screenshot("result7.png")

def test_execute_login_with_invalid_email(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_with_invalid_email()
    page.define_password()
    page.apply_submit()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located(LoginPageLocators.INVALID_EMAIL_LOGIN_WARNING))
    page.check_response_for_login_with_invalid_email()
    page.check_warning_for_login_with_invalid_email()
    browser.save_screenshot("result8.png")

def test_execute_login_with_invalid_password(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.define_invalid_password()
    page.apply_submit()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located(LoginPageLocators.INVALID_EMAIL_LOGIN_WARNING))
    page.check_response_for_login_with_invalid_password()
    page.check_warning_for_login_with_invalid_email()
    browser.save_screenshot("result9.png")