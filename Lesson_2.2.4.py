from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_num1 = browser.find_element_by_css_selector("[type=submit]")
    x_num1.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    num1 = browser.find_element_by_xpath("//span[@class='nowrap'][@id='input_value']")
    x = str(num1.text)
    y = calc(x)
    #print(num)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)


    #from selenium.webdriver.support.ui import Select
    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value(str(z))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)