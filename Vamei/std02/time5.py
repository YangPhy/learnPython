import datetime
t=datetime.datetime(2012,9,1,8,30)
t_next=datetime.datetime(2020,6,18,23,33)
delta1=datetime.timedelta(seconds=600)
delta2=datetime.timedelta(weeks=3)
print(t+delta1)
print(t+delta2)
print(t_next-t)

print(t>t_next)
