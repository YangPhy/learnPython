def test(f,a,b):
    print ('test')
    print (f(a,b))

test((lambda x,y:x**2+y),6,9)
