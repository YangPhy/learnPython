## Python进阶02: 文本文件的输入输出

Python具有基本的文本文件读写功能。Python的标准库提供有更丰富的读写功能。

文本文件的读写主要通过open()所构建的文件对象来实现:[Example](filesIO.py)

### 创建文件对象
我们打开一个文件，并使用一个对象来表示该文件：
```
f = open(文件名，模式)
```
最常用的模式有：
```
"r"     # 只读
“w”     # 写入
```
比如
```
>>>f = open("test.txt","r")
```

### 文件对象的方法
读取：
```
content = f.read(N)          # 读取N bytes的数据
content = f.readline()       # 读取一行
content = f.readlines()      # 读取所有行，储存在列表中，每个元素是一行。
```
写入
```
f.write('I like apple')      # 将'I like apple'写入文件
```
关闭文件：
```
f.close()
```
### Summary
```
f = open(name, "r")
line = f.readline()
f.write('abc')
f.close()
```




