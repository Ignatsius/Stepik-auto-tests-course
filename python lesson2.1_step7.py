from selenium import webdriver
import time
import math


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    y = browser.find_element_by_id('treasure')

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = y.get_attribute('valuex')
    assert x is not None

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    z = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(z)

    # Отметить checkbox "I'm the robot".
    # Выбрать radiobutton "Robots rule!"
    # Нажать на кнопку "Submit"
    #for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    #    browser.find_element_by_css_selector(selector).click()

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
