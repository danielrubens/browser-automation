'''This file will include a class with instance methods.
That will be responsible to interact with our website
after we have some results, to apply friltrations.'''

from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def apply_star_rating(self):
        # star_filtration_box = self.driver.find_element_by_id('filter_class')
        star_filtration_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        print(star_filtration_box)
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
        for i in star_child_elements:
            print(i)
        # print(len(star_child_elements))
