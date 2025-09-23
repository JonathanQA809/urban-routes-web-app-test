import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from pages import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        assert routes_page.get_from_address() == data.ADDRESS_FROM
        assert routes_page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        time.sleep(3)
        routes_page.click_call_taxi()
        time.sleep(3)
        routes_page.click_supportive_plan()
        time.sleep(3)
        actual_value = routes_page.get_supportive_text()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        time.sleep(3)
        routes_page.click_call_taxi()
        time.sleep(3)
        routes_page.click_supportive_plan()
        time.sleep(3)
        routes_page.click_enter_phone_number()
        time.sleep(3)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(3)
        routes_page.click_next_button()
        # Get the SMS code
        sms_code = helpers.retrieve_phone_code(self.driver)
        routes_page.input_sms_code(str(sms_code))
        time.sleep(3)
        routes_page.click_confirm_button()
        time.sleep(3)
        actual_value = routes_page.get_phone_number()
        expected_value = "+1 123 123 12 12"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        time.sleep(2)
        routes_page.click_call_taxi()
        time.sleep(2)
        routes_page.click_payment_method()
        time.sleep(2)
        routes_page.click_plus_button()
        time.sleep(2)
        routes_page.click_card_number_field()
        time.sleep(2)
        routes_page.enter_card_number(data.CARD_NUMBER)
        time.sleep(2)
        routes_page.click_card_code()
        time.sleep(2)
        routes_page.enter_card_code(data.CARD_CODE)
        time.sleep(2)
        routes_page.simulate_click()
        time.sleep(2)
        routes_page.link_click()
        time.sleep(2)
        routes_page.close_payment_method()
        time.sleep(2)
        actual_value = routes_page.get_card_text()
        expected_value = "Card"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        time.sleep(2)
        routes_page.click_call_taxi()
        time.sleep(2)
        routes_page.enter_comment_input(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        assert routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        time.sleep(2)
        routes_page.click_call_taxi()
        time.sleep(2)
        routes_page.click_supportive_plan()
        time.sleep(2)
        routes_page.click_blanket_and_handkerchiefs_option()
        time.sleep(2)
        assert routes_page.get_blanket_and_handkerchiefs_option_checked() is True
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        time.sleep(2)
        routes_page.click_call_taxi()
        time.sleep(2)
        routes_page.click_supportive_plan()
        time.sleep(2)
        routes_page.order_ice_cream_twice()
        count = routes_page.get_ice_cream_count()
        assert count == 2, f"Expected 2, got {count}"

        print("function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model appears")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

