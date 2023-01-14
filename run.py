from booking.booking import Booking 
import time

try:
    with Booking() as bot:
        bot.land_first_page()
        # bot.choose_currency(currency='USD')
        # bot.select_place('New York')
        # bot.select_dates('2023-01-15', '2023-01-19')
        # bot.select_guests(1)
        # bot.search()
        bot.apply_filtrations(5, 'price')
        time.sleep(5)
except Exception as e:
    if 'in PATH' in str(e):
      print(
        'You are trying to run the bot from command line \n'
        'Please add to PATH your Selenium Drivers \n'
        'Windows: \n'
        '        set PATH=%PATH;C:path-to-your-folder \n \n'
        'Linux: \n'
        '       PATH=%PATH:/path/toyour/folder/ \n'
      )
    else:
        raise    