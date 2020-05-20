re=iter(range(5))

try:
    for i in range(100):
        print(re.__next__())
except StopIteration:
    print('here is end',i)
print('HaHaHa')
