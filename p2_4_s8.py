# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:15:33 2020

@author: KseniaYa
"""

"""
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    x = float(x)
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(link)
    
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element_by_id("book")
    button.click()
    

    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    inpt = browser.find_element_by_id("answer")
    inpt.send_keys(y)
    
    button = browser.find_element_by_id("solve")
    button.click()
    
    time.sleep(10)
    
finally:
    browser.quit()