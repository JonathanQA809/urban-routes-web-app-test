from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Address fields
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CALL_TAXI_BTN = (By.XPATH, "//button[@class='button round']")
    SUPP_PLAN_BTN = (By.XPATH, "//div[text()='Supportive']")
    SUPP_TEXT_LOCATOR = (By.XPATH, "//div[text()='Supportive']")
    CLICK_PHONE_NUM_FIELD = (By.XPATH, "//div[@class='np-text']")
    ENTER_PHONE_NUM = (By.XPATH, "//input[@id='phone']")
    CLICK_NEXT_BTN = (By.XPATH, "//button[text()='Next']")
    CODE_LOCATOR = (By.ID, "code")
    CLICK_CONFIRM_BTN = (By.XPATH, "//button[text()='Confirm']")
    PHONE_NUMBER_LOCATOR = (By.XPATH, "//div[@class='np-text']")
    PAYMENT_METHOD_LOCATOR = (By.XPATH, "//div[@class='pp-value']")
    PLUS_BTN_LOCATOR = (By.XPATH, "//img[@class='pp-plus']")
    VALID_CARD_LOCATOR = (By.CSS_SELECTOR, "input#number.card-input[name='number']")
    VALID_CARD_CODE_LOCATOR = (By.CSS_SELECTOR, "input#code.card-input[name='code'][placeholder='12']")
    SIMULATE_CLICK_LOCATOR = (By.XPATH, "//div[contains(@class,'head') and normalize-space()='Adding a card']")
    LINK_LOCATOR = (By.XPATH, "//button[@type='submit' and contains(@class,'button') and contains(@class,'full') and normalize-space()='Link']")
    CLOSE_PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    CASH_TO_CARD_LOCATOR = (By.CSS_SELECTOR, "div.pp-value-text")
    COMMENT_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@id='comment' and @name='comment' and @type='text']")
    OPTION_SWITCHES_LOCATOR = (By.CLASS_NAME, 'switch')
    OPTION_SWITCHERS_INPUTS = (By.CLASS_NAME, 'switch-input')
    ICE_CREAM_ADD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAM_COUNT_LOCATOR = (By.CLASS_NAME, 'counter-value')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//button[@class="smart-button"]')
    CAR_SEARCH_MODAL_LOCATOR = (By.XPATH, '//div[text()="Car search"]')

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.wait_for_clickable(locator).click()

    def input_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def input_from_address(self, from_address):
        self.input_text(self.FROM_FIELD, from_address)

    def input_to_address(self, to_address):
        self.input_text(self.TO_FIELD, to_address)

    def get_from_address(self):
        return self.wait_for_visible(self.FROM_FIELD).get_attribute('value')

    def get_to_address(self):
        return self.wait_for_visible(self.TO_FIELD).get_attribute('value')

    def set_route(self, from_address, to_address):
        self.input_from_address(from_address)
        self.input_to_address(to_address)

    # Supportive Card
    def click_call_taxi(self):
        self.click_element(self.CALL_TAXI_BTN)

    def click_supportive_plan(self):
        self.click_element(self.SUPP_PLAN_BTN)

    def get_supportive_text(self):
        return self.wait_for_visible(self.SUPP_TEXT_LOCATOR).text

    #Filling in the Phone Number

    def click_enter_phone_number(self):
        self.click_element(self.CLICK_PHONE_NUM_FIELD)

    def enter_phone_number(self, phone_number):
        self.input_text(self.ENTER_PHONE_NUM, phone_number)

    def click_next_button(self):
        self.click_element(self.CLICK_NEXT_BTN)

    def input_sms_code(self, code):
        self.input_text(self.CODE_LOCATOR, code)

    def click_confirm_button(self):
        self.click_element(self.CLICK_CONFIRM_BTN)

    def get_phone_number(self):
        return self.wait_for_visible(self.PHONE_NUMBER_LOCATOR).text

    # Adding a Credit Card

    def click_payment_method(self):
        self.click_element(self.PAYMENT_METHOD_LOCATOR)

    def click_plus_button(self):
        self.click_element(self.PLUS_BTN_LOCATOR)

    def click_card_number_field(self):
        self.click_element(self.VALID_CARD_LOCATOR)

    def enter_card_number(self, card_number):
        self.input_text(self.VALID_CARD_LOCATOR, card_number)

    def click_card_code(self):
        self.click_element(self.VALID_CARD_CODE_LOCATOR)

    def enter_card_code(self, card_code):
        self.input_text(self.VALID_CARD_CODE_LOCATOR, card_code)

    def simulate_click(self):
        self.click_element(self.SIMULATE_CLICK_LOCATOR)

    def link_click(self):
        self.click_element(self.LINK_LOCATOR)

    def close_payment_method(self):
        self.click_element(self.CLOSE_PAYMENT_METHOD_LOCATOR)

    def get_card_text(self):
        return self.wait_for_visible(self.CASH_TO_CARD_LOCATOR).text


    # Writing a Comment for the Driver

    def enter_comment_input(self, comment_text):
        self.input_text(self.COMMENT_INPUT_FIELD_LOCATOR, comment_text)

    def get_driver_message(self):
        return self.wait_for_visible(self.COMMENT_INPUT_FIELD_LOCATOR).get_attribute('value')

    # Ordering a Blanket and Handkerchiefs

    def click_blanket_and_handkerchiefs_option(self):
        self.wait_for_visible(self.OPTION_SWITCHES_LOCATOR)
        switches = self.driver.find_elements(*self.OPTION_SWITCHES_LOCATOR)
        switches[0].click()

    def get_blanket_and_handkerchiefs_option_checked(self):
        self.wait_for_visible(self.OPTION_SWITCHERS_INPUTS)
        switches = self.driver.find_elements(*self.OPTION_SWITCHERS_INPUTS)
        return switches[0].get_property('checked')

    # Ordering 2 Ice Creams (Supportive Taxi)

    def click_order_ice_cream(self):
        self.click_element(self.ICE_CREAM_ADD_BUTTON_LOCATOR)

    def get_ice_cream_count(self):
        el = self.wait_for_visible(self.ICE_CREAM_COUNT_LOCATOR)
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


    # Locate and input an address into the "from" field.

    def order_button(self):
        self.click_element(self.ORDER_BUTTON_LOCATOR)

    def get_car_search_modal(self):
        return self.wait_for_visible(self.CAR_SEARCH_MODAL_LOCATOR).is_displayed()














