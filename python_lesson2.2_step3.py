# Задание: работа с выпадающим списком

from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser= webdriver.Chrome()
    browser.get(link)

    def calc(num1, num2):
        return str(int(num1) + int(num2))

    num1_text = browser.find_element_by_id('num1')
    num1 = num1_text.text
    num2_text = browser.find_element_by_id('num2')
    num2 = num2_text.text

    summ = calc(num1, num2)

    from selenium.webdriver.support.ui import Select  # Подключение библиотеку WebDriver
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(summ)

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