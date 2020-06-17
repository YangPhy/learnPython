import re
import datetime
file_name='output_1981.10.21.txt'
m=re.search("output_(?P<year>\d{4}).(?P<month>\d{2}).(?P<date>\d{2})",file_name)
# Method 1, change str to int and out put
yy=int(m.group("year"))
mm=int(m.group("month"))
dd=int(m.group("date"))
t=datetime.datetime(yy,mm,dd)
print(t.weekday())
new_file_name='output_'+str(yy)+'-'+str(mm)+'-'+str(dd)+'-'+str(t.weekday())
print("new_file_name is",new_file_name)

# Method 2
week=datetime.datetime.strptime(m.group("year")+m.group("month")+m.group("date"),"%Y%m%d").weekday()
new_file_name2='output_'+m.group("year")+'-'+m.group("month")+'-'+m.group("date")+'-'+str(week)
print("new_file_name is",new_file_name2)
