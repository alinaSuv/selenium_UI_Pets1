import time
import requests
from .locators import ProfilePageLocators, MainPageLocators
from .login_page import LoginPage


class ProfilePage(LoginPage):

    def open_pet_adding_form(self):
        self.browser.find_element(*ProfilePageLocators.PET_ADDING_BUTTON).click()

    def define_pet_name(self):
        pet_name = self.browser.find_element(*ProfilePageLocators.ADD_PET_NAME)
        pet_name.send_keys("Frutty")

    def define_pet_type(self):
        self.browser.find_element(*ProfilePageLocators.ADD_PET_TYPE).click()
        selection_pet_type = self.browser.find_element(*ProfilePageLocators.SELECT_PET_TYPE).click()

    def define_pet_age(self):
        pet_age = self.browser.find_element(*ProfilePageLocators.ADD_PET_AGE)
        pet_age.send_keys("7")

    def define_pet_gender(self):
        pet_gender = self.browser.find_element(*ProfilePageLocators.ADD_PET_GENDER).click()
        selection_pet_gender = self.browser.find_element(*ProfilePageLocators.SELECT_PET_GENDER).click()

    def perform_pet_submit(self):
        pet_submit = self.browser.find_element(*ProfilePageLocators.PET_SUBMIT_BUTTON).click()

    def open_profile_page(self):
        profile_page_link = self.browser.find_element(*ProfilePageLocators.PROFILE_PAGE_LINK1).click()
        open_profile_page = self.browser.find_element(*ProfilePageLocators.PROFILE_PAGE_LINK2).click()

    def open_main_page(self):
        main_page_link = self.browser.find_element(*ProfilePageLocators.MAIN_PAGE_LINK).click()

    def check_success_message(self):
        success_message = self.browser.find_element(*ProfilePageLocators.SUCCESS_MESSAGE)
        assert success_message

    def check_added_pet_in_profile(self):
        find_added_pet = self.browser.find_element(*ProfilePageLocators.ADDED_PET)
        assert find_added_pet

    def check_response_for_pet_adding(self):
        response = requests.post('http://34.141.58.52:8000/pets')
        status_code = response.status_code
        assert status_code == 200

    def edit_pet(self):
        pet_selection_for_editing = self.browser.find_element(*ProfilePageLocators.PET_EDIT_BUTTON).click()
        time.sleep(2)
        pet_age = self.browser.find_element(*ProfilePageLocators.ADD_PET_AGE).clear()
        pet_age = self.browser.find_element(*ProfilePageLocators.ADD_PET_AGE)
        pet_age.send_keys("8")
        pet_gender = self.browser.find_element(*ProfilePageLocators.ADD_PET_GENDER).click()
        selection_pet_gender = self.browser.find_element(*ProfilePageLocators.SELECT_PET_GENDER).click()
        time.sleep(2)
        pet_saving_changes = self.browser.find_element(*ProfilePageLocators.PET_PROFILE_SAVING).click()

    def delete_pet(self):
        pet_selection_for_removing = self.browser.find_element(*ProfilePageLocators.PET_DELETE_BUTTON).click()
        time.sleep(1)
        delete_confirmation = self.browser.find_element(*ProfilePageLocators.PET_DELETE_CONFIRM_BUTTON_YES).click()
        time.sleep(1)

    def filtering_by_pet_name2(self):
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        pet_name.clear()
        pet_name.send_keys("Frutty", "\n")

    def open_pet_details(self):
        pet_details = self.browser.find_element(*MainPageLocators.PET_DETAILS_BUTTON).click()
        time.sleep(2)

    def check_pet_picture_block(self):
        pet_picture_block = self.browser.find_element(*MainPageLocators.PET_PICTURE_IN_DETAILS)
        assert pet_picture_block

    def check_pet_details_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.PET_NAME_IN_DETAILS).text
        print(pet_name)
        assert (pet_name, "Frutty ")

    def check_pet_details_type(self):
        pet_type = self.browser.find_element(*MainPageLocators.PET_TYPE_IN_DETAILS).text
        print(pet_type)
        assert (pet_type == "reptile")

    def check_pet_details_owner(self):
        pet_owner = self.browser.find_element(*MainPageLocators.PET_OWNER_IN_DETAILS).text
        print(pet_owner)
        assert (pet_owner == "mankevichalina2+10@gmail.com")



