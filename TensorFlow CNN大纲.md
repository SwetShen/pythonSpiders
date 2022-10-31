### 一、环境安装

#### 1.1python环境安装

配置环境变量

更换源

#### 1.2 Anaconda(jupyter note) 或者 Pycharm

      anaconda下载地址 https://www.anaconda.com

​      Pycharm 下载地址

anaconda是python 人工智能以及数学处理等学科研究的工具，主要集成了大量的插件库，用于解决和研究各种现实问题提供了条件，但不适合python应用开发，且不具备生产力。

Pycharm 是JetBrains研发的软件，目前市面上的主流生产开发软件，旗下有Intellij IDEA（Java）、Webstorm(前端开发)、AndroidStudio(Andorid开发)...等等，但在图表显示上逊色于anaconda，不适合逐步研究问题。

#### 1.3 numpy与pandas

​        1.2.1 关于numpy

​        1.2.2 关于pandas

#### 1.4 matplotlib

​        简单的图表绘制

```
plt.plot(inputX,outputY,'ro',label="XY")
plt.xlabel('inputx')
plt.ylabel('outputY')
plt.title('inputX and outputY')
```

#### 1.5 tensorflow

​        1.5.1关于tensorflow

### 二、python基础学习

#### 2.1Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。

Python 由 Guido van Rossum 于 1989 年底发明，第一个公开发行版发行于 1991 年。

官方宣布，2020 年 1 月 1 日， 停止 Python 2 的更新。

Python 2.7 被确定为最后一个 Python 2.x 版本。

因此我们采用最新版本的python作为开发环境

#### 2.2  HelloWorld

```python
print("Hello, World!")
```

#### 2.3 变量类型

​    2.3.1 变量赋值

```python
# -*- coding: UTF-8 -*-

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name
```

​    2.3.2 标准数据类型

```
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
```

​    2.3.4 数字

指定一个值时，Number 对象就会被创建

```pyhton
a = 1
b = 10
```

del语句可以删除一些对象的引用

```python
del a
del a,b
```

Python支持四种不同的数字类型：

- int（有符号整型）
- long（长整型，也可以代表八进制和十六进制）
- float（浮点型）
- complex（复数)

```
a = 10 int整数
b = 51924361L 长整型
c = 15.20 浮点型
d = 32.3e+18 科学进制浮点数
```

​    

​    2.3.5 字符串

```
a = "runoob"
```

python的字串列表有2种取值顺序:

- 从左到右索引默认0开始的，最大范围是字符串长度少1
- 从右到左索引默认-1开始的，最大范围是字符串开头

<img src="D:\_MARK_DOWN\image-20220310100643766.png" alt="image-20220310100643766" style="zoom:50%;" />

```python
s = 'abcdef'
s[1:5]
'bcde'
```

<img src="D:\_MARK_DOWN\image-20220310100821074.png" alt="image-20220310100821074" style="zoom:50%;" />

```
# -*- coding: UTF-8 -*-

str = 'Hello World!'

print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第六个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串
```

​    2.3.6 列表

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用 **[ ]** 标识，是 python 最通用的复合数据类型。

列表中值的切割也可以用到变量 **[头下标:尾下标]** ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

```PYTHON
# -*- coding: UTF-8 -*-

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表
```

​    2.3.7 元组

元组是另一个数据类型，类似于 List（列表）。

元组用 **()** 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

```PYTHON
# -*- coding: UTF-8 -*-

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第四个（不包含）的元素 
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组
```

​    2.3.8 字典

字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

```python
# -*- coding: UTF-8 -*-

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}


print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值
```

​        2.3.9 数据类型转换

| 函数                     | 描述                              |
|:---------------------- |:------------------------------- |
| int(x [,base\])        | 将x转换为一个整数                       |
| long(x [,base\] )      | 将x转换为一个长整数                      |
| float(x)               | 将x转换到一个浮点数                      |
| complex(real [,imag\]) | 创建一个复数                          |
| str(x)                 | 将对象 x 转换为字符串                    |
| repr(x)                | 将对象 x 转换为表达式字符串                 |
| eval(str)              | 用来计算在字符串中的有效Python表达式,并返回一个对象   |
| tuple(s)               | 将序列 s 转换为一个元组                   |
| list(s)                | 将序列 s 转换为一个列表                   |
| set(s)                 | 转换为可变集合                         |
| dict(d)                | 创建一个字典。d 必须是一个序列 (key,value)元组。 |
| frozenset(s)           | 转换为不可变集合                        |
| chr(x)                 | 将一个整数转换为一个字符                    |
| unichr(x)              | 将一个整数转换为Unicode字符               |
| ord(x)                 | 将一个字符转换为它的整数值                   |
| hex(x)                 | 将一个整数转换为一个十六进制字符串               |
| oct(x)                 | 将一个整数转换为一个八进制字符串                |

