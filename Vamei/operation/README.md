## Python基础04: 运算
Python的运算符和其他语言类似

（我们暂时只了解这些运算符的基本用法，方便我们展开后面的内容，高级应用暂时不介绍）

### 数学运算
```
>>>print 1+9        # 加法
>>>print 1.3-4      # 减法
>>>print 3*5        # 乘法
>>>print 4.5/1.5    # 除法
>>>print 3**2       # 乘方     
>>>print 10%3       # 求余数
```

### 判断
```
>>>print 5==6               # =， 相等
>>>print 8.0!=8.0           # !=, 不等
>>>print 3<3, 3<=3          # <, 小于; <=, 小于等于
>>>print 4>5, 4>=0          # >, 大于; >=, 大于等于
>>>print 5 in [1,3,5]       # 5是list [1,3,5]的一个元素
```
（还有is, is not等, 暂时不深入）

### 逻辑运算
```
>>>print True and True, True and False      # and, “与”运算， 两者都为真才是真
>>>print True or False                      # or, "或"运算， 其中之一为真即为真
>>>print not True                           # not, “非”运算， 取反
```