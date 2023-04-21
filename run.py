from booking.booking import Booking 
import time

try:
    with Booking() as bot:
      
        # time.sleep(2)  
        bot.land_first_page()
        # bot.choose_candidate()
        # time.sleep(2)
        bot.fill_name(name='')
        bot.fill_email(email='')
        # bot.select_guests(int(input("How many guests?")))
        # bot.search()
        # bot.apply_filtrations(5, 'price')
        # time.sleep(5)
        # bot.refresh()
        # bot.report_results()
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