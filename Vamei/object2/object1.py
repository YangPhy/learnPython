# Define a class named "Bird"
class Bird(object):
    have_feather=True
    way_of_reproduction='egg'
    def move(self,dx,dy):
        position=[0,0]
        position[0]=position[0]+dx
        position[1]=position[1]+dy
        return position

class happyBird(Bird):
    def __init__(self,more_words):
        print ('We are happy birds.',more_words)

summer = happyBird('Hail to Pitt !')

