ta=[1,2,3]
tb=[9,8,7]

# cluster
zipped=zip(ta,tb)
print('zip(ta,tb)=',zip(ta,tb))

#decompose
na,nb=zip(*zipped)
print(na,nb)


