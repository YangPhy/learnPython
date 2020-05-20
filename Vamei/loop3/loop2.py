def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print(i)

