from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/math.html'

def culc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num_x = browser.find_element(By.ID, 'input_value')
    result = culc(num_x.text)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(result)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    button_submit = browser.find_element(By.XPATH, '//button[contains(@class, "btn")]')
    button_submit.click()



finally:
    time.sleep(5)
    browser.quit()