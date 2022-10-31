
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')

driver.get('https://www.baidu.com')

# 通过id=kw去取输入框的元素
# inp = driver.find_element(By.ID,'kw')

inp = driver.find_element(By.CSS_SELECTOR,'#kw')
# 通过class=bg s_btn 去获取按钮的元素
# button = driver.find_element(By.CLASS_NAME,'s_btn')
button = driver.find_element(By.CSS_SELECTOR,'.s_btn')

# send_keys(需要输入的内容) 输入内容
inp.send_keys('selenium')

# click() 点击
button.click()