class Human(object):
    def __init__(self,input_gender):
        self.gender=input_gender
    def printGender(self):
        print(self.gender)


li_lei=Human('male')
print(li_lei.gender)
li_lei.printGender()

# Initialize han_meimei as male
han_meimei=Human('male')
print(han_meimei.gender)
# What if he did a transfer to female ?
han_meimei.gender='female'
han_meimei.printGender()
# Does han_meimei's transfer affect li_lei ?
li_lei.printGender()
