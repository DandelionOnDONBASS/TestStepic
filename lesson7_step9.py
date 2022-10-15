from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math 



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    x1=x.text
    x2 = int(x1)
    y = browser.find_element(By.ID, "num2")
    y1 = y.text
    y2=int(y1)



    sum = y2 + x2
    sum1 = str(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum1)



    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()




finally:
 
    time.sleep(10)
 
    browser.quit()