"""
Установка - pip install selenium==4.*
Версии библиотек в вирт. окружении - pip list

Драйвер для Chrome - https://sites.google.com/chromium.org/driver/downloads
Список различных версий для Chrome - https://chromedriver.storage.googleapis.com/index.html
Версия браузера - chrome://version/

Инструкция:
1. Скачать версию драйвера с текущей версией браузера на компе;
2. Разархивировать файл драйвера в каталог C:\chromedriver
3. Добавить в переменную PATH папку из шага 2
4. В cmd выполнить команду path → Среди переменных сред, указан добавленный каталог
5. Вызвать драйвер напрямую командой - chromedriver

Запуск из консольный строки (для общего ознакомления):
1. mkdir selenium_course - создание папки
2. copy C:\Users\user\Downloads\first_script.py c:\Users\user\selenium_course
3. environments\selenium_env\Scripts\activate.bat
4. python c:\Users\user\selenium_course\first_script.py

"""

### Запуск браузера и первый скрипт ###

import time
from selenium import webdriver # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By # импортируем класс By, который позволяет выбрать способ поиска элемента

# инициализируем драйвер браузера. После этой команды видно новое открытое окно браузера
driver = webdriver.Chrome()
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get('https://stepik.org/lesson/25969/step/12')
time.sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему.
# Метод принимает в качестве аргументов способ поиска и значение, по которому будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, '.textarea')

# Напишем текст в найденное поле
textarea.send_keys('get()')
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, '.submit-submission')

# Скажем драйверу, что нужно нажать на кнопку. После этой команды должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# Закрытие окна браузера
driver.quit()





