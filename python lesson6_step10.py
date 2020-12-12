# Уникальность селекторов: часть 2 
# (зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом)

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # First name
    # использовать такой селектор лучше, чем по class_name т.к. он является более уникальным
    # class_name так же подходит, суть в родительском классе .first_block
    input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
    input1.send_keys("Artem")
    # Last name
    input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
    input2.send_keys("Kolobov")
    # Email
    input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
    input3.send_keys("g2@mail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # Дождаемся загрузки следующей страницы, прежде чем выполнять проверки
    # Не самый лучший способ из за неконкретного времени
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()