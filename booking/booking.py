import booking.constants as const
import os
import time
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=const.SELENIUM_DRIVER, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        #add strings to ignore some errors
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.implicitly_wait(15)
        # self.get(const.BASE_URL)
        self.get(const.STEPS)
        time.sleep(3)

    def choose_currency(self, currency=None):
        try:
            self.implicitly_wait(5)
            currency_element = self.find_element_by_css_selector(
                'button[data-tooltip-text="Choose your currency"]'
            )
            currency_element.click()
            selected_currency = self.find_element_by_css_selector(
                f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
            )
            selected_currency.click()
            time.sleep(3)
        except:
            print('HTML Element not loaded')

    def select_place(self, place):
        time.sleep(7)
        self.implicitly_wait(15)
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place)

        first_result = self.find_element_by_css_selector('li[data-i="0"]')
        first_result.click()
        time.sleep(3)

    def select_dates(self, checkin, checkout):
        self.implicitly_wait(15)
        checkin_element = self.find_element_by_css_selector(f'td[data-date="{checkin}"]')
        checkin_element.click()
        checkout_element = self.find_element_by_css_selector(f'td[data-date="{checkout}"]')
        checkout_element.click()
        time.sleep(3)
    
    def select_guests(self, count=1):
        guests = self.find_element_by_id('xp__guests__toggle')
        guests.click()
        while True:
            decrease_adults = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults.click()
            adults_value = self.find_element_by_id('group_adults').get_attribute('value')
            if int(adults_value) == 1:
                break
        increase_button = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        for _ in range(count - 1):
            increase_button.click()

    def search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtrations(self, stars, trigger):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(stars)
        filtration.dropdown_triggers(trigger)
    
    def report_results(self):
        property_cards = self.find_elements_by_css_selector(
            'div[data-testid="property-card"]'
        )
        # property_cards = self.find_element_by_class_name("d4924c9e74")
        report = BookingReport(property_cards)
        report.pull_titles()