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
        star_filtration_box.click()
        time.sleep(5)
    
    def dropdown_triggers(self, trigger):
        trigers = self.driver.find_element_by_css_selector(
            'button[data-testid="sorters-dropdown-trigger"]'
        )
        trigers.click()
        order_trigers = ['popularity', 'upsort_bh', 'price', 'review_score_and_price',
                         'class', 'class_asc', 'class_and_price', 'distance_from_search' ]
        order_trigers_button = self.driver.find_element_by_css_selector(
            f'button[data-id="{trigger}"]'
        )
        order_trigers_button.click()