#### 2.4 条件语句

​    2.4.1if...else 语句

```
flag = False
name = 'luren'
if name == 'python':         # 判断变量是否为 python 
    flag = True              # 条件成立时设置标志为真
    print 'welcome boss'     # 并输出欢迎信息
else:
    print name               # 条件不成立时输出变量名称
```

​    2.4.2 if...elif

```
num = 5     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出
```

​    注意：python没有switch语句

#### 2.5 循环语句

​    2.5.1通过数据进行迭代

```
# -*- coding: UTF-8 -*-

for letter in 'Python':     # 第一个实例
   print("当前字母: %s" % letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果: %s'% fruit)

print ("Good bye!")
```

​    2.5.2通过序列索引迭代

```
# -*- coding: UTF-8 -*-

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 : %s' % fruits[index])

print ("Good bye!")
```

#### 2.6 函数

你可以定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号**()**。
- 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None

```python
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

​    2.6.1 open 函数

你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。

语法：

```python
file object = open(file_name [, access_mode][, buffering])
```

各个参数的细节如下：

- file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
- access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
- buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

不同模式打开文件的完全列表：

| 模式  | 描述                                                                                |
|:--- |:--------------------------------------------------------------------------------- |
| t   | 文本模式 (默认)。                                                                        |
| x   | 写模式，新建一个文件，如果该文件已存在则会报错。                                                          |
| b   | 二进制模式。                                                                            |
| +   | 打开一个文件进行更新(可读可写)。                                                                 |
| U   | 通用换行模式（不推荐）。                                                                      |
| r   | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。                                                  |
| rb  | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。                              |
| r+  | 打开一个文件用于读写。文件指针将会放在文件的开头。                                                         |
| rb+ | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。                                     |
| w   | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。                      |
| wb  | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。  |
| w+  | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。                       |
| wb+ | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。   |
| a   | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。       |
| ab  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+  | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。                 |
| ab+ | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。                       |

```python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("foo.txt", "w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
```

##### close()方法

File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。

当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。

语法：

```python
fileObject.close()
```

##### write()方法

write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

write()方法不会在字符串的结尾添加换行符('\n')：

语法：

```
fileObject.write(string)
```

在这里，被传递的参数是要写入到已打开文件的内容。

例子：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("foo.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()
```

##### read()方法

read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

语法：

```python
fileObject.read([count])
```

在这里，被传递的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()
```

### 三、Numpy基础

NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

#### 3.1 使用pip安装

```
pip install --user numpy scipy matplotlib
```

#### 3.2 ndarray

NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。

```
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

| 名称     | 描述                             |
|:------ |:------------------------------ |
| object | 数组或嵌套的数列                       |
| dtype  | 数组元素的数据类型，可选                   |
| copy   | 对象是否需要复制，可选                    |
| order  | 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认） |
| subok  | 默认返回一个与基类类型一致的数组               |
| ndmin  | 指定生成数组的最小维度                    |

```python
import numpy as np 
a = np.array([1,2,3])  
print (a)
```

```
# 多于一个维度  
import numpy as np 
a = np.array([[1,  2],  [3,  4]])  
print (a
```

```
# 最小维度  
import numpy as np 
a = np.array([1, 2, 3, 4, 5], ndmin =  2)  
print (a)
```

```
# dtype 参数  
import numpy as np 
a = np.array([1,  2,  3], dtype = complex)  
print (a)
```

#### 3.3 ndarray.shape

```
import numpy as np  

a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)
```

```
import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) 
a.shape =  (3,2)  
print (a)
```

```
import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2)  
print (b)
```

#### 3.4 Numpy创建数据

3.4.1 empty 创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组

```
numpy.empty(shape, dtype = float, order = 'C')
```

参数说明：

| 参数    | 描述                                         |
|:----- |:------------------------------------------ |
| shape | 数组形状                                       |
| dtype | 数据类型，可选                                    |
| order | 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

```
import numpy as np 
x = np.empty([3,2], dtype = int) 
print (x)
```

3.4.2 zeros 创建指定大小的数组，数组元素以 0 来填充：

```
numpy.zeros(shape, dtype = float, order = 'C')
```

参数说明：

| 参数    | 描述                                   |
|:----- |:------------------------------------ |
| shape | 数组形状                                 |
| dtype | 数据类型，可选                              |
| order | 'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组 |

```
import numpy as np

# 默认为浮点数
x = np.zeros(5) 
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype = np.int) 
print(y)

# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)
```

3.4.3 ones 创建指定形状的数组，数组元素以 1 来填充：

```
numpy.ones(shape, dtype = None, order = 'C')
```

参数说明：

| 参数    | 描述                                   |
|:----- |:------------------------------------ |
| shape | 数组形状                                 |
| dtype | 数据类型，可选                              |
| order | 'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组 |

```
import numpy as np

# 默认为浮点数
x = np.ones(5) 
print(x)

# 自定义类型
x = np.ones([2,2], dtype = int)
print(x)
```

**有监督学习**有监督学习的数据集包含了样本x与样本的标签y，算法模型需要学习到映射
fe:x→y，其中fe代表模型函数，为模型的参数。在训练时，通过计算模型的预测值
fe(x)-与真实标签y之间的误差来优化网络参数θ，使得网络下一次能够预测更精准。常见的
有监督学习有线性回归，逻辑回归，支持向量机，随机森林等。
**无监督学习**收集带标签的数据往往代价较为昂贵，对于只有样本x的数据集，算法需要自
行发现数据的模态，这种方式叫做无监督学习。无监督学习中有一类算法将自身作为监督
信号，即模型需要学习的映射为fg:x→x，称为自监督学习(Self-supervised Learning)。在
训练时，通过计算模型的预测值fe(x)与自身x之间的误差来优化网络参数θ。常见的无监督
学习算法有自编码器，生成对抗网络等。
**强化学习**也称为增强学习，通过与环境进行交互来学习解决问题的策略的一类算法。与有
监督、无监督学习不同，强化学习问题并没有明确的“正确的”动作监督信号，算法需要
与环境进行交互，获取环境反馈的滞后的奖励信号，因此并不能通过计算动作与“正确动
作”之间的误差来优化网络。常见的强化学习算法有DQN, PPO等。

### 四、Tensorflow的学习

```
课程：
深度学习经典网络算法、项目实战 

TensorFlow™是一个基于数据流编程（dataflow programming）的符号数学系统，被广泛应用于各类机器学习（machine learning）算法的编程实现，通俗来说，它是一个可以“自我学习”的框架，而框架就是帮助我们简化各项操作的工具。而我们需要做的就是去设计这个内容。

为什么选择tensorflow
1、升级到2.x版本更成熟，相较于1.X更简单，更容易。
2、基本上学术界和开发界，都采用tensorflow。
3、跨平台，具备各种现成的模型库。

之后学习的建议：多看论文，特别是关于ResNet的论文

tensorflow安装有两个版本
CPU版本和 GPU版本（GPU版本除了安装 tensorflow-gpu 还要安装英伟达CUDA）
```

从Tensorflow的名字中有两个概念，一个是Tensor，一个是Flow。

Tensor就是张量，张量在数学和物理学领域都有各自的定义，但本次实验我们的使用与前两者毫无联系。我们可以认为它就是一个n维数组，这个n可以是0，也可以是其他任意数。 

Flow是“流”，它直观地表达了张量与张量之间通过计算相互转化的过程。

Tensorflow 是一个通过计算图的形式来表述计算的编程体系。TensorFlow中的每一个计算都是计算图上的一个节点，而节点之间的边描述了计算之间的依赖

（计算图与GPU运算有很重要关系，本次实验以CPU为主，我们暂时只了解概念。）

#### 4.1 机器学习的流程

```
机器学习流程：
1、数据获取
2、特征工程 （*）
3、建立模型
4、评估与应用

算法实际上的贡献，没有数据更为重要
比方做饭，蔬菜不新鲜，炒菜流程和技术再牛也不能化腐朽为神奇
```

##### 4.1.1 特征工程的作用

```
1、数据特征决定了模型的上限
2、预处理和特征提取是最核心的
3、算法与参数选择决定了如何逼近这个上限
```

#### 4.2 tf基础

```
import tensorflow as tf #导入tensorflow库
import numpy as np #导入numpy库
```

```
#pip3 install django-excel -i https://mirrors.aliyun.com/pypi/simple/ 更换阿里巴巴源
tf.__version__ #查看tensorflow版本
```

简单运算

![image-20220310143942945](D:\_MARK_DOWN\image-20220310143942945.png)

![image-20220310144001145](D:\_MARK_DOWN\image-20220310144001145.png)

![image-20220310144247670](D:\_MARK_DOWN\image-20220310144247670.png)

计算案例

```

```

![image-20220310144640999](D:\_MARK_DOWN\image-20220310144640999.png)

![image-20220310144704587](D:\_MARK_DOWN\image-20220310144704587.png)

#### 4.3 Tensor （张量）

```
tf.Tensor 可以当作是进行GPU加速运算的矩阵就可以
比如：一个数据（0维）、一个数组（一维矩阵）、一个二维矩阵、一个三维矩阵，甚至思维矩阵 都可以是一个Tensor
（也就是将现实中所有的问题或者数据，进行矩阵化）
```

张量的计算

tf.constant 是一个计算，这个计算的结果为一个张量，保存在变量中

```
import tensorflow as tf
a = tf.constant([1.0,2.0],name="a")
b = tf.constant([2.0,3.0],name="b")
result = tf.add(a,b,name="add") 
```

构建张量的结构也仅需三个属性 :名字(name)、维度(shape)、类型(type)

#### 4.4 Tensorflow实现神经网络

神经网络部分我们主要讲解四个点：

1、通过游乐场来介绍神经网络的主要功能和计算流程

2、前向传播（forward-propagation）

3、通过Tensorflow变量表达神经网络参数

4、反向传播（back-propagation）

#### 4.5 游乐场模型

| 参数名                 | 描述               |
| ------------------- | ---------------- |
| Epoch               | 训练次数             |
| Learning rate       | 学习率（数据量增多，学习率越小） |
| activation          | 激活函数             |
| regularization      | 正则化              |
| regularization rate | 正则化概率            |
| problem type        | 处理问题种类           |
| data                | 数据               |
| features            | 数据特征             |
| hidden layers       | 隐藏层              |
| output              | 输出层              |
|                     |                  |

#### 4.6 前向传播

前向传播有几个重要的部分：特征值、权重值、隐藏层、损失函数、归一化

<img src="D:\_MARK_DOWN\image-20220321100214373.png" alt="image-20220321100214373" style="zoom:50%;" />

1）特征值（x1,x2）

如果我们要判断一个零件是否合格，那么我们需要选取一些可以影响到合格性的指标,比如在这里我们途中所描述的零件长度、零件质量。（而且这些特征都必须用数值来表示）

下面我们可以举例说明特征

2）权重值（w）：

权重值,又称权重初始值，关系到神经网络是否能学习成功，当激活函数使用**ReLu时**，权重的初始值使用**He初始值**；当激活函数为**Sigmoid或tanh时**等S型曲线函数时，初始值使用**Xavier初始值**， 总之这是自动生成的。（人为定义有较大概率会造成训练模型的过拟合）

<img src="D:\_MARK_DOWN\image-20220321101622703.png" alt="image-20220321101622703" style="zoom:50%;" />

计算过程：

<img src="D:\_MARK_DOWN\image-20220321101446050.png" alt="image-20220321101446050" style="zoom:50%;" />

3）隐藏层( 得分函数 )

tensorflow中一个概念叫做计算图，描述的重点是，在神经网络中，我们将每一个运算的过程都看作一个节点。这里的a11,a12,a13 就是节点。（或者叫作神经元）而 a11,a12,a13 所在的一层被叫做隐藏层（hidden layer 又被叫做一个Dense（全连接层））

![image-20220321102041973](D:\_MARK_DOWN\image-20220321102041973.png)

上述公式，是由特征节点中 “特征值*权重值”的和

最终我们计算的和为：

![image-20220321102420421](D:\_MARK_DOWN\image-20220321102420421.png)

上述的整个过程，我们可以把x1、x2 看作一个1 x 2 的矩阵 x = [x1, x2]

而将W看作是一个2 x 3的矩阵

<img title="" src="file:///D:/_MARK_DOWN/image-20220321102554750.png" alt="image-20220321102554750" style="zoom:50%;" width="226">

这样我们通过矩阵乘法可以得到隐藏层的三个节点组成的向量值：

<img title="" src="file:///D:/_MARK_DOWN/image-20220321102907795.png" alt="image-20220321102907795" style="zoom:50%;" width="427">

输出层：

<img title="" src="file:///D:/_MARK_DOWN/image-20220321103008663.png" alt="image-20220321103008663" style="zoom:50%;" width="448">

4）损失函数

什么是损失函数：

上述得到的结果有好，有不好，如何来衡量这个结果(有多好，有多差...) 具体到数值的差异

就像上学读书考试

<img title="" src="file:///D:/_MARK_DOWN/image-20220321103641276.png" alt="image-20220321103641276" style="zoom:50%;" width="417">

$s_j 错误类别的分值
s_y 正确类别的分值
1 防止损失函数负值差异化
$
举例说明：

| <img src="D:\_MARK_DOWN\image-20220321110347830.png" alt="image-20220321110347830" style="zoom:33%;" /> | <img title="" src="file:///D:/_MARK_DOWN/image-20220321110434141.png" alt="image-20220321110434141" style="zoom:50%;" width="303"> |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |

（可选）损失函数中的正则化 （解决因损失率波动，造成的过拟合）。

![image-20220321115301066](D:\_MARK_DOWN\image-20220321115301066.png)

![image-20220321111103620](D:\_MARK_DOWN\image-20220321111103620.png)

5） 归一化

<img src="D:\_MARK_DOWN\image-20220321111550523.png" alt="image-20220321111550523" style="zoom:50%;" />

将的得分值，进行类别概率化

<img src="D:\_MARK_DOWN\image-20220321111311085.png" alt="image-20220321111311085" style="zoom:33%;" />

<img src="D:\_MARK_DOWN\image-20220321111937828.png" alt="image-20220321111937828" style="zoom: 33%;" />

#### 4.7 反向传播（梯度下降）

![image-20220321114615885](D:\_MARK_DOWN\image-20220321114615885.png)

#### 4.8 激活函数

![image-20220321115621276](D:\_MARK_DOWN\image-20220321115621276.png)

RELU函数可以防止“梯度消失”，做到梯度值逐渐变化。

总结：神经网络在巨量数据分析任务中虽然很强，但是我们做的事情，是希望它不要太强。防止它最终无法达到我们期望的预测，也就是我们说的过拟合，俗称在学习中学傻了。

#### 4.9  神经网络任务案例 - 一元一次线性方程

一元线性回归

先导入我们需要的库

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow.keras
import warnings
warnings.filterwarnings("ignore")
%matplotlib inline
```

1）我们去构建一个计算方程  

$Y = 4X  + 1$

最终的目的是，希望用户随机输入一个X的值，能够预测得到一个值。

2）我们去创造 许多 X  与  Y 的值，来训练这个模型

当然不仅是X 的值是随机的，关于Y的值，我也会让它变得和真实结果有很大的差异。

```
inputX = np.random.rand(1000,1)
noise = np.random.normal(0,0.05,inputX.shape)
outputY = inputX * 4 + 1 + noise
```

3） 通过inputX、outputY绘制一下我们的点图

```
#绘制当前的效果图
plt.plot(inputX,outputY,'ro',label="XY")

plt.xlabel('inputX')
plt.ylabel('inputY')
plt.title('inputX and inputY')
```

4）如果同学们选择了 输入的X的值差异太大，有的-27 ，有的120，我们可以选择对数据预处理，使得它们的值差异没有那么大（这一条是可选的）

这里使用的是K近邻算法

```
from sklearn import preprocessing
input_features = preprocessing.StandardScaler().fit_transform(inputX)
```

5）构建神经网络模型

这里的Sequential() 就是我们需要的神经网络模型，在Tensorflow的API中有许多参数，我们后期要讲解。

```
model = tf.keras.Sequential()
model.add(layers.Dense(8))
model.add(layers.Dense(16))
model.add(layers.Dense(1))
```

6）定义好优化器和损失函数

```
model.compile(optimizer=tf.keras.optimizers.SGD(0.001),loss='mean_squared_error')
```

优化器为我们指定了第一次的w参数

7）

```
model.fit(input_features,outputY,validation_split=0.25,epochs=50,batch_size=50)
```

8）预测这个结果

```
#如果将原来的模型中的输入作为预测值，预测的结果为
predict = model.predict(input_features)
predict.shap
```

9）前后对比图

```
#前后对比效果
plt.plot(inputX,outputY,'ro',label="real Y")
plt.plot(inputX.reshape(-1),predict.reshape(-1),'bo',label="predict Y")

plt.xlabel('inputX')
plt.ylabel('inputY')
plt.title('inputX and inputY')
```

课后作业： 请同学们（修改方程）测试一下 

#### 4.10 神经网络任务案例- 重庆天气预测（多元）

多元线性回归

```
1、分析
```

课后作业，仿照

#### 4.11 神经网络任务案例 -石头剪刀布识别案例

分类任务

```

```

课后作业，男人与女人

### 五、Opencv 案例 -人脸特征识别

安装 pip install opencv-contrib-python

5.1 读取图片

```
import cv2 as cv

img = cv.imread('data/train/1.huge.jpg')
cv.imshow('real_img',img)
cv.waitKey(0)
cv.destroyAllWindows()
```

5.2 灰度转换

```
import cv2 as cv
img = cv.imread('data/train/1.huge.jpg')
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray_img)
cv.imwrite('data/hg/gray_hg.jpg',gray_img)
cv.imshow('real_img',img)
cv.waitKey(0)
cv.destroyAllWindows()
```

5.3 修改尺寸

```
import cv2 as cv
img = cv.imread('data/train/1.huge.jpg')
resize_img = cv.resize(img,dsize=(200,200))
cv.imshow('resize_img',resize_img)
cv.imshow('real_img',img)
# cv.waitKey(0)
while True:
    if ord('q') == cv.waitKey(0):
        break
