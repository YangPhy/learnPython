class bird(object):
    feather=True

class chicken(bird):
    fly=False
    def __init__(self,age):
        self.age=age
    def __getattr__(self,name):
        if name=='adult':
            if self.age> 1.0:
                return True
            else:
                return False
        else:
            raise AttributeError(name)

summer=chicken(2)

print(summer.adult)
summer.age=0.5
print(summer.adult)
#print(summer.male)

