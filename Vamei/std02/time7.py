import datetime
t=datetime.datetime(2012,9,1,8,30)
t_next=datetime.datetime(2020,6,18,23,33)
format="output_%Y-%m-%d-%H%M%S.txt"
print(t.strftime(format))
print(t_next.strftime(format))
