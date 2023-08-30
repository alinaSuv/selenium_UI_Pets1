import pytest
from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture()
def execute_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()

