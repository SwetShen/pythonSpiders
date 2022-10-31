### 1 Python Selenium 简介和环境配置

##### 1.1 Selenium 简介

  Selenium 是一个 Web 的自动化测试工具，最初是为网站自动化测试而开发的。Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。它支持所有主流的浏览器（包括 IE、Firefox、Safari、Opera 和 Chrome 等）。可以使用它对浏览器进行各种各样的模拟操作，包括爬取一些网页内容。支持多种操作系统（包括 Windows、Linux、MAC 等）

  官方文档网址：

Selenium with Python：https://selenium-python.readthedocs.io/index.html
Selenium Documentation：https://www.selenium.dev/selenium/docs/api/py/api.html

##### 1.2 Python Selenium 环境配置

  配置 Python Selenium 开发环境的步骤如下：

（1）在 Python 环境下安装 Selenium。

（2）下载浏览器的 WebDriver。

  各浏览器的 WebDriver 可以在 这里 查找或者自己搜索。

浏览器名称    WebDriver 下载地址
Chrome    https://sites.google.com/a/chromium.org/chromedriver/
http://chromedriver.storage.googleapis.com/index.html
Firefox    https://github.com/mozilla/geckodriver/releases/
IE    http://selenium-release.storage.googleapis.com/index.html
注意：WebDriver 需要和对应浏览器的版本对应，才能正常运行。

（3）安装浏览器的 WebDriver。

  将下载的 WebDriver 复制到对应的目录。不同操作系统的位置不一样，具体参照如下：

操作系统    WebDriver 放置路径
Windows    Python 的 Scripts 目录下
MAC    /usr/local/bin/
注意：这一步也可以不做，可以在使用时告知 WebDriver 所在的路径，后面会说明具体方法。

### 2 Python Selenium 基础操作

##### 2.1 启动浏览器

###### 2.1.1 普通方式启动

（1）启动 Chrome 浏览器

```
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
```

如果在配置开发环境时，没有将浏览器的 WebDriver 放到指定目录，可以告知 WebDriver 所在的路径。

```
from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
browser.get('http://www.baidu.com/')
```

(2) 启动 Firefox 浏览器

```
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.baidu.com/')
```

###### 2.1.2 Headless 方式启动

  Headless Chrome 是 Chrome 浏览器的无界面形态，可以在不打开浏览器的前提下，使用所有 Chrome 支持的特性运行你的程序。相比于现代浏览器，Headless Chrome 更加方便测试 web 应用，获得网站的截图，做爬虫抓取信息等。相比于较早的 PhantomJS 等，Headless Chrome 则更加贴近浏览器环境。

```
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# 增加无界面选项
chrome_options.add_argument('--headless')
# 如果不加这个选项，有时定位会出现问题
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=chrome_options)

browser.get('http://www.baidu.com/')
# 打印网页的标题
print(browser.title)
browser.quit()
```

也可以使用如下方式设置：

```
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# 增加无界面选项
chrome_options.headless = True
browser = webdriver.Chrome(options=chrome_options)

browser.get('http://www.baidu.com/')
# 打印网页的标题
print(browser.title)
browser.quit()
```

###### 2.1.3 加载配置启动浏览器

 Selenium 操作浏览器是不加载任何配置的，下面是关于加载 Chrome 配置的方法：

在 Chrome 地址栏输入chrome://version/，查看自己的“个人资料路径”，然后在浏览器启动时，调用这个配置文件，代码如下：

```
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#设置成用户自己的数据目录
chrome_options.add_argument(
    '--user-data-dir'
    '=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
driver=webdriver.Chrome(options=chrome_options)
```

#### 2.2 元素定位

  元素的定位是自动化测试的核心，要想操作一个元素，首先应该识别它。

  Selenium 提供了以下几种定位元素的方法：

| 描述           | 查找一个元素                         | 查找多个元素                          |
| ------------ | ------------------------------ | ------------------------------- |
| 通过 ID 定位元素   | find_element_by_id()           | find_elements_by_id()           |
| 通过标签名定位元素    | find_element_by_tag_name()     | find_elements_by_tag_name()     |
| 通过类名定位元素     | find_element_by_class_name()   | find_elements_by_class_name()   |
| 通过CSS选择器定位元素 | find_element_by_css_selector() | find_elements_by_css_selector() |

##### 2.2.1 通过 ID 定位元素

```
from selenium import webdriver

driver = webdriver.Chrome()
login_form = driver.find_element_by_id('loginForm')
```

