import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
result = math.ceil(math.pow(math.pi, math.e) * 10000)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    linkText = browser.find_element(By.LINK_TEXT, str(result))
    linkText.click()

    firstName = browser.find_element(By.NAME, 'first_name')
    firstName.send_keys('Ilnur')

    lastName = browser.find_element(By.NAME, 'last_name')
    lastName.send_keys('Sharapov')

    cityInput = browser.find_element(By.CLASS_NAME, 'city')
    cityInput.send_keys('Kazan')

    countryInput = browser.find_element(By.ID, 'country')
    countryInput.send_keys('RT')

    submitButton = browser.find_element(By.CLASS_NAME, 'btn')
    submitButton.click()


finally:
    time.sleep(5)
    browser.quit()