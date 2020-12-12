#Задание: загрузка файла
#В этом задании в форме регистрации требуется загрузить текстовый файл.

# импортируем модуль
import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Artem')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Kolobov')
    input_email = browser.find_element_by_name('email')
    input_email.send_keys('llll@ll.ru')

    # получаем путь к директории текущего исполняемого скрипта
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "text.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # Выбираем кнопку добавить файл
    element = browser.find_element_by_css_selector("[type='file']")
    # отправляем файл
    element.send_keys(file_path)

# Нажать на кнопку Submit
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()