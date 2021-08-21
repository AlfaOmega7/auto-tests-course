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
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element_by_id("book")
    button.click()

    num_1 = browser.find_element_by_xpath("//span[@class='nowrap'][@id='input_value']")
    x = str(num_1.text)
    y = calc(x)
    print(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(10)