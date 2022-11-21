from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    #значение первого  и второго числа
    dgtl1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    dgtl2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    dgtl1 = int(dgtl1)
    dgtl2 = int(dgtl2)
    #нашли сумму чисел
    dgtl3 = dgtl1+dgtl2
    #ищем в списке элемент со значением равным сумме и кликаем
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(dgtl3))  # ищем элемент с текстом "равным" сумме

    #xz = skarb.get_attribute("valuex")
    #xz = browser.find_element(By.CSS_SELECTOR, "div.form-group > label > span:nth-child(2)")
    #xz = int(xz)
    #fxz = calc(xz)
    #Ввести ответ в текстовое поле
    #input1 = browser.find_element(By.CSS_SELECTOR, "div.form-group input").send_keys(fxz)
    #Отметить checkbox "I'm the robot"
    #ChB1 = browser.find_element(By.CSS_SELECTOR, "div.form-check.form-check-custom > input.form-check-input")
    #ChB1 = browser.find_element(By.CSS_SELECTOR, "div.form-group input.check-input[type='checkbox']")
    #ChB1.click()
    #Выбрать radiobutton "Robots rule!"
    #RB1 = browser.find_element(By.CSS_SELECTOR, "div.form-check.form-radio-custom > input.form-check-input")
    #RB1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    #RB1.click()

    # Ваш код, который заполняет обязательные поля
    #input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    #input1.send_keys("Ivan")
    #input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    #input2.send_keys("Petrov")
    #input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    #input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    #python c:\Users\Office\selenium_course\2_3_3.py Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
   # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

    