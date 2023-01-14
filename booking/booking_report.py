# This file is going to include method tall will parse
# The specific data that we need from each one of the deal boxes


from selenium.webdriver.remote.webelement import WebElement


class BookingReport():
    def __init__(self, property_cards: WebElement):
        self.property_cards = property_cards

    def pull_titles(self):
        for i in self.property_cards:
            hotel_name = i.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            price = i.find_element_by_css_selector(
                'span[data-testid="price-and-discounted-price"]'
            ).text
            score = i.find_element_by_css_selector(
                'div[data-testid="review-score"]'
            ).text
            print(f'{hotel_name}: {price} --- Score: {score}')