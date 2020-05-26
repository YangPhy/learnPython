# without context manager
f = open("new.txt","w")
print(f.closed) #whether the file is closed
f.write('Hello, world!')
f.close()
print(f.closed)
