from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'

def culc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure')
    value_from_treasure = treasure.get_attribute('valuex')

    result = culc(value_from_treasure)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(result)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.ID, 'robotsRule')
    robot_radiobutton.click()

    button_submit = browser.find_element(By.CLASS_NAME, 'btn')
    button_submit.click()

finally:
    time.sleep(5)
    browser.quit()