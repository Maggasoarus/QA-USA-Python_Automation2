from selenium.webdriver.chrome import webdriver

import data
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    if is_url_reachable(data.URBAN_ROUTES_URL):
        print("urban routes found")
    else:
        print("urban routes not found")


class UrbanRoutesPage:
    def set_route(self, ADDRESS_FROM, ADDRESS_TO):
        pass

    def get_from(self):
        pass

    def get_to(self):
        pass


def test_set_route(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    assert routes_page.get_from() == data.ADDRESS_FROM
    assert routes_page.get_to() == data.ADDRESS_TO


def test_select_plan(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.select_supportive_plan()
    assert routes_page.get_current_selected_plan() == ‘supportive’


def test_fill_phone_number(self):
    # Add in S8
    print("function created for fill phone number")
    pass


def test_fill_card(self):
    # Add in S8
    print("function created for fill card")
    pass


def test_comment_for_driver(self):
    # Add in S8
    print("function created for driver comment")
    pass


def test_order_blanket_and_handkerchiefs(self):
    # Add in S8
    print("function created for blanket and handkerchiefs")
    pass


def test_order_2_ice_creams(self):
    number_of_ice_creams = 2
    for count in range(number_of_ice_creams):
    # Add in S8
    pass


def test_car_search_model_appears(self):
    # Add in S8
    print("function created for car search model")
    pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
