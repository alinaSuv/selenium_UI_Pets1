import time
from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        select_login = self.browser.find_element(*MainPageLocators.LOGIN_SELECT)
        select_login.click()

    def filtering_by_pet_name(self, petName):
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        pet_name.clear()
        pet_name.send_keys(petName, "\n")

    def check_filtered_pet_by_name(self):
        filtered_pet_name = self.browser.find_element(*MainPageLocators.FILTERED_NAME)
        assert (filtered_pet_name, "Teddy")

    def clear_name_filter(self):
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        pet_name.clear()
        pet_name.send_keys(Keys.ENTER)
        time.sleep(2)

    def filtering_by_pet_category(self):
        category_dropdown = self.browser.find_element(*MainPageLocators.CATEGORY_DROPDOWN).click()
        time.sleep(1)
        pet_category = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_CATEGORY).click()

    def check_filtered_pet_by_category(self):
        filtered_pet_category = self.browser.find_element(*MainPageLocators.FILTERED_CATEGORY)
        assert ("parrot", filtered_pet_category)

    def combo_filtering_positive(self):
        category_dropdown = self.browser.find_element(*MainPageLocators.CATEGORY_DROPDOWN).click()
        time.sleep(1)
        pet_category = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_CATEGORY).click()
        time.sleep(1)
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        pet_name.clear()
        pet_name.send_keys("Kaka Du", "\n")

    def check_result_combo_filtering_positive(self):
        filtered_pet_category = self.browser.find_element(*MainPageLocators.FILTERED_CATEGORY)
        assert ("parrot", filtered_pet_category)
        filtered_pet_name = self.browser.find_element(*MainPageLocators.FILTERED_NAME)
        assert ("Kaka Du", filtered_pet_name)

    def check_result_combo_filtering_negative(self):
        no_filters_results = self.browser.find_element(*MainPageLocators.NO_RESULTS)
        assert ("No records found.", no_filters_results)

    def check_adding_like(self):
        initial_like_amount = self.browser.find_element(*MainPageLocators.LIKE_AMOUNT).text
        print("Like amount equals: ", initial_like_amount)
        assert initial_like_amount
        like_action = self.browser.find_element(*MainPageLocators.LIKE_ACTION).click()
        time.sleep(3)
        latest_like_amount = self.browser.find_element(*MainPageLocators.LIKE_AMOUNT).text
        print("Like amount equals: ", latest_like_amount)
        assert initial_like_amount == "1"

    def adding_comment(self):
        pet_details = self.browser.find_element(*MainPageLocators.PET_DETAILS_BUTTON).click()
        time.sleep(2)
        comment_field = self.browser.find_element(*MainPageLocators.COMMENT_FIELD)
        comment_field.send_keys('Test Comment', "\n")
        time.sleep(1)
        saving_comment = self.browser.find_element(*MainPageLocators.COMMENT_SAVE_BUTTON).click()

    def check_comment_adding(self):
        comments_block = self.browser.find_element(*MainPageLocators.COMMENTS_BLOCK)



