from booking.booking import Booking 
import time


with Booking() as bot:
    bot.land_first_page()
    # bot.choose_currency(currency='USD')
    # bot.select_place('New York')
    # bot.select_dates('2023-01-15', '2023-01-19')
    # bot.select_guests(1)
    # bot.search()
    bot.apply_filtrations(5)
    time.sleep(5)
    