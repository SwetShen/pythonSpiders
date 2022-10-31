1. 安装 pip install beautifulsoup4

2. 导入 from bs4 import BeautifulSoup

3. 创建Beautiful Soup对象 soup=BeautifulSoup(html)  
   如果是本地文件 soup=BeautifulSoup(open('index.html'))

4. 格式化输出 print soup.prettify()
   
   四种对象  
   
   4.1 Tag： HTML中的标签及其内容，比如

```bash
print soup.title
print soup.head
print soup.a
print soup.p
```

查看对象类型： print type(soup.a)  
Tag的两个重要属性name和attrs：

```css
print soup.head.name
print soup.p.attrs
print soup.p['class']
```

    4.2 NavigableString：标签内部文字  
如 print soup.p.string  
查看对象类型： print type(soup.p.string)  
    4.3 BeautifulSoup：文档的全部内容，特殊的Tag对象  
    4.4 Comment：特殊类型的NavigableString

5. 遍历文档树  
   5.1 直接子节点

> tag的.contents .children属性  
> .contents返回列表，用索引获取某个特定元素：

```css
print soup.head.contents
print soup.head.contents[0]
```

.children返回列表生成器对象，用遍历获取所有子节点：

```css
print soup.head.children

for child in soup.body.children:
  print child
```

5.2 所有子孙节点

> tag的.descendants属性  
> 类似.children，返回所有子孙节点。  
> 5.3 节点内容  
> tag的.string属性  
> 如果tag内没有或者只有一个子节点，.string方法将返回其内容。

```css
print soup.head.string
print soup.title.string
```

如果tag内包含许多子节点，.string会返回None。

```css
print soup.html.string
```

5.4 多个内容

> tag的.strings和.stripped_strings属性  
> 结果需要遍历获取，.stripped_strings可以去除多余空白内容：

```go
for string in soup.strings:
  print(repr(string))
```

5.5 父节点及全部父节点

> tag的.parent和.parents属性  
> .parents结果需要遍历获取  
> 5.6 兄弟节点和全部兄弟节点  
> tag的.next_sibling, .previous_sibling, .next_siblings, .previous_siblings属性  
> 返回同级兄弟节点，有可能是字符串或者空白。

5.7 前后节点和全部前后节点

> tag的.next_element, .previous_element, .next_elements, .previous_elements属性  
> 返回前后节点，忽略级别关系。

6. 搜索文档树  
   6.1 find_all(name,attrs,recursive,text,**kwargs)  
   返回列表。  
   6.1.1 name  
   A.字符串： soup.find_all('b')  
   B.正则表达式

```dart
import re
for tag in soup.find_all(re.compile('^b')):
  print tag.name
```

C. 列表： soup.find_all(['a','b'])  
D. True: 返回所有tag但不包括字符串节点  
E. 方法

```python
def has_class_but_no_id(tag):
  return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_Id)
```

6.1.2 attrs

```ruby
soup.find_all(id='link2')
soup.find_all(href=re.compile('elsie'))
soup.find_all(href=re.compile('elsie'),id='link1')
soup.find_all('a',class_='sister')
```

6.1.3 recursive  
默认True，返回所有子孙节点。recursive=False只返回直接子节点  
6.1.4 text

```bash
soup.find_all(text='Elsie')
soup.find_all(text=['Tillie','Elsie','Lacie'])
soup.find_all(text=re.compile('Dormouse'))
```

6.1.5 limit  
限制返回结果数： soup.find_all('a',limit=2)

7. find(name,attrs,recursive,text,**kwargs)  
   返回第一个匹配结果。其他与find_all类似
8. CSS选择器

> soup.select() 返回列表。可以在遍历后，使用get_text()获得其内容  
> 8.1 基本选择器：标签名，类名，id名

```go
print soup.select('title')
print soup.select('.a')
print soup.select('#link1')
```

8.2 组合选择器

```go
print soup.select('p #link1')
print soup.select('head>title')
```

8.3 获取内容  
在遍历输出后，使用get_text()方法获取内容。

```go
print soup.select('title')[0].get_text()
for title in soup.select('title'):
  print title.get_text()
```
