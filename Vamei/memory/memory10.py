from sys import getrefcount

a=[1,2,3]
b=a
print(getrefcount(b))

a=1
print(getrefcount(b))
