f=open("record.txt","w")
f.write('tom, 12, 86\n')
f.write('Lee, 15, 99\n')
f.write('Lucy, 11, 58\n')
f.write('Joseph, 19, 56\n')
f.close()

g=open("record.txt","r")
print(g.readline())
print(g.readline())
print(g.readline())
print(g.readline())
g.close()



