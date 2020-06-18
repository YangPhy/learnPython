import os.path
path='/home/yang/Downloads/Tree.zip'

print(os.path.exists(path))

print(os.path.getsize(path))
print(os.path.getatime(path))
print(os.path.getmtime(path))

print(os.path.isfile(path))
print(os.path.isdir(path))
