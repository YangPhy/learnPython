from datetime import datetime
format="output-%Y-%m-%d-%H%M%S.txt"
str="output-1997-12-23-030000.txt"
t=datetime.strptime(str,format)
print(t)
