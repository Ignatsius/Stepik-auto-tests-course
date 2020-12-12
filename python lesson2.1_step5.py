from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать математическую функцию от x
    # Функция calc(), которая рассчитает и вернет вам значение функции
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считать значение для переменной x
    # Считаем значение х через функцию
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click() 

    # Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



    # Улучшеный вариант кода:

"""from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    browser.find_element_by_css_selector(selector).click()"""