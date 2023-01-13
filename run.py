from booking.booking import Booking 

with Booking() as bot:
    bot.land_first_page()
    bot.choose_currency(currency='USD')
    bot.select_place('New York')
    bot.select_dates('2023-01-12', '2023-01-15')