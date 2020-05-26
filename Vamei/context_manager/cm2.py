# with context manager
with open('new.txt',"w") as f:
    print(f.closed)
    f.write("Hello world!")
print(f.closed)
