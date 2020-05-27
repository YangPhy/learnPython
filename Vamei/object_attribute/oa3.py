class bird(object):
    feather=True

class chicken(bird):
    fly=False
    def __init__(self,age):
        self.age=age
    def getAdult(self):
        if self.age>1.0:
            return True
        else:
            return False
    adult= property(getAdult) #property is built-in

summer=chicken(2)

print(summer.age)
print(summer.adult)
summer.age=0.5
print(summer.age)
print(summer.adult)