##### 2.2.2 通过标签名定位元素

```
from selenium import webdriver

driver = webdriver.Chrome()
login_form = driver.find_element_by_tag_name('form')
```

##### 2.2.3 通过类名定位元素

```
from selenium import webdriver

driver = webdriver.Chrome()
content = driver.find_element_by_class_name('content')
```

##### 2.2.4 通过css选择器定位元素

```
from selenium import webdriver

driver = webdriver.Chrome()
content = driver.find_element_by_class_name('content')
```

#### 2.3 Selenium 三种等待方式

  现在的大多数的 Web 应用程序是使用Ajax技术。当一个页面被加载到浏览器时， 该页面内的元素可以在不同的时间点被加载。因此，有时候需要等待一些时间，让网页加载完全后再进行操作。

  存在三种等待方法可使用，分别为：强制等待、隐式等待和显式等待。

##### 2.3.1 强制等待

  强制等待通过使用 time.sleep() 实现。不管浏览器是否加载完成，程序都等待设定的时间，时间一到，继续执行后面的代码。

```
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://android.myapp.com/myapp/search.htm?kw=QQ'
driver.get(url)


#强制等待 5s 后再执行下一步

time.sleep(5)

element = driver.find_element_by_class_name('installBtn')
print(element.get_attribute('appname'))
driver.quit()
```

这种等待方式太过于死板，会严重影响程序执行速度。

##### 2.3.2 隐式等待

  隐式等待通过使用 implicitly_wait() 方法实现，默认等待时间是 0 秒。隐式等待是设置一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步；否则，一直等到时间截止，然后执行下一步。implicitly_wait() 的用法比 time.sleep() 更智能，前者是在一个时间范围内智能的等待，后者是智能等待一个固定的时间。

```
from selenium import webdriver

driver = webdriver.Chrome()

# 设置隐式等待时间，最长等待 10s

browser.implicitly_wait(10)
url = 'https://android.myapp.com/myapp/search.htm?kw=QQ'
driver.get(url)
element = driver.find_element_by_class_name('installBtn')
print(element.get_attribute('appname'))
driver.quit()
```

  隐式等待仍然有一个弊端，那就是程序会一直等待整个页面加载完成，也就是一般情况下浏览器标签栏那个小圈不再转，才会执行下一步。就可能会出现这种情况：个别 js 之类的东西特别慢，即使我们想要定位的元素早就已经加载完成了，程序仍然会继续等待，直到整个页面加载完成或时间截止，然后执行下一步。

注意：隐式等待值的设置对 WebDriver 的整个生命周期有效，所以只要设置一次即可，不需要像 time.sleep() 在每个地方都进行设置。

##### 2.3.3 显式等待

  显式等待是在代码中定义等待一定条件发生后再进一步执行你的代码。通过 WebDriverWait 结合 ExpectedCondition 实现。

  实现逻辑是：程序每隔 XX 秒判断一下设定的条件，如果条件成立，则执行下一步；否则继续等待，直到超过设置的最长时间，然后抛出超时异常。显示等待包含了判断条件和最长等待时间。

  实现步骤：首先初始化一个 WebDriverWait 实例；然后调用 until() 或 until_not()。

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://android.myapp.com/myapp/search.htm?kw=QQ'
driver.get(url)
try:
 # 判断类名为 installBtn 的元素是否被添加在 dom 树里面（并不代表该元素一定可见）
 # 间隔 0.5 秒进行一次判断，直到条件成立或超过 10 秒。
 element = WebDriverWait(driver, 10).until(
 EC.presence_of_element_located((By.CLASS_NAME, 'installBtn')))
 print(element.get_attribute('appname'))
finally:
 driver.quit()
