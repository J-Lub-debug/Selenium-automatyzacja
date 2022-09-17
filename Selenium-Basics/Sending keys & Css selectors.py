from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demo.anhtester.com/basic-first-form-demo.html")

driver.implicitly_wait(5)

first_input = driver.find_element(By.ID, 'sum1').send_keys(15)
second_input = driver.find_element(By.ID, 'sum2').send_keys(Keys.NUMPAD1, Keys.NUMPAD5)

#By array id
#button = driver.find_elements(By.CLASS_NAME, 'btn-default')[1].click()

#By CSS elector
button = driver.find_element(By.CSS_SELECTOR,'button[onclick="return total()"')
button.click()
