from selenium import webdriver
import time
from math import*

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    button_primary = browser.find_element_by_css_selector("button.btn")
    button_primary.click()
    # Прожимаем окей в конфирме
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(log(abs(12*sin(int(x)))))

    x_text = browser.find_element_by_id('input_value')
    x = x_text.text

    answer = calc(x)

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)

    button_primary = browser.find_element_by_css_selector("button.btn")
    button_primary.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()