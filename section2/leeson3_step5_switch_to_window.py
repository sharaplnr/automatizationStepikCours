from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# Переключение на другую вкладку
browser.switch_to.window('window_name')

# Возвращение имени вкладки из массива
new_window = browser.window_handles[1] # имя второй вкладки

# Имя текущ. вкладки
first_window = browser.window_handles[0]

# После переключения на другую вкладку, можно работать с элементами страница из этой вкладки
