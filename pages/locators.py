from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > a')
    LOGIN_SELECT = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_PET_NAME = (By.ID, "petName")
    FILTERED_NAME = (By.CLASS_NAME, "product-name")
    FILTER_BY_PET_CATEGORY = (By.XPATH, "//li[5]")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, ".p-dropdown-trigger-icon")
    FILTERED_CATEGORY = (By.CLASS_NAME, "product-category")
    NO_RESULTS = (By.CLASS_NAME, "p-dataview-emptymessage")
    PET_DETAILS_BUTTON = (By.CSS_SELECTOR, ".p-button-label")
    PET_PICTURE_IN_DETAILS = (By.XPATH, "//div/div/div/div")
    PET_NAME_IN_DETAILS = (By.XPATH, '//span/span[2]')
    PET_TYPE_IN_DETAILS = (By.XPATH, "//li[2]/a/span/span[2]")
    PET_OWNER_IN_DETAILS = (By.XPATH, '//li[4]/a/span/span[2]')
    LIKE_AMOUNT = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/span[2]')
    LIKE_ACTION = (By.XPATH, "//div[5]/div/div[3]/div[2]/span/i")
    COMMENT_FIELD = (By.XPATH, "//form/div/div/div[2]/div")
    COMMENT_SAVE_BUTTON = (By.XPATH, "//div/button")





class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_SUBMIT_BUTTON = (By.CLASS_NAME, "p-button-label")
    SUCCESS_LOGIN_SIGN = (By.CSS_SELECTOR, ".pi-plus")
    INVALID_EMAIL_LOGIN_WARNING = (By.XPATH, '//*[@id="pv_id_2_content"]/div/div')

class ProfilePageLocators:
    PROFILE_PAGE_LINK1 = (By.XPATH, "//i")
    PROFILE_PAGE_LINK2 = (By.XPATH, '//span[2]')
    MAIN_PAGE_LINK = (By.XPATH, '//*[@id="app"]/header/div/div')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".p-toast-message-text")
    PET_ADDING_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button/span[1]')
    ADD_PET_NAME = (By.ID, "name")
    ADD_PET_TYPE = (By.ID, "typeSelector")
    SELECT_PET_TYPE = (By.XPATH, "//li[3]")
    ADD_PET_AGE = (By.XPATH, "//span[@id='age']/input")
    ADD_PET_GENDER = (By.ID, "genderSelector")
    SELECT_PET_GENDER = (By.XPATH, "//div[3]/div/ul/li")
    PET_SUBMIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    PET_EDIT_BUTTON = (By.XPATH, "//div[5]/div/div[2]/button/span[2]")
    PET_DELETE_BUTTON = (By.XPATH, "//div[3]/div/div[2]/button[2]/span[2]")
    PET_DELETE_CONFIRM_BUTTON_YES = (By.XPATH, "/html/body/div[3]/div[2]/button[2]")
    PET_PROFILE_SAVING = (By.XPATH, "//span[contains(.,'Save')]")
    ADDED_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[5]')

