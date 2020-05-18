year=int(input('Please input year: '))

def check_leap(year):
    if year % 400 ==0:
        return 'is leap year'
    elif year % 4 ==0 and year % 100 != 0:
        return 'is leap year'
    else:
        return 'is not leap year'

print(year,check_leap(year))






