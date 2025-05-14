import self
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
from_field = (By.ID, 'from')
to_field = (By. ID, 'to’)
supportive_plan_card = (By. XPATH, '//div[contains(text(), "Supportive")]*)
supportive_plan_card_parent = (By-XPATH, '//div[contains(text(), "Supportive")]//..')
active_plan_card = (By. XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
call_taxi_button = (By. XPATH, ' //button[contains(text(), "Call a taxi")]')

def set_route (self, from_address, to_address):
self. set_from (from_address)
self.set_to (to_address)
self.click_call_taxi_button ()

def set_from (self, from_address):
from_field = self.driver.find_element (*self. from_field)
from_field.send_keys (from.address)

def set_to (self, to_address):
to_field = self.driver.find_element (*self. to_field)
to_field.send_keys (to.address)

def get_from (self):
return self.driver.find_element (*self.from_field).get_property (‘value’)

def get_to (self):
return self.driver.find_element (*self.to_field).get_property (‘value’)

def click_call_taxi_button (self):
self.driver.find_element (*self.call_taxi_button).click ()

def set_route (self, from_address, to_address):
self. set_from (from_address)
self.set_to (to_address)
self.click_call_taxi_button ()