import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    CALL_A_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")

    SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(text(), 'Supportive')]")

    PHONE_INPUT = (By.ID, "phone")
    CODE_INPUT = (By.ID, "code")

    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.ID, "code")

    COMMENT_INPUT = (By.ID, "comment")
    DRIVER_INFO = (By.CLASS_NAME, "driver-info")

    BLANKET_CHECKBOX = (By.ID, "blanket")
    HANDKERCHIEFS_CHECKBOX = (By.ID, "napkins")
    ICE_CREAM_BUTTON = (By.ID, "ice-cream")

    CAR_SEARCH_MODEL = (By.CLASS_NAME, "car-search")


    def __init__(self, driver):
        self.driver = driver

    def set_route(self, address_from, address_to):
        self.driver.find_element(*self.FROM_INPUT).send_keys(address_from)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.TO_INPUT))
        self.driver.find_element(*self.TO_INPUT).send_keys(address_to)
        self.click_call_taxi_button()

    def get_from(self):
        return self.driver.find_element(*self.FROM_INPUT).get_attribute('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_INPUT).get_attribute('value')

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.CALL_A_TAXI_BUTTON))
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN).click()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN).text


    def fill_phone_number(self, phone):
        phone_input = self.driver.find_element(*self.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(phone)

    def fill_verification_code(self, code):
        code_input = self.driver.find_element(*self.CODE_INPUT)
        code_input.clear()
        code_input.send_keys(code)

    def is_phone_verified(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "verified-phone")
            return True
        except:
            return False

    def fill_card_details(self, card_number, card_code):
        number_input = self.driver.find_element(*self.CARD_NUMBER_INPUT)
        number_input.clear()
        number_input.send_keys(card_number)

        code_input = self.driver.find_element(*self.CARD_CODE_INPUT)
        code_input.clear()
        code_input.send_keys(card_code)

    def is_card_valid(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "card-valid")
            return True
        except:
            return False

    def get_card_error_message(self):
        try:
            error_message = self.driver.find_element(By.CLASS_NAME, "card-error")
            return error_message.text
        except:
            return None

    def toggle_blanket(self):
        blanket_checkbox = self.driver.find_element(*UrbanRoutesLocators.BLANKET_CHECKBOX)
        blanket_checkbox.click()

    def toggle_handkerchiefs(self):
        handkerchiefs_checkbox = self.driver.find_element(*UrbanRoutesLocators.HANDKERCHIEFS_CHECKBOX)
        handkerchiefs_checkbox.click()

    def add_ice_cream(self, quantity=1):
        ice_cream_button = self.driver.find_element(*UrbanRoutesLocators.ICE_CREAM_BUTTON)
        for _ in range(quantity):
            ice_cream_button.click()

    def is_blanket_selected(self):
        blanket_checkbox = self.driver.find_element(*UrbanRoutesLocators.BLANKET_CHECKBOX)
        return blanket_checkbox.is_selected()

    def is_handkerchiefs_selected(self):
        handkerchiefs_checkbox = self.driver.find_element(*UrbanRoutesLocators.HANDKERCHIEFS_CHECKBOX)
        return handkerchiefs_checkbox.is_selected()

    def get_ice_cream_count(self):
        try:
            ice_cream_counter = self.driver.find_element(By.CLASS_NAME, "ice-cream-counter")
            return int(ice_cream_counter.text)
        except:
            return 0
