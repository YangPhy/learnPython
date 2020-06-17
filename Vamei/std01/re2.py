import re
str='abcd4ef'
m=re.search('[0-9]',str)
print(m.group(0))

m2=re.match('[0-9]',str)
print(m2)

str2=re.sub('[0-9]','num',str)
print(str2)

#print(help(re.split))
str3='I love you'
print(str3)
split=re.split(' ',str3)
print(split)

str4= re.findall(r"docs","https://docs.python.org/3/whatsnew/3.6.html")
print(str4)
