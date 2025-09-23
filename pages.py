import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # Address fields
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')

    def input_from_address(self, from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)

    def input_to_address(self, to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute('value')

    def get_to_address(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute('value')

    # Supportive Card
    CALL_TAXI_BTN = (By.XPATH, "//button[@class='button round']")
    SUPP_PLAN_BTN = (By.XPATH, "//div[text()='Supportive']")
    SUPP_TEXT_LOCATOR = (By.XPATH, "//div[text()='Supportive']")

    def click_call_taxi(self):
        self.driver.find_element(*self.CALL_TAXI_BTN).click()

    def click_supportive_plan(self):
        self.driver.find_element(*self.SUPP_PLAN_BTN).click()

    def get_supportive_text(self):
        # Return the "Supportive" text
        return self.driver.find_element(*self.SUPP_TEXT_LOCATOR).text

    #Filling in the Phone Number
    CLICK_PHONE_NUM_FIELD = (By.XPATH, "//div[@class='np-text']")
    ENTER_PHONE_NUM = (By.XPATH, "//input[@id='phone']")
    CLICK_NEXT_BTN = (By.XPATH, "//button[text()='Next']")
    CODE_LOCATOR = (By. ID, "code")
    CLICK_CONFIRM_BTN = (By.XPATH, "//button[text()='Confirm']")
    PHONE_NUMBER_LOCATOR = (By.XPATH, "//div[@class='np-text']")

    def click_enter_phone_number(self):
        self.driver.find_element(*self.CLICK_PHONE_NUM_FIELD).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.ENTER_PHONE_NUM).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.CLICK_NEXT_BTN).click()

    def input_sms_code(self, code):
        self.driver.find_element(*self.CODE_LOCATOR).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CLICK_CONFIRM_BTN).click()

    def get_phone_number(self):
        # Return the "phone num" text
        return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).text

    # Adding a Credit Card
    PAYMENT_METHOD_LOCATOR = (By.XPATH, "//div[@class='pp-value']")
    PLUS_BTN_LOCATOR = (By.XPATH, "//img[@class='pp-plus']")
    VALID_CARD_LOCATOR = (By.CSS_SELECTOR, "input#number.card-input[name='number']")
    VALID_CARD_CODE_LOCATOR = (By.CSS_SELECTOR, "input#code.card-input[name='code'][placeholder='12']")
    SIMULATE_CLICK_LOCATOR = (By.XPATH, "//div[contains(@class,'head') and normalize-space()='Adding a card']")
    LINK_LOCATOR = (By. XPATH, "//button[@type='submit' and contains(@class,'button') and contains(@class,'full') and normalize-space()='Link']")
    CLOSE_PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    CASH_TO_CARD_LOCATOR = (By.CSS_SELECTOR, "div.pp-value-text")


    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def click_plus_button(self):
        self.driver.find_element(*self.PLUS_BTN_LOCATOR).click()

    def click_card_number_field(self):
        self.driver.find_element(*self.VALID_CARD_LOCATOR).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.VALID_CARD_LOCATOR).send_keys(card_number)

    def click_card_code(self):
        self.driver.find_element(*self.VALID_CARD_CODE_LOCATOR).click()

    def enter_card_code(self, card_code):
        self.driver.find_element(*self.VALID_CARD_CODE_LOCATOR).send_keys(card_code)

    def simulate_click(self):
        self.driver.find_element(*self.SIMULATE_CLICK_LOCATOR).click()

    def link_click(self):
        self.driver.find_element(*self.LINK_LOCATOR).click()

    def close_payment_method(self):
        self.driver.find_element(*self.CLOSE_PAYMENT_METHOD_LOCATOR).click()

    def get_card_text(self):
        # Return the "card text" checked
        return self.driver.find_element(*self.CASH_TO_CARD_LOCATOR).text


    # Writing a Comment for the Driver
    COMMENT_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@id='comment' and @name='comment' and @type='text']")

    def enter_comment_input(self, comment_text):
        self.driver.find_element(*self.COMMENT_INPUT_FIELD_LOCATOR).send_keys(comment_text)

    def get_driver_message(self):
        # Return the "driver message" text
        return self.driver.find_element(*self.COMMENT_INPUT_FIELD_LOCATOR).get_attribute('value')

    # Ordering a Blanket and Handkerchiefs
    OPTION_SWITCHES_LOCATOR = (By.CLASS_NAME, 'switch')
    OPTION_SWITCHERS_INPUTS = (By.CLASS_NAME, 'switch-input')

    def click_blanket_and_handkerchiefs_option(self):
        switches = self.driver.find_elements(*self.OPTION_SWITCHES_LOCATOR)
        switches[0].click()
        self.get_blanket_and_handkerchiefs_option_checked()

    def get_blanket_and_handkerchiefs_option_checked(self):
        switches = self.driver.find_elements(*self.OPTION_SWITCHERS_INPUTS)
        return switches[0].get_property('checked')

    # Ordering 2 Ice Creams (Supportive Taxi)
    ICE_CREAM_LABEL_LOCATOR = (By.XPATH, '//div[contains(text(), "Ice cream")]')
    ICE_CREAM_ADD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAM_COUNT_LOCATOR = (By.CLASS_NAME, 'counter-value')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//span[contains(text(), "Enter the number and order")]')

    def click_order_ice_cream(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ICE_CREAM_ADD_BUTTON_LOCATOR)
        ).click()

    def get_ice_cream_count(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ICE_CREAM_COUNT_LOCATOR)
        )
        text = (el.text or "").strip()
        try:
            return int(text)
        except ValueError:
            digits = ""
            for ch in text:
                if ch.isdigit():
                    digits += ch
            return int(digits) if digits else 0


    def order_ice_cream_twice(self):
        for _ in range(2):
            self.click_order_ice_cream()