cv.destroyAllWindows()
```

5.4 绘制矩形

```
import cv2 as cv

img = cv.imread('data/train/1.huge.jpg')
x,y,w,h = 100,100,100,100
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)
cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=5)
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'huge',(100,100),font,1,(255,255,255),2)
cv.imshow('re_img',img)

cv.waitKey(0)
#释放内存
cv.destroyAllWindows()
```

5.5 人脸检测

Haar级联监测

```
#导入cv模块
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

img = cv2.imread('img/xwdsh02.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y + h, x:x + w]
    #在检测到的人脸区域内检测眼睛
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imwrite('img/xwdsh02_detect.jpg',img)
```

SSD检测

```
import cv2

model_file = "dnn_face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel"
config_file = "dnn_face_detector/deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(config_file,model_file)
threshold = 0.9

img = cv2.imread('img/xwdsh01.jpg')
frameHeight = img.shape[0]
frameWidth = img.shape[1]

blob = cv2.dnn.blobFromImage(img,1.0,(300,300),[104,117,123],False,False)

net.setInput(blob)
detections = net.forward()

for i in range(detections.shape[2]):
    detection_score = detections[0,0,i,2]
    if detection_score > threshold:
        x1 = int(detections[0,0,i,3]*frameWidth)
        y1 = int(detections[0,0,i,4]*frameHeight)
        x2 = int(detections[0,0,i,5]*frameWidth)
        y2 = int(detections[0,0,i,6]*frameHeight)
        #绘制矩形
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
cv2.imwrite('img/xwdsh01_ssd_detect.jpg',img)
```

cv2.dnn.blobFromImage

image:输入图像（1、3或者4通道）


可选参数：

scalefactor:图像各通道数值的缩放比例
size:输出图像的空间尺寸,如size=(200,300)表示高h=300,宽w=200
mean:用于各通道减去的值，以降低光照的影响(e.g. image为bgr3通道的图像，mean=[104.0, 177.0, 123.0],表示b通道的值-104，g-177,r-123)
swapRB:交换RB通道，默认为False.(cv2.imread读取的是彩图是bgr通道)
crop:图像裁剪,默认为False.当值为True时，先按比例缩放，然后从中心裁剪成size尺寸
ddepth:输出的图像深度，可选CV_32F 或者 CV_8U.


5.6 多人脸识别

```
#导入cv模块
import cv2 as cv
#检测函数
def face_detect_demo():
    gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gary)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

