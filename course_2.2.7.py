from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 150);")
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
print(y)