```

| 参数                 | 说明                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| driver             | WebDriver 实例                                                                                                       |
| timeout            | 超时时间，等待的最长时间                                                                                                       |
| poll_frequency     | 调用 until() 或 until_not() 中的方法的间隔时间，默认是0.5秒                                                                         |
| ignored_exceptions | 忽略的异常，如果在调用 until() 或 until_not() 的过程中抛出这个元组中的异常，则不中断代码，继续等待，如果抛出的是这个元组外的异常，则中断代码，抛出异常。默认只有NoSuchElementException。 |

  until() 表示预期条件成立，until_not() 表示预期条件不成立。它们的参数一样，说明如下：

| 参数      | 说明                         |
| ------- | -------------------------- |
| method  | 期望的条件，即在等待期间，每个一段时间被调用的方法  |
| message | 如果超时，抛出超时异常，将 message 传入异常 |

  expected_conditions 模块提供了一组预定义的条件给 WebDriverWait 使用（即可作为 until() 或 until_not() 中的 method 参数）：

presence_of_element_located    某元素出现在 DOM 树里面（不表示其是可见的），如果存在的话，返回单个元素
presence_of_all_elements_located    某类元素出现在 DOM 树里面（不表示其是可见的），如果存在的话，返回的是一个 list
text_to_be_present_in_element    某个元素文本包含某文字
text_to_be_present_in_element_value    某个元素的值包含某文字
element_to_be_clickable    某元素是可见的，并且可点击
element_to_be_selected    某元素是可选择的
element_located_selection_state_to_be    定位某元素，判断某元素的选中状态是否等于给定的值
element_located_to_be_selected    定位某元素，判断是否被选中
element_selection_state_to_be    某元素的选中状态是否等于给定的值，可以用来判断选中或没选中

#### 2.4 操作元素

##### 2.4.1 元素基础操作

  一般来说，webdriver 中比较常用的操作元素的方法有下面几个：

| 方法              | 说明                   |
| --------------- | -------------------- |
| text            | 属性值，元素的文本            |
| tag_name        | 属性值，元素的标签名           |
| size            | 属性值，元素的大小            |
| click()         | 点击元素                 |
| send_keys()     | 在元素上模拟按键输入           |
| submit()        | 提交元素的内容，如果可以的话       |
| clear()         | 清除元素的内容，如果其是一个文本输入元素 |
| is_enabled()    | 元素当前是否处于 enable 状态   |
| is_selected()   | 元素当前是否处于被选中状态        |
| get_attribute() | 获取元素的属性值             |
| get_property()  | 获取元素的属性值             |

参考代码：

```
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)

#定位“百度一下”的 button

search_btn = driver.find_element_by_id('su')

# 获取 button 元素的标签名和大小

print('tagName = {}, size = {}'.format(
 search_btn.tag_name, search_btn.size))

# 获取 button 的enable 和选中状态

print('Enabled = {}, Selected = {}'.format(
 search_btn.is_enabled(), search_btn.is_selected()))

# 获取 button 的类名属性

print('Class name = {}'.format(search_btn.get_attribute('class')))

# 定位搜索的输入框

search_input = driver.find_element_by_id('kw')

# 清除输入框中的内容

search_input.clear()

# 在输入框中模拟输入字符 “Selenium”

search_input.send_keys('Selenium')

# 执行搜索，有以下三种方法：
# a. 在输入框中模拟输入 “Enter” 按键
# search_input.send_keys(Keys.ENTER)
# b. 提交输入框的内容
# search_input.submit()
# c. 点击“百度一下” button
search_btn.click()
```

在某些情况下，我们可能需要模拟输入组合键，参考代码如下：

```
#ctrl+a 全选输入框内容 
search_input.send_keys(Keys.CONTROL,'a')
```

##### 2.4.2 填写表格（选择操作）

  现在我们已经了解到可以通过 send_keys() 向文本框中输入文字，但是其他元素呢？我们可以对元素一个个进行单独操作，这不是一个好的方法。因此 WebDriver 提供了一个叫 Select 的类，可以完成这些操作。

options    属性，所有选择项
all_selected_options    属性，所有被选中的选择项
first_selected_option    属性，第一个被选中的选择项
select_by_value()    通过值选择对应选项
select_by_index()    通过索引选择对应选项
select_by_visible_text()    通过文本内容选择对应选项
deselect_all()    清除所有选择。仅当支持多选时有效
deselect_by_value()    通过值取消选择对应选项
deselect_by_index()    通过索引取消选择对应选项
deselect_by_visible_text()    通过文本内容取消选择对应选项
  参考代码：

```
from selenium import webdriver 
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
```

##### 2.4.3 鼠标和键盘操作

  WebDriver 通过 ActionChains 类提供了一些鼠标和键盘操作相关的方法：

方法    说明
perform()    执行所有存储在 ActionChains 中的操作
reset_actions()    清除所有存储在 ActionChains 中的操作
click()    在指定元素上进行点击操作。如果没有指定元素，在当前鼠标所在位置进行点击操作
click_and_hold()    在指定元素上按住鼠标左键
context_click()    在指定元素上进行鼠标右键点击操作。如果没有指定元素，在当前鼠标所在位置进行鼠标右键点击操作
double_click()    在指定元素上进行双击操作。如果没有指定元素，在当前鼠标所在位置进行双击操作
drag_and_drop()    在源元素上按住鼠标左键，然后移动到目标元素上并释放鼠标
drag_and_drop_by_offset()    在源元素上按住鼠标左键，然后移动指定偏移并释放鼠标
key_down()    只发送一个按键，而不释放它。其只能与辅助按键（control、Alt 和 Shift）
key_up()    释放一个辅助按键
move_by_offset()    将鼠标从当前位置按照指定的偏移量进行移动
move_to_element()    将鼠标移动到指定元素的中间
move_to_element_with_offset()    将鼠标移动到指定元素的指定坐标上，元素的左上角坐标为（0, 0）
pause()    暂定指定时间内的所有输入
release()    释放在指定元素上的按住操作
send_keys()    发送按键到当前被 focus 的元素
send_keys_to_element()    发送按键到指定的元素
  参考代码：

```
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)

