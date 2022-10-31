# pip install selenium 安装
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#webdriver 浏览器驱动
#使用webdriver,先给浏览器移植一个驱动
#支持驱动的浏览器：Chrome（谷歌浏览器） Firefox（火狐浏览器）
#              Edge（WIN10自带浏览器） IE浏览器

#安装Edge浏览器驱动
# 打开官网链接，下载驱动
# （重要）查看下载的版本支持 Version: 107.0.1418.26
#  在浏览器的地址栏输入 edge://version/
# 查看自己的浏览器的版本：Microsoft Edge	107.0.1418.26 (正式版本) (64 位)
# （注意）如果版本低 那就在浏览器的设置中，找到关于浏览器，更新一下。

# 下载对应驱动后，解压文件得到 msedgedriver.exe
# 将 msedgedriver.exe 放到msedge.exe(edge软件的根目录)
# 选中Edge图标，右键“打开文件位置”,继续选择并打开文件位置
# msedgedriver.exe 放置到这个目录

# 得到浏览器对象
# edge = webdriver.Edge()
edge = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')

# chrome = webdriver.chrome()
# firefox = webdriver.firefox()
# 打开百度这个网页
edge.get("https://www.baidu.com")

time.sleep(5)

#获取百度的输入框
input = edge.find_element(By.ID,'kw')
#清空百度输入框中的内容
input.clear()
#输入内容
input.send_keys('selenium')

