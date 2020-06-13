# define class
class Me(object):
    def test(self):
        print("Hello!")

def new_test():
    print ("New Hello!")

me=Me()


print('hasattr(me, "test")=',hasattr(me, "test")) 
print('getattr(me,"test")=',getattr(me,"test"))

# set test to be new_test
print('setattr(me,"test",new_test)=',setattr(me,"test",new_test))
print('getattr(me,"test")=',getattr(me,"test"))

# delete test
delattr(me,"test")
print('hasattr(me, "test")=',hasattr(me, "test")) 
print('getattr(me,"test")=',getattr(me,"test"))

print('isinstance(me,Me)=',isinstance(me,Me))
print('issubclass(Me,object)=',issubclass(Me,object))
