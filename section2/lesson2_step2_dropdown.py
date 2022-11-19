from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text

    sum = int(num1) + int(num2)

    select_dropdown = browser.find_element(By.ID, 'dropdown')
    select_dropdown.click()

    dropdown_value = browser.find_element(By.XPATH, f'//select/option[text()="{sum}"]')
    dropdown_value.click()


finally:
    time.sleep(5)
    browser.quit()