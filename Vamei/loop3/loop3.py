xl=[1,3,5]
yl=[9,12,13]
L=[x**2 for (x,y) in zip(xl,yl) if y> 10]
print(L)
