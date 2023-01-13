'''This file will include a class with instance methods.
That will be responsible to interact with our website
after we have some results, to apply friltrations.'''

from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def apply_star_rating(self):
        self.driver.find_element_by_id('filter_class')
