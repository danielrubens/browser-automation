from booking.booking import Booking 
import time

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.choose_currency(currency='USD')
        bot.select_place(input("Where do you want to go?"))
        bot.select_dates(input("Checkin date"), input("Checkout date"))
        bot.select_guests(int(input("How many guests?")))
        bot.search()
        bot.apply_filtrations(5, 'price')
        time.sleep(5)
        bot.refresh()
        bot.report_results()
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