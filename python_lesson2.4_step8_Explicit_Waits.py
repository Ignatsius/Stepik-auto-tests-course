from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import*

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    def calc(x):
        return str(log(abs(12*sin(int(x))))) 

    x_text = browser.find_element_by_id('input_value')
    x = x_text.text

    answer = calc(x)

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)

    button_primary = browser.find_element_by_id("solve")
    button_primary.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
