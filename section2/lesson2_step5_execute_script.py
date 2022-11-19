from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    # button.location_once_scrolled_into_view
    browser.execute_script('arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()