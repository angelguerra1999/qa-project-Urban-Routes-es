from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import data

class UrbanRoutesPage:
    # Selectores...
    
    def __init__(self, driver):
        self.driver = driver

    # Métodos de acciones en la página
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
    
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_taxi_button).click()

    def click_comfort_tariff_button(self):
        tariff = self.driver.find_elements(*self.comfort_tariff_button)
        tariff[4].click()

    def click_phone_number_field(self):
        self.driver.find_element(*self.telephone_number).click()

    def fill_in_phone_number(self):
        self.driver.find_element(*self.phone_input).send_keys(data.phone_number)
    
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_confirmation_code(self, code):
        self.driver.find_element(*self.code_field).send_keys(code)
    
    def click_code_confirmation_button(self):
        self.driver.find_element(*self.code_confirmation_button).click()

    def click_payment_method_field(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card).click()

    def enter_card_number(self):
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)

    def enter_card_code(self):
        self.driver.find_element(*self.card_code_field).send_keys(data.card_code)

    def press_tab_key(self):
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def click_card_close_button(self):
        self.driver.find_element(*self.card_close_button).click()

    def enter_new_message(self):
        self.driver.find_element(*self.message).send_keys(data.message_for_driver)

    def click_blanket_and_scarves_switch(self):
        self.driver.find_element(*self.blanket_and_scarves_switch).click()

    def click_add_icecream(self):
        self.driver.find_element(*self.add_icecream).click()

    def click_order_a_taxi(self):
        self.driver.find_element(*self.order_a_taxi).click()
    
    def wait_opcional_modal(self):
        self.driver.find_element(*self.modal_opcional)
    
    def setup_route(self):
        self.set_from(data.address_from)
        self.set_to(data.address_to)
        self.click_order_taxi_button()
    
    def enter_full_phone_number_and_confirm(self):
        self.click_phone_number_field()
        self.fill_in_phone_number()
        self.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        self.set_confirmation_code(code)
        self.click_code_confirmation_button()
    
    def add_credit_card(self):
        self.click_payment_method_field()
        self.click_add_card_button()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_number_field)).send_keys(data.card_number)
        self.enter_card_number()
        self.enter_card_code()
        self.press_tab_key()
        self.click_add_button()
        self.click_card_close_button()
