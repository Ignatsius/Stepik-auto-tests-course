from selenium import webdriver # Подключаем драйвер селениума
import time  # Подрубаем таймер

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text') # Открываем браузер
    link = browser.find_element_by_link_text('224592') # Находим ссылку
    link.click() # Кликаем на ссылку
    input1 = browser.find_element_by_tag_name('input') # Поиск элемента по названию тега элемента
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name') # Поиск по атрибуту name элемента
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city') # Находим ссылку
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country') # Находим ссылку
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn") # Находим ссылку
    button.click() # Находим ссылку

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла