def line_conf():
    def line(x):
        return 2*x+1
    return line    # return a function object

my_line=line_conf()
print(my_line(5))
