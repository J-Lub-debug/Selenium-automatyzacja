from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#browser driver need to be in script folder or you need to use driver manager see https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
driver = webdriver.Chrome() #choice of browser, it requires seperate executable called chrome driver that need be put in PATH

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html") #visit given website
#it gets applied to all the elements in script
driver.implicitly_wait(3) #given in seconds, it doesn't wait if the page is already loaded before that time passes
my_element = driver.find_element(By.ID, "downloadButton")
my_element.click()


WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), #element filtration
        'Complete!' #expected text
    )
)