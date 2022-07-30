from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
    
    
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))    


try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button.click()
    browser.execute_script("window.scrollBy(0, 400);")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_attribute = x_element.text
    x = x_attribute
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "#solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()