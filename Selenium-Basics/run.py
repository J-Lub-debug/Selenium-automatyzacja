from booking.booking import Booking

with Booking() as bot:  # context manager
    bot.land_first_page()
    #bot.change_currency(currency='GBP')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2022-09-28', check_out_date='2022-10-06')
    bot.select_adults(10)
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() #A workaround to let our bot to grab the data properly
    bot.report_results()
    # __exit__ method gets called here after Python exits the Context "with" indent
