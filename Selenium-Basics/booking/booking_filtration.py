# This file will include a class with instance methods.
# That will be responsible to interact with our website.
# After we have some results, to apply filtrations.
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver #req for autocompletion

# No autocompletion due to not known type before the actual passing takes place
class BookingFiltration:
    def __init__(self, driver:WebDriver): # :type req for autocompletion
        self.driver = driver

    def apply_star_rating(self, star_value):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        print(len(star_child_elements))

        for star_element in star_child_elements:
            if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars': # strip() remove whitespaces
                star_element.click() #div element doesnt have click element, find parent or different method