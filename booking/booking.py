import booking.constants as const
import os
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=const.SELENIUM_DRIVER, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def choose_currency(self, currency=None):
        self.implicitly_wait(15)
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency.click()

    def select_place(self, place):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place)

        first_result = self.find_element_by_css_selector('li[data-i="0"]')
        first_result.click()