'''
Для поиска элементов Selenium используется метод find_element, который принимает два аргумента тип локатора и значение
локатора.

Селектор/локатор - это способ идентификации веб элемента/элементов в браузере через, например CSS/Xpath правила.

Разновидности типов локатора в методе:
- find_element(By.ID, value)
- find_element(By.NAME, value)
- find_element(By.CLASS_NAME, value)
- find_element(By.TAG, value)
- find_element(By.CSS_SELECTOR, value)
- find_element(By.LINK_TEXT, value) поиск ссылки по полному совпадению
- find_element(By.PARTIAL_LINK_TEXT, value) поиск ссылки по тексту вхождения
- find_element(By.XPATH, value) поиск элемента с помощью языка запросов XPath

Импорт необходимых модулей

from selenium import webdriver
from selenium.webdriver.common.by import By - импорт класса By, которые содержит всевозможные локаторы

Пример инициализации драйвера хром, переход на ссылку, поиск элемента по ID

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")

NoSuchElementException - не правильно указан локатор

Если с помощью локатора найдены несколько элементов, то выберется первый из них.

Локаторы - стратегия поиска и значения, по которым должен выполняться поиск. Н-р можно искать по локатору By.ID со зна-
чением "send_button"

browser.quit() - закрытие браузера, закрывает все окно, вкладки и процессы вебдрайвера, запущенные во время тестовой
сессии.

browser.close() - закрывает текущее окно браузера.

Для того, чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, используют конструкцию
try/finally

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    browser.quit()

Если в блоке try произойдёт какая-нибудь ошибка, то код в блоке finally выполнится в любом случае.


Материал по ошибкам и исключениям - https://stepik.org/lesson/24463/step/1?unit=6771

Доп. - Команды в терминале
tasklist - список работающих процессов
tasklist /IM chromedriver.exe /T /F - принудительное завершение процесса драйвера

'''