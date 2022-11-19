from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.NAME, 'first_name')
    firstName.send_keys('Ilnur')

    lastName = browser.find_element(By.NAME, 'last_name')
    lastName.send_keys('Sharapov')

    cityInput = browser.find_element(By.CLASS_NAME, 'city')
    cityInput.send_keys('Kazan')

    countryInput = browser.find_element(By.ID, 'country')
    countryInput.send_keys('RT')

    submitButton = browser.find_element(By.ID, 'submit_button')
    submitButton.click()

finally:
    time.sleep(5)
    browser.quit()


