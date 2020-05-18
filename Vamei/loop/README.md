## Python基础06 循环
循环用于重复执行一些程序块。

### for循环

for循环需要预先设定好循环的次数(n)，然后执行隶属于for的语句n次。

基本构造是
```
for 元素 in 序列: 
    statement
```

举例来说，我们编辑一个叫[forDemo.py](forDemo.py)的文件
```
for a in [3,4.4,'life']:
    print a
```
这个循环就是每次从表[3,4.4,'life'] 中取出一个元素（回忆：表是一种序列），然后将这个元素赋值给a，之后执行隶属于for的操作(print)。

#### range()

Python 2写法：
[Example1](loop1.py)
```
idx = range(5)
print idx
```
Python 3写法：
[Example2](loop2.py)
```
idx = list(range(5))
print(idx)
```
× 利用range():
[Example3](loop3.py)
```
for a in range(10):
    print a**2
```

### while循环
while的用法是
```
while 条件:
    statement
```
while会不停地循环执行隶属于它的语句，直到条件为假(False): 
[Example4](loop4.py)
```
i=1
while i < 10:
    print (i)
    i = i + 1
```

### 终端循环
```
continue   # 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作
break      # 停止执行整个循环
```
[Example5](loop5.py): 当循环执行到i = 2的时候，if条件成立，触发continue, 跳过本次执行(不执行print)，继续进行下一次执行(i = 3)。
```
for i in range(10):
    if i == 2: 
        continue
    print i
```
[Example6](loop6.py): 当循环执行到i = 2的时候，if条件成立，触发break, 整个循环停止。
```
for i in range(10):
    if i == 2: 
        break
    print i
```

### Summary
* rang()
* for 元素 in 序列
* while 条件
* continue
* break