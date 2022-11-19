import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

def culc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button_book = browser.find_element(By.ID, 'book')
    button_book.click()

    x_element = browser.find_element(By.XPATH, '//span[@id = "input_value"]')
    result = culc(x_element.text)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(result)

    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()

finally:
    time.sleep(5)
    browser.quit()