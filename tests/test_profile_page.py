import time
from pages.profile_page import ProfilePage

link = 'http://34.141.58.52:8080/#/login'
link2 = 'http://34.141.58.52:8080/#/'

def test_adding_pet_with_required_data(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()
    time.sleep(2)
    page.open_pet_adding_form()
    page.define_pet_name()
    page.define_pet_type()
    page.perform_pet_submit()
    time.sleep(1)
    page.open_profile_page()
    browser.save_screenshot("result10.png")
    page.check_success_message()
    page.check_added_pet_in_profile()

def test_editing_pet(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()
    time.sleep(2)
    page.edit_pet()
    time.sleep(1)
    browser.save_screenshot("result11.png")
    page.check_success_message()

def test_removing_pet(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()
    time.sleep(2)
    page.delete_pet()
    time.sleep(1)
    browser.save_screenshot("result12.png")
    page.check_success_message()


def test_adding_pet_with_all_data(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_login()
    page.define_password()
    page.apply_submit()
    time.sleep(2)
    page.open_pet_adding_form()
    page.define_pet_name()
    page.define_pet_type()
    page.define_pet_age()
    page.define_pet_gender()
    page.perform_pet_submit()
    time.sleep(1)
    page.open_main_page()
    time.sleep(2)
    page.filtering_by_pet_name2()
    time.sleep(1)
    page.open_pet_details()
    page.check_pet_picture_block()
    page.check_pet_details_name()
    page.check_pet_details_type()
    page.check_pet_details_owner()

















