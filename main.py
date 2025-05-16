from selenium import webdriver
import data
import helpers
from helpers import is_url_reachable
from pages import UrbanRoutesPage  # assuming you have this class in this file

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        assert routes_page.get_current_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        routes_page.fill_verification_code(code)
        assert routes_page.is_phone_verified() == True

    def test_fill_card_details(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        routes_page.fill_verification_code(code)
        routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.is_card_valid() == True

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        routes_page.fill_verification_code(code)
        routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.wait_for_driver()
        routes_page.write_comment()
        assert routes_page.is_driver_assigned(), "Driver was not assigned"
        assert routes_page.is_comment_visible(), "Comment is not visible"

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        routes_page.fill_verification_code(code)
        routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.wait_for_driver()
        routes_page.write_comment()
        routes_page.order_blanket_and_handkerchiefs()
        assert routes_page.is_blanket_and_handkerchief_ordered(), "Blanket and handkerchiefs were not successfully ordered"

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        routes_page.fill_verification_code(code)
        routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.wait_for_driver()
        routes_page.write_comment()
        routes_page.order_blanket_and_handkerchiefs()
        routes_page.order_2_ice_creams()
        assert routes_page.are_2_ice_creams_ordered(), "2 ice creams were not successfully ordered"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        routes_page.fill_verification_code(code)
        routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.wait_for_driver()
        routes_page.write_comment()
        routes_page.order_blanket_and_handkerchiefs()
        routes_page.order_2_ice_creams()
        assert routes_page.does_car_search_model_appear(), "Car search model does not appear"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
