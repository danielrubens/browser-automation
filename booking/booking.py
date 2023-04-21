import booking.constants as const
import os
import time
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable



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
        self.get(const.BASE_URL)
        time.sleep(3)

    def choose_candidate(self):
        try:
            self.implicitly_wait(5)
            currency_element = self.find_element_by_css_selector(
                'input[value="1018"]'
            )
            currency_element.click()
            selected_currency = self.find_element_by_css_selector(
                f'button[class="buttonForm"]'
            )
            selected_currency.click()
            time.sleep(3)
        except:
            print('HTML Element not loaded')

    def fill_name(self, name):
        time.sleep(2)
        self.implicitly_wait(2)
        search_field = self.find_element_by_id('nome')
        search_field.send_keys('Daniel Rubens')
        # time.sleep(3)

    def fill_email(self, email):
        time.sleep(2)
        self.implicitly_wait(2)
        search_field = self.find_element_by_id('email')
        search_field.send_keys('danielrubens@gmail.com')
    
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
        report = BookingReport(property_cards)
        table = PrettyTable(
            field_names=['Hotel Name', 'Hotel Price', 'Hotel Score']
        )
        table.add_rows(report.pull_hotel_attributes())
        print(table)