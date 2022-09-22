# This file will include a class with instance methods.
# That will be responsible to interact with our website.
# After we have some results, to apply filtration.
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.remote.webdriver import WebDriver  # req for autocompletion

# No autocompletion due to not known type before the actual passing takes place
class BookingFiltration:
    def __init__(self, driver:WebDriver): # :type req for autocompletion
        self.driver = driver

    def apply_star_rating(self, *star_values): # *parameter - pass many arguments to one argument
        # doesn't work even with the implicit_wait. ERROR: Element not clickable at Point
        # star_rating_checkbox = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-item="class:class=4"] > input:first-child')

        # Gets first child (input checkbox) of div parent and runs click trough JS-Executor
        for star_value in star_values:
            self.driver.execute_script(
                f"""document.querySelector('div[data-filters-item="class:class={star_value}"] > input:first-child').click()""")
    def sort_price_lowest_first(self):
        sort_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        sort_element.click()
        lowest_price_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"')
        lowest_price_element.click()