#读取图像
img = cv.imread('data/leijun.jpg')
#检测函数
face_detect_demo()

cv.waitKey(0)
#释放内存
cv.destroyAllWindows()
```

5.7 摄像头检测

```
import cv2 as cv
#检测函数
def face_detect_demo(img):
    gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gary)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

#读取摄像头
cap = cv.VideoCapture(0)
#循环
while True:
    flag,frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(1):
        break
#释放内存
cv.destroyAllWindows()
#释放摄像头
cap.release()
```

5.8 拍照保存

```
import cv2
#摄像头
cap=cv2.VideoCapture(0)

num = 3

while(cap.isOpened()):#检测是否在开启状态
    ret_flag,Vshow = cap.read()#得到每帧图像
    cv2.imshow("Capture_Test",Vshow)#显示图像
    k = cv2.waitKey(1) & 0xFF#按键判断
    if k == ord('s'):#保存
       cv2.imwrite("data/train/"+str(num)+".shen"+".jpg",Vshow)
       print("success to save"+str(num)+".jpg")
       print("-------------------")
       num += 1
    elif k == ord(' '):#退出
        break
#释放摄像头
cap.release()
#释放内存
cv2.destroyAllWindows()
```

5.9 训练数据

```
import os
import cv2
import sys
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    facesSamples=[]
    ids=[]
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #检测人脸
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
    #打印数组imagePaths
    print('数据排列：',imagePaths)
    #遍历列表中的图片
    for imagePath in imagePaths:
        #打开图片,黑白化
        PIL_img=Image.open(imagePath).convert('L')
        #将图像转换为数组，以黑白深浅
       # PIL_img = cv2.resize(PIL_img, dsize=(400, 400))
        img_numpy=np.array(PIL_img,'uint8')
        #获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
        #获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])
        #预防无面容照片
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
        #打印脸部特征和id
        #print('fs:', facesSamples)
        print('id:', id)
        #print('fs:', facesSamples[id])
    print('fs:', facesSamples)
    #print('脸部例子：',facesSamples[0])
    #print('身份信息：',ids[0])
    return facesSamples,ids

