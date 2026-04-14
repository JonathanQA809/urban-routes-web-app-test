from selenium import webdriver
from pages import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    def open_routes_page(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        return UrbanRoutesPage(self.driver)

    def open_route_order_form(self):
        routes_page = self.open_routes_page()
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi()
        return routes_page

    def open_supportive_order_form(self):
        routes_page = self.open_route_order_form()
        routes_page.click_supportive_plan()
        return routes_page

    def test_set_route(self):
        routes_page = self.open_routes_page()
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert routes_page.get_from_address() == data.ADDRESS_FROM
        assert routes_page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        routes_page = self.open_supportive_order_form()

        assert routes_page.get_supportive_text() == "Supportive"



    def test_fill_phone_number(self):
        routes_page = self.open_supportive_order_form()
        routes_page.click_enter_phone_number()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next_button()

        sms_code = helpers.retrieve_phone_code(self.driver)
        routes_page.input_sms_code(str(sms_code))
        routes_page.click_confirm_button()

        assert routes_page.get_phone_number() == data.PHONE_NUMBER


    def test_fill_card(self):
        routes_page = self.open_route_order_form()
        routes_page.click_payment_method()
        routes_page.click_plus_button()
        routes_page.click_card_number_field()
        routes_page.enter_card_number(data.CARD_NUMBER)
        routes_page.click_card_code()
        routes_page.enter_card_code(data.CARD_CODE)
        routes_page.simulate_click()
        routes_page.link_click()
        routes_page.close_payment_method()

        assert routes_page.get_card_text() == "Card"

    def test_comment_for_driver(self):
        routes_page = self.open_route_order_form()
        routes_page.enter_comment_input(data.MESSAGE_FOR_DRIVER)

        assert routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = self.open_supportive_order_form()
        routes_page.click_blanket_and_handkerchiefs_option()

        assert routes_page.get_blanket_and_handkerchiefs_option_checked()


    def test_order_2_ice_creams(self):
        routes_page = self.open_supportive_order_form()
        routes_page.order_ice_cream_twice()

        count = routes_page.get_ice_cream_count()
        assert count == 2, f"Expected 2, got {count}"

    def test_car_search_model_appears(self):
        routes_page = self.open_supportive_order_form()
        routes_page.enter_comment_input(data.MESSAGE_FOR_DRIVER)
        routes_page.order_button()

        assert routes_page.get_car_search_modal()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
