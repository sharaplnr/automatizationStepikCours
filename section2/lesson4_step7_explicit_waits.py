from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/wait2.html')

button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'verify'))) # Ждать в течение 5 сек, пока элемент не станет активной
button.click()

message = browser.find_element(By.ID, 'verify_message')


assert 'successful' in message.text

browser.quit()

# Другие правила ожидания - https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
# Также можно создать негативное ожидание с помощью until_not
# Проверять в течение 5 сек, пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, 'verify')))