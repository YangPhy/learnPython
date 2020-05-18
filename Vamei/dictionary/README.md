## Python进阶01: 词典

进阶教程对基础教程的进一步拓展，说明Python的细节。希望在进阶教程之后，你对Python有一个更全面的认识。

之前我们说了，列表是Python里的一个类。一个特定的表，比如说nl = [1,3,8]，就是这个类的一个对象。我们可以调用这个对象的一些方法，比如 nl.append(15)。
我们要介绍一个新的类，**词典 (dictionary)**。与列表相似，词典也可以**储存多个元素**。这种储存多个元素的对象称为**容器(container)**。

### 基本概念
常见的创建词典的方法: [Example1](dictionary1.py)
```
>>>dic = {'tom':11, 'sam':57,'lily':100}
>>>print type(dic)
```
词典和表类似的地方，是包含有**多个元素**，每个元素以逗号分隔。但词典的元素包含有两部分，**键**和**值**，常见的是以字符串来表示键，也可以使用数字或者真值来表示键（不可变的对象可以作为键）。值可以是任意对象。键和值两者一一对应。

比如上面的例子中，‘tom’对应11，'sam对应57，'lily'对应100

与表不同的是，词典的元素没有顺序。你不能通过下标引用元素。词典是通过键来引用。
```
>>>print dic['tom']
>>>dic['tom'] = 30
>>>print dic
```
构建一个新的空的词典：
```
>>>dic = {}
>>>print dic
```
在词典中增添一个新元素的方法：
```
>>>dic['lilei'] = 99
>>>print di
```
这里，我们引用一个新的键，并赋予它对应的值。

### 词典元素的循环调用:[Example2](dictionary2.py)
```
dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print dic[key]
```

### 词典的常用方法
```
>>>print dic.keys()           # 返回dic所有的键
>>>print dic.values()         # 返回dic所有的值
>>>print dic.items()          # 返回dic所有的元素（键值对）
>>>dic.clear()                # 清空dic，dict变为{}
>>>del dic['tom']             # 删除 dic 的‘tom’元素
>>>print(len(dic))            # 查询词典中的元素总数
```
