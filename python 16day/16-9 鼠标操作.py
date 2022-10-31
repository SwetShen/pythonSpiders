from selenium import webdriver
from selenium.webdriver.common.by import By

# 选项设置需要在get网页之前设置
edge_options = webdriver.EdgeOptions()
# 设置无界面访问
# edge_options.add_argument('--headless')
# edge_options.add_argument('--disable-gpu')

src = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
driver = webdriver.Edge(src,options=edge_options)

driver.get('https://lishi.tianqi.com/chongqing/202202.html')

#click() 点击
more = driver.find_element(By.CLASS_NAME,'lishidesc2')
more.click() #打开隐藏的元素

ali = driver.find_elements(By.CSS_SELECTOR,'.thrui>li')
for li in ali:
    date = li.find_element(By.CLASS_NAME,'th200')
    print(date.text)
    infos = li.find_elements(By.CLASS_NAME,'th140')
    for info in infos:
        print(info.text)

