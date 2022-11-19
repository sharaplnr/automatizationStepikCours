from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    radio_button = browser.find_element(By.ID, 'peopleRule')
    radio_button_get_checked = radio_button.get_attribute('checked')
    radio_button_get_id = radio_button.get_attribute('id')
    robots_radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton_checked = robots_radiobutton.get_attribute('checked')

    print(radio_button_get_checked, type(radio_button_get_checked))
    print(radio_button_get_id, type(radio_button_get_checked))
    print(radiobutton_checked, type(radiobutton_checked))

    assert radio_button_get_checked is not None, 'People radio is not selected by default'


finally:
    time.sleep(2)
    browser.quit()