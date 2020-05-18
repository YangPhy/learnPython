## Python基础01: Hello world
### Python命令行
Linux下，在命令行输入
```
$python
```
将直接进入python的交互模式。然后在命令提示符>>>后面输入
```
print ('Hello world!')
```
即可在屏幕上输出 'Hello world!'。
命令行模式可使用
```
quit()
```
进行退出。
（在Python 2.x中，print还可以是一个关键字，可写成print 'Hello World!'，但这在3.x中行不通 ）

### Python程序
创建[helloWorld.py文件](helloWorld.py)，内容为
```
print ('Hello world!')
```
在命令行输入
```
python helloWorld.py
```
运行该程序。

### 脚本
可以将helloWorld.py改写成一个可执行的脚本[hello.py](hello.py)。在使用
```
chmod +x hello.py
```
将其权限更改为可执行以后，在命令行输入
```
./hello.py
```
直接运行。