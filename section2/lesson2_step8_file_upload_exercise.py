from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name_field = browser.find_element(By.XPATH, '//input[@name = "firstname"]')
    name_field.send_keys('Testname')
    lastname_field = browser.find_element(By.XPATH, '//input[@name = "lastname"]')
    lastname_field.send_keys('Testlastname')
    email_field = browser.find_element(By.XPATH, '//input[@name = "email"]')
    email_field.send_keys('x@x.x')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'file.txt'
    file_path = os.path.join(current_dir, file_name)

    file_upload = browser.find_element(By.XPATH, '//input[@id = "file"]')
    file_upload.send_keys(file_path)

    submit_btn = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()