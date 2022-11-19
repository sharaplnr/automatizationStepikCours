from selenium import webdriver

browser = webdriver.Chrome()

# Переключение на alert
alert = browser.switch_to.alert
# Принять alert
alert.accept()

# Получение текста из alert
alert.text

# Переключение на confirm
confirm = browser.switch_to.alert
# Принять confirm
confirm.accept()
# Отклонить confirm
confirm.dismiss()

# Переключение на prompt
prompt = browser.switch_to.alert
# Ввод в поле prompt
prompt.send_keys('Answer')
# Принять prompt
prompt.accept()