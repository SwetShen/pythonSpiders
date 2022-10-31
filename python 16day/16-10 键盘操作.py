from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 选项设置需要在get网页之前设置
edge_options = webdriver.EdgeOptions()
# 设置无界面访问
# edge_options.add_argument('--headless')
# edge_options.add_argument('--disable-gpu')

src = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
driver = webdriver.Edge(src,options=edge_options)

driver.get('https://www.meishij.net/fenlei/haixian/')

#Ctrl + A 选中所有内容
#perform()执行前面的所有操作
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').send_keys("c").perform()

