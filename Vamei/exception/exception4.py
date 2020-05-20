def test_func():
    try:
        m=1/0
    except NameError:
        print('Catch NameError in the sub-function')

try:
    test_func()
except ZeroDivisionError:
    print('Catch error in the main program')

