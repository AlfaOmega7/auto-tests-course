from selenium import webdriver
import time
def calc(z):
  return int(sum(x, y))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_num1 = browser.find_element_by_id("num1")
    y_num2 = browser.find_element_by_id("num2")
    x = int(x_num1.text)
    y = int(y_num2.text)
    z = int(x + y)
    #print (int(z))

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(1)