'''This file will include a class with instance methods.
That will be responsible to interact with our website
after we have some results, to apply friltrations.'''

from selenium.webdriver.remote.webdriver import WebDriver
import time



class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def apply_star_rating(self, stars):
        star_filtration_box = self.driver.find_element_by_css_selector(
            f'div[data-filters-item="class:class={str(stars)}"]'
        )
        # star_filtration_box = self.driver.find_element_by_css_selector(
        #     'div[data-filters-group="class"]'
        # )
        # print(star_filtration_box)
        star_filtration_box.click()
        time.sleep(5)


