import time

from pages.login_page import LoginPage
from pages.main_page import MainPage

link = 'http://34.141.58.52:8080/#/'
linkLoginPage = 'http://34.141.58.52:8080/#/login'


def test_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result6.png')

def test_filter_by_name(browser):
    page = MainPage(browser, link)
    page.open()
    page.filtering_by_pet_name(petName="Teddy")
    time.sleep(1)
    page.check_filtered_pet_by_name()
    browser.save_screenshot('result13.png')
    page.clear_name_filter()

def test_filter_by_category(browser):
    page = MainPage(browser, link)
    page.open()
    page.filtering_by_pet_category()
    time.sleep(2)
    page.check_filtered_pet_by_category()
    browser.save_screenshot('result14.png')

def test_combo_filtering_positive_case(browser):
    page = MainPage(browser, link)
    page.open()
    page.combo_filtering_positive()
    page.check_result_combo_filtering_positive()
    browser.save_screenshot('result15.png')

def test_combo_filtering_negative_case(browser):
    page = MainPage(browser, link)
    page.open()
    page.filtering_by_pet_category()
    page.filtering_by_pet_name(petName="Teddy")
    page.check_result_combo_filtering_negative()
    browser.save_screenshot('result16.png')

def test_add_like(browser):
    page = LoginPage(browser, linkLoginPage)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()
    time.sleep(2)
    page.open_main_page()
    page = MainPage(browser, url='http://34.141.58.52:8080/#/')
    page.filtering_by_pet_name(petName="Bela")
    time.sleep(2)
    page.check_adding_like()
    time.sleep(3)

def test_add_comment(browser):
    page = LoginPage(browser, linkLoginPage)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()
    time.sleep(2)
    page.open_main_page()
    page = MainPage(browser, url='http://34.141.58.52:8080/#/')
    page.filtering_by_pet_name(petName="Bela")
    time.sleep(1)
    page.adding_comment()
    time.sleep(1)
    browser.save_screenshot('result17.png')








