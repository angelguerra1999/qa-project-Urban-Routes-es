from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data

class UrbanRoutesPage:
    
    # Definición de selectores de elementos
    from_field = (By.ID, 'from_field_id')
    to_field = (By.XPATH, '//input[@id="to_field_id"]')
    order_taxi_button = (By.CLASS_NAME, 'order_taxi_button_class')
    comfort_tariff_button = (By.CSS_SELECTOR, '.comfort_tariff_button_class')
    telephone_number = (By.ID, 'telephone_number_id')
    phone_input = (By.ID, 'phone_input_id')
    next_button = (By.ID, 'next_button_id')
    code_field = (By.ID, 'code_field_id')
    code_confirmation_button = (By.ID, 'code_confirmation_button_id')
    payment_method = (By.ID, 'payment_method_id')
    add_card = (By.ID, 'add_card_id')
    card_number_field = (By.ID, 'card_number_field_id')
    card_code_field = (By.ID, 'card_code_field_id')
    add_button = (By.ID, 'add_button_id')
    card_close_button = (By.ID, 'card_close_button_id')
    message = (By.ID, 'message_id')
    blanket_and_scarves_switch = (By.XPATH, '//input[@id="blanket_and_scarves_switch_id"]')
    add_icecream = (By.ID, 'add_icecream_id')
    order_a_taxi = (By.ID, 'order_a_taxi_id')
    modal_opcional = (By.ID, 'modal_opcional_id')

    def __init__(self, driver):
        self.driver = driver

    # Métodos de acciones en la página
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
    
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def click_order_taxi_button(self):
        # Esperar a que el contenedor esté presente
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'order_taxi_button_class'))
        )
        # Esperar a que el botón sea clickeable y luego hacer clic
        taxi_click = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'order_taxi_button_class'))
        )
        taxi_click.click()

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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.modal_opcional))

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
