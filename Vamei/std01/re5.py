import re
m=re.search("output_(?P<year>\d{4})","output_1986.txt")
print(m)
print(m.group(0))
print(m.group("year"))
