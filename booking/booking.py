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
        self.implicitly_wait(5)
        self.get(const.BASE_URL)
        time.sleep(3)

    def choose_candidate(self):
        try:
            self.implicitly_wait(2)
            currency_element = self.find_element_by_css_selector(
                'input[value="1018"]'
            )
            currency_element.click()
            # return True
    
            
            # self.implicitly_wait(2)
            # selected_currency = self.find_element_by_css_selector('button[type="submit"]')
            # selected_currency.click()
            # time.sleep(3)
        except:
            print('HTML Element not loaded')

    def fill_name(self, name):
        # time.sleep(2)
        # self.implicitly_wait(2)
        try:
            search_field = self.find_element_by_id('nome')
            search_field.send_keys('Daniel Rubens')
            return True
        # time.sleep(3)
        except:
            self.choose_candidate()
            self.click_vote()

    def fill_email(self, email):
        # time.sleep(2)
        # self.implicitly_wait(2)
        try:
            search_field = self.find_element_by_id('email')
            search_field.send_keys('danielrubens@gmail.com')
    
        except:
            self.choose_candidate()
            self.click_vote()

    def fill_phone(self, phone):
    #    time.sleep(2)
    #    self.implicitly_wait(2)
        try:
            search_field = self.find_element_by_id('telefone')
            search_field.send_keys('(85) 98159-6937')
    
        except:
            self.choose_candidate()
            self.click_vote()

    def check_box(self):
        try:
            search_field = self.find_element_by_id('term_user')
            search_field.click()
    
        except:
            self.choose_candidate()
            self.click_vote()

    def click_button(self):
        time.sleep(2)
        search_field = self.find_element_by_css_selector('button[type="submit"]')
        search_field.click()

    def click_vote(self):
        time.sleep(2)
        search_field = self.find_element_by_css_selector('button[type="submit"]')
        search_field.click()
    