if __name__ == '__main__':
    #图片路径
    path='./data/train/'
    #获取图像数组和id标签数组和姓名
    faces,ids=getImageAndLabels(path)
    #获取训练对象
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    #recognizer.train(faces,names)#np.array(ids)
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('trainer/trainer.yml')
    #save_to_file('names.txt',names)
```

5.10 人脸识别

```
import cv2
import os


#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer/trainer.yml')
names=[]
warningtime = 0


#准备识别的图片
def face_detect_demo(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度
    face_detector=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
    face=face_detector.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    #face=face_detector.detectMultiScale(gray)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
        # 人脸识别
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        #print('标签id:',ids,'置信评分：', confidence)
        if confidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
               # warning()
               warningtime = 0
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('result',img)
    #print('bug:',ids)

def name():
    path = './data/train/'
    #names = []
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
       name = str(os.path.split(imagePath)[1].split('.',2)[1])
       names.append(name)


#摄像头
cap=cv2.VideoCapture(0)

name()
while True:
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):
        break
cv2.destroyAllWindows()
cap.release()
#print(names)
```

数据获取： 

1、benchmark 是一个行业的基准（数据库，论文，源码，结果）

```
http://shuoyang1213.me/WIDERFACE/
```

2、优秀论文，通常实验阶段都会介绍它所使用的数据集，公开数据集可以下载。申请数据集的时候，最好使用学校的邮箱。

3、论坛或者交流社区，比如thinkface

4、数据规模，越大越好 本次实验是2W多数据

二分类数据，第一类人脸，第二类非人脸。                                                                                                      

对于正样本：裁剪的操作，根据标注的坐标把人脸裁剪出来。可以使用opencv这个工具，来完成制作人脸数据。要检查一下，看一看数据有没有问题。

iou 图像 重叠比率 比如<0.2  0.2~0.8  > 0.8

对于负样本：进行一个随机的裁剪，IOU这个比例（重叠的比例）在原始的数据当中IOU<0.3认为是一个负样本。

制作LMDB数据源，（其实它呼吁事故caffe支持的非常常用的分类的数据源）

编写两个txt文档文件

train.txt

```
0/xxx.jpg 0
1/xxx.jpg 1
```

val.txt

```
xxx.jpg 0
xxx.jpg 1
```

5.2 
