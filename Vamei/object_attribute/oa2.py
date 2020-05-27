class bird(object):
    feather=True

class chicken(bird):
    fly=False
    def __init__(self,age):
        self.age=age

summer=chicken(2)

summer.__dict__['age']=3
print(summer.__dict__['age'])

summer.age=5
print(summer.age)
print('summer.__class__=',summer.__class__)
print('chicken.__class__=',chicken.__class__)
print('bird.__base__=',bird.__base__)
