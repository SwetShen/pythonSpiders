# 无网页模式打开
from selenium import webdriver
from selenium.webdriver.common.by import By

# 选项设置需要在get网页之前设置
edge_options = webdriver.EdgeOptions()
# 设置无界面访问
# edge_options.add_argument('--headless')
# edge_options.add_argument('--disable-gpu')
edge_options.headless = True

src = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
driver = webdriver.Edge(src,options=edge_options)

driver.get('https://www.baidu.com')

#获取标题
print(driver.title)