# 定位“百度一下”的 button

search_btn = driver.find_element_by_id('su')

# 定位搜索的输入框

search_input = driver.find_element_by_id('kw')

# 首先，向文本输入框中模拟输入“Selenium”；

# 然后，点击“百度一下”按钮，开始进行搜索

ActionChains(driver)\
 .send_keys_to_element(search_input, 'Selenium')\
 .click(search_btn)\
 .perform()
```

#### 2.5 操作浏览器

##### 2.5.1 浏览器基础操作

  WebDriver 提供了一些操作浏览器的基本方法：

方法    说明
minimize_window()    最小化当前窗口
maximize_window()    最大化当前窗口
set_window_size()    设置当前窗口的大小
back()    控制浏览器后退
forward()    控制浏览器前进
refresh()    刷新当前页面
close()    关闭当前窗口，只关闭单个窗口
quit()    退出相关的驱动程序和关闭所有窗口
  参考代码如下：

```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

# 最大化当前窗口
driver.maximize_window()
# 最小化当前窗口
driver.minimize_window()
# 设置当前窗口的宽度为 1080，高度为 800，单位为像素
driver.set_window_size(1080, 800)

# 控制浏览器后退
driver.back()
# 控制浏览器前进
driver.forward()

# 刷新当前页面
driver.refresh()

# 关闭当前窗口
driver.close()
# 退出相关的驱动程序和关闭所有窗口
driver.quit()
```

##### 2.5.2 Frame 切换

  在 Web 应用中会遇到 frame/iframe 表单嵌套页面的情况，WebDriver 只能在一个页面上对元素识别与定位，对于 frame/iframe 表单嵌套页面上的元素无法直接定位。WebDriver 提供了如下方法来进行 frame/iframe 之间的切换：

方法    说明
switch_to.frame()    切换到指定的 frame/iframe
switch_to.default_content()    切换到默认的 frame/iframe

##### 2.5.3 窗口切换

  在浏览器操作过程中，会存在多个窗口的情况，这时就需要进行窗口切换。WebDriver 提供了如下方法：

方法    说明
current_window_handle    属性，获取当前窗口的句柄
window_handles    属性，获取当前会话中的所有窗口句柄
switch_to.window()    切换到指定句柄的窗口
  参考代码：

```
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)

# 获取当前窗口句柄

main_window = driver.current_window_handle

# 点击“关于百度”

link = driver.find_element_by_link_text('关于百度').click()

# driver.window_handles 可以获取当前会话中的所有窗口句柄

for handle in driver.window_handles:
 if handle != main_window:
 # 切换到指定句柄的窗口
 driver.switch_to.window(handle)
 break
```

##### 2.5.4 操作弹窗

  WebDriver 提供了对弹窗的处理。具体做法：首先，使用 WebDriver.switch_to.alert 获取到弹窗；然后，使用 text、accept()、dismiss() 和 send_keys() 等方法进行操作。

方法    说明
text    属性，返回弹窗中的文字信息
accept()    接受现有弹框
dismiss()    取消现有弹框
send_keys()    发送文本至弹框
  参考代码：

```
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)

#鼠标悬停至“设置”链接

link = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置

driver.find_element_by_link_text("搜索设置").click()

time.sleep(2)

# 保存设置

driver.find_element_by_link_text("保存设置").click()
time.sleep(2)

# 获取弹框的文本

print(driver.switch_to.alert.text)

# 接受弹框

driver.switch_to.alert.accept()

# 取消弹框

# driver.switch_to.alert.dismiss()
```
