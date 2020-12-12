from selenium import webdriver
import time
from math import*

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_primary = browser.find_element_by_css_selector("button.btn")
    button_primary.click()

    first_window = browser.window_handles[0]

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

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

    

# from selenium import webdriver
# import time
# import math

# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"

#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--start-maximized")
#     browser = webdriver.Chrome(options=chrome_options)

#     def go_to_link():
#         return browser.get(link)

#     def click_to_button():
#         button = browser.find_element_by_tag_name('button')
#         return button.click()

#     def find_new_window():
#         new_window = browser.window_handles[1]
#         return new_window

#     def switch_to_window(new_window):
#         return browser.switch_to.window(new_window)

#     def find_x():
#         x_element = browser.find_element_by_xpath("//span[@id='input_value']")
#         x = x_element.text
#         return x

#     def calc(x):
#         y = str(math.log(abs(12 * math.sin(int(x)))))
#         return y

#     def insert_answer(y):
#         answer = browser.find_element_by_xpath("//input[@id='answer']")
#         return answer.send_keys(y)

#     def click_to_submit():
#         submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
#         return submit.click()

#     step1 = go_to_link()
#     step2 = click_to_button()
#     step3_1 = find_new_window()
#     step3_2 = switch_to_window(step3_1)
#     step4_1 = find_x()
#     step4_2 = calc(step4_1)
#     step4_3 = insert_answer(step4_2)
#     step4_4 = click_to_submit()

# finally:
#     time.sleep(10)
#     browser.quit()