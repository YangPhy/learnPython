def line_conf():
    def line(x):
        return 2*x+1
    print(line(5)) #within the scope

line_conf()
print(line(5))  # out of the scope
