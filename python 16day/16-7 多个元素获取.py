
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')

driver.get('https://www.baidu.com')

#ID id属性
#CLASS_NAME class属性
#CSS_SELECTOR 选择器
#TAG_NAME 标签名称

#find_elements 查找多个符合要求的元素
aspan = driver.find_elements(
    By.CSS_SELECTOR,'.hotsearch-item .title-content-title')

# print(len(aspan))
for span in aspan:
    # 获取元素对象的text文本内容
    print(span.text)