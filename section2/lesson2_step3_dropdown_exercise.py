from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html' # https://suninjuly.github.io/selects2.html

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text

    sum = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum))

    button_submit = browser.find_element(By.CLASS_NAME, 'btn')
    button_submit.click()

finally:
    time.sleep(5)
    browser.quit()