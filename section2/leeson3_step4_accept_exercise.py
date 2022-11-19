from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def culc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_magical = browser.find_element(By.XPATH, '//button[contains(@class, "btn")]')
    button_magical.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.XPATH, '//span[@id = "input_value"]')
    result = culc(x_element.text)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(result)

    button_submit = browser.find_element(By.CLASS_NAME, 'btn')
    button_submit.click()


finally:
    time.sleep(5)
    browser.quit()