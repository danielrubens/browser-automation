from booking.booking import Booking 

with Booking() as bot:
    bot.land_first_page()
    bot.choose_currency(currency='USD')
    bot.select_place('New York')