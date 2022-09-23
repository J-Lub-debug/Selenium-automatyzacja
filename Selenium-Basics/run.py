from booking.booking import Booking

with Booking() as bot:  # context manager
    bot.land_first_page()
    #bot.change_currency(currency='GBP')
    bot.select_place_to_go(input("Where you want to go?"))
    #bot.select_dates(check_in_date='2022-09-28', check_out_date='2022-10-06')
    bot.select_dates(check_in_date=input("Check in date in yyyy-mm-dd format"),
                     check_out_date=input("Check out date in yyyy-mm-dd format"))
    bot.select_adults(int(input("How many adults?")))
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() #A workaround to let our bot to grab the data properly
    bot.report_results()
    # __exit__ method gets called here after Python exits the Context "with" indent
