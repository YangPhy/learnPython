## Python基础09: 面向对象的进一步拓展
我们熟悉了对象和类的基本概念。我们将进一步拓展，以便能实际运用对象和类。

### 调用类的其它信息
上一讲中提到，在定义方法时，必须有self这一参数。这个参数表示某个对象。对象拥有类的所有性质，那么我们可以**通过self，调用类属性**。
```
class Human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print self.laugh
    def laugh_100th(self):
        for i in range(100):
            self.show_laugh()

li_lei = Human()          
li_lei.laugh_100th()
```
* 这里有一个类属性laugh。在方法show_laugh()中，通过self.laugh，调用了该属性的值。
* 还可以用相同的方式调用其它方法。方法show_laugh()，在方法laugh_100th中()被调用。

**通过对象可以修改类属性值。但这是危险的。类属性被所有同一类及其子类的对象共享。类属性值的改变会影响所有的对象。**

### __int__()方法
__init__()是一个特殊方法(special method)。Python有一些特殊方法。Python会特殊的对待它们。特殊方法的特点是名字前后有两个下划线。

如果你在类中定义了__init__()这个方法，创建对象时，Python会自动调用这个方法。这个过程也叫初始化。
```
class happyBird(Bird):
    def __init__(self,more_words):
        print 'We are happy birds.',more_words

summer = happyBird('Happy,Happy!')
```
