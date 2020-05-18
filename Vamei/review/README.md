## Python基础10: 反过头来看看

从最初的“Hello World”，走到面向对象。该回过头来看看，教程中是否遗漏了什么。

我们之前提到一句话，"Everything is Object". 那么我们就深入体验一下这句话。


需要先要介绍两个内置函数，dir()和help()
dir()用来查询一个类或者对象所有属性。你可以尝试一下
```
>>>print dir(list)
```
help()用来查询的说明文档。你可以尝试一下
```
>>>print help(list)
```
(list是Python内置的一个类，对应于我们之前讲解过的列表)


### list一个类
在上面以及看到，表是Python已经定义好的一个类。当我们新建一个表时，比如：
```
>>>nl = [1,2,5,3,5]
```
实际上，nl是类list的一个对象。

实验一些list的方法：
```
>>>print nl.count(5)       # 计数，看总共有多少个5
>>>print nl.index(3)       # 查询 nl 的第一个3的下标
>>>nl.append(6)            # 在 nl 的最后增添一个新元素6
>>>nl.sort()               # 对nl的元素排序
>>>print nl.pop()          # 从nl中去除最后一个元素，并将该元素返回。
>>>nl.remove(2)            # 从nl中去除第一个2
>>>nl.insert(0,9)          # 在下标为0的位置插入9
```
总之，list是一个类。每个列表都属于该类。


### 运算符是特殊方法:[Example](review.py)
使用dir(list)的时候，能看到一个属性，是\__add\__()。从形式上看是特殊方法（下划线，下划线）。它特殊在哪呢？
这个方法定义了"+"运算符对于list对象的意义，两个list的对象相加时，会进行的操作。
```
>>>print [1,2,3] + [5,6,9]
```
运算符，比如+, -, >, <, 以及下标引用[start:end]等等，从根本上都是定义在类内部的方法。

尝试一下
```
>>>print [1,2,3] - [3,4]
```
会有错误信息，说明该运算符“-”没有定义。现在我们继承list类，添加对"-"的定义
```
class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]        
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1,2,3]) - superList([3,4])
```
内置函数len()用来返回list所包含的元素的总数。内置函数__sub__()定义了“-”的操作：从第一个表中去掉第二个表中出现的元素。如果__sub__()已经在父类中定义，你又在子类中定义了，那么子类的对象会参考子类的定义，而不会载入父类的定义。任何其他的属性也是这样。






