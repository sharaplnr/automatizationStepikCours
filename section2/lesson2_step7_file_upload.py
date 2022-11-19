from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__)) # путь текущей директории исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(__file__))
