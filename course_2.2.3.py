from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def sum(x, y):
    return str(x + y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "span#num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, "span#num2")
    y =  int(y_element.text)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(sum(x,y))
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
print(sum(x, y)) #проверка правильности работы функции суммирования