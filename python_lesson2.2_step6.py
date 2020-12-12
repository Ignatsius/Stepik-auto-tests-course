from selenium import webdriver
import time
from math import*

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()                # 1-8 Открытие страницы браузера
    browser.get(link)

    x_text = browser.find_element_by_id("input_value")
    x = x_text.text

    def calc(x):
        return str(log(abs(12*sin(int(x)))))

    y = calc(x)

    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.click()

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

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()