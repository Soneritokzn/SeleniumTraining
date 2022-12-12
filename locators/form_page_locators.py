from selenium.webdriver.common.by import By
from random import randint
class FormPageLocators():
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-1-{randint(1, 3)}"]')
    MOBILE = (By.CSS_SELECTOR, "#userNumber")
    SUBLECT = (By.CSS_SELECTOR, "#firstName")
    HOBBIES = (By.CSS_SELECTOR, "#firstName")
    FILE_INPUT = (By.CSS_SELECTOR, "#firstName")
    CURRENT_ADDRES = (By.CSS_SELECTOR, "#firstName")
    SUBMIT = (By.CSS_SELECTOR, "#firstName")

    RESULT_TABLE