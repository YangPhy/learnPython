re1=map((lambda x:x+3),[1,2,3,4,5,6])

re2=map((lambda x,y: x+y),[1,2,3],[4,5,6])

print(list(re1))
print(list(re2))

