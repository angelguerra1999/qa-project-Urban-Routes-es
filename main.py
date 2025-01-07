import data
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import helpers
import urban_routes_page

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # Configuración de opciones de Chrome
        chrome_options = Options()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urban_routes_page.UrbanRoutesPage(cls.driver)

        # Configurar la ruta inicial una sola vez
        cls.routes_page.setup_route()

    def test_set_route(self):
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        self.routes_page.click_comfort_tariff_button()
        comfort_tariff = self.driver.find_elements(*self.routes_page.comfort_tariff_button)
        assert "tcard" in self.driver.find_element(*urban_routes_page.UrbanRoutesPage.comfort_tariff_button).get_attribute("class")
        assert comfort_tariff[4].is_enabled()

    def test_fill_phone_number(self):
        self.routes_page.enter_full_phone_number_and_confirm()
        phone_input_value = self.driver.find_element(*self.routes_page.phone_input).get_attribute("value")
        assert phone_input_value == data.phone_number

    def test_add_credit_card(self):
        self.routes_page.add_credit_card()
        card_input = self.driver.find_elements(*self.routes_page.card_added)[1]
        assert card_input.is_enabled()

    def test_write_message(self):
        self.routes_page.enter_new_message()
        assert self.driver.find_element(*self.routes_page.message).get_property('value') == data.message_for_driver

    def test_request_blanket_and_scarves(self):
        self.routes_page.click_comfort_tariff_button()
        self.routes_page.click_blanket_and_scarves_switch()
        checkbox = self.driver.find_element(*urban_routes_page.UrbanRoutesPage.switch_checkbox)
        assert checkbox.is_selected()

    def test_request_icecream(self):
        self.routes_page.click_comfort_tariff_button()
        self.routes_page.click_add_icecream()
        self.routes_page.click_add_icecream()
        icecream_counter = self.driver.find_element(*urban_routes_page.UrbanRoutesPage.icecream_counter)
        icecream_count = int(icecream_counter.text)
        assert icecream_count == 2

    def test_search_taxi(self):
        self.routes_page.enter_full_phone_number_and_confirm()
        self.routes_page.add_credit_card()
        self.routes_page.enter_new_message()
        self.routes_page.click_blanket_and_scarves_switch()
        self.routes_page.click_add_icecream()
        self.routes_page.click_add_icecream()
        self.routes_page.click_order_a_taxi()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.routes_page.modal_opcional))
        assert self.driver.find_element(*self.routes_page.modal_opcional).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
