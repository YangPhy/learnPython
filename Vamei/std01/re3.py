import re
pattern=re.compile('[0-9]')
m=pattern.match('32dfdf')

print(m)
print(m.group(0))
