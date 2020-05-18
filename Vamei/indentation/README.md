## Python基础05: 缩进和选择

### 缩进
Python最具特色的是用缩进来标明成块的代码。我下面以if选择结构来举例。if后面跟随条件，如果条件成立，则执行归属于if的一个代码块。

先看C语言的表达方式（**注意：这是C，不是Python!**）
```
if ( i > 0 )
{
    x = 1;
    y = 2;
}
```
如果i > 0的话，我们将进行括号中所包括的两个赋值操作。括号中包含的就是块操作，它隶属于if。

在Python中，同样的目的，这段话是这样的
```
if i>0:
    x=1
    y=2
```
在Python中， 去掉了i > 0周围的括号，去除了每个语句句尾的分号，表示块的花括号也消失了。多出来了if ...之后的 **:(冒号)**, 还有就是x = 1 和 y =2前面有**四个空格的缩进**。
通过缩进，Python识别出这两个语句是隶属于if。

*Python这样设计的理由纯粹是为了程序好看。*

**初学者（4个空格为语句块缩进）经常犯的错误是tab键和空间键混用，造成的缩进不一致。凡是报错信息看到：IndentationError: unexpected indent ，就是表示缩进不一致。**

### If 语句
写一个完整的程序，命名为[ifDemo.py](ifDemo.py)。这个程序用于实现if结构。
```
i=1
x=1
if i>0:
    x=x+1
print x # This is the Python 2 syntax, in Python 3, we write print(x)
```
```
$python ifDemo.py
```
运行。程序运行到if的时候，条件为True，因此执行x = x+1,。
print x语句没有缩进，那么就是if之外。

这种以**四个空格**的缩进来表示**隶属关系**的书写方式，以后还会看到。强制缩进增强了程序的**可读性**。

#### 复杂一些的 if 选择
对于有多个条件备选的情况，使用
```
if, elif, else
```
引领：[Example1](indentation1.py)
Python检测条件，如果发现if的条件为假，那么跳过后面紧跟的块，检测下一个elif的条件； 如果还是假，那么执行else块。
通过上面的结构将程序分出三个分支。程序根据条件，只执行三个分支中的一个。

#### if的嵌套
整个if可以放在另一个if语句中，也就是if结构的嵌套使用：[Example2](indentation2.py)
```
i=5
if i>1:
    print('i>1')
    print('good')
    if i>1:
        print('i>2')
        print('even better')
```
if i > 2 后面的块相对于该if缩进了四个空格，以表明其隶属于该if，而不是外层的if。

### Summary
* if语句之后的冒号
* 以四个空格的缩进来表示隶属关系, Python中不能随意缩进
```
if  <条件1>:

    statement

elif <条件2>:

    statement

elif <条件3>：

    statement

else:

    statement
```