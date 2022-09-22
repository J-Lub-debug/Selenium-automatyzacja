from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome): # inherit from webdriver.Chrome to use its methods
    # Constructor it's going to run immediately when we instantiate object of this class
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__() # super reference base class from which we inherited
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):  # default value None
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click();

        # *= means it contain substring of
        # f before strings means formatted_string which allows use of {}
        selected_currency_element = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.CSS_SELECTOR, 'input[name="ss"]')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        #first_result = self.find_element(By.CSS_SELECTOR, 'div[tabindex="-1"]')
        first_result.click()

    # It only accepts dates from current Month/Next month in 'yyyy-mm-dd' format
    def select_dates(self, check_in_date, check_out_date):
        # unable to find such element for some reason
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    # + improve this version by selecting date that is further in the future ex. 3 months
    # + try catch error when one of dates is Earlier than Today - date.today

    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID, "xp__guests__toggle")
        selection_element.click()

        decrease_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
        increase_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')

        # decrease Default Value of adults to minimal value (1)
        while True:
            decrease_adults_element.click()
            adults_value_element = self.find_element(By.ID, "group_adults") # min=1 max=30
            adults_value = adults_value_element.get_attribute('value') #Should return adults count | Returns value as String

            if int(adults_value) == 1:
                break

        # Increase number of adults to {count}
        for _ in range(count - 1): # _ - no usage of "i" value {Python specific}
            increase_adults_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]') #There's another element with this selector but it chooses the First one
        search_button.click()

    # Instantiate another class since the file got long
    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self) # pass self object (Driver) to class and instantiate its Object
        filtration.apply_star_rating(3, 4, 5)

        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element(By.CLASS_NAME, 'd4924c9e74')

        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score" ]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)









