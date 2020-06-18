import os.path
path='/home/yang/doc/file.txt'

print(os.path.basename(path))
print(os.path.dirname(path))


info=os.path.split(path)
print(info)

path2=os.path.join('/','home','yang','file')

p_list=[path,path2]
print(os.path.commonprefix(p_list))

print(os.path.normpath('/home/yang/../.'))
