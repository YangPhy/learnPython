## Python 标准库08: 多线程与同步 (threading包)
Python主要通过标准库中的threading包来实现多线程。在当今网络时代，每个服务器都会接收到大量的请求。服务器可以利用多线程的方式来处理这些请求，以提高对网络端口的读写效率。Python是一种网络服务器的后台工作语言 (比如豆瓣网)，所以多线程也就很自然被Python语言支持。

(关于多线程的原理和C实现方法，请参考我之前写的[Linux多线程与同步](https://www.cnblogs.com/vamei/archive/2012/10/09/2715393.html)，要了解race condition, mutex和condition variable的概念)

### 多线程售票以及同步
我们使用Python来实现Linux多线程与同步文中的售票程序。我们使用mutex (也就是Python中的Lock类对象) 来实现线程的同步: [Example1](thread1.py)
```
# A program to simulate selling tickets in multi-thread way
# Written by Vamei

import threading
import time
import os

# This function could be any function to do other chores.
def doChore():
    time.sleep(0.5)

# Function for each thread
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()                # Lock; or wait if other thread is holding the lock
        if i != 0:
            i = i - 1                 # Sell tickets
            print(tid,':now left:',i) # Tickets left
            doChore()                 # Other critical operations
        else:
            print("Thread_id",tid," No more tickets")
            os._exit(0)              # Exit the whole process immediately
        lock.release()               # Unblock
        doChore()                    # Non-critical operations

# Start of the main function
i    = 100                           # Available ticket number 
lock = threading.Lock()              # Lock (i.e., mutex)

# Start 10 threads
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))   # Set up thread; target: the callable (function) to be run, args: the argument for the callable 
    new_thread.start()                                      # run the thread
```
我们使用了两个全局变量，一个是i，用以储存剩余票数；一个是lock对象，用于同步线程对i的修改。此外，在最后的for循环中，我们总共设置了10个线程。每个线程都执行booth()函数。线程在调用start()方法的时候正式启动 (实际上，计算机中最多会有11个线程，因为主程序本身也会占用一个线程)。Python使用threading.Thread对象来代表线程，用threading.Lock对象来代表一个互斥锁 (mutex)。

有两点需要注意:

* 我们在函数中使用global来声明变量为全局变量，从而让多线程共享i和lock (在C语言中，我们通过将变量放在所有函数外面来让它成为全局变量)。如果不这么声明，由于i和lock是不可变数据对象，它们将被当作一个局部变量(参看Python动态类型)。如果是可变数据对象的话，则不需要global声明。我们甚至可以将可变数据对象作为参数来传递给线程函数。这些线程将共享这些可变数据对象。
* 我们在booth中使用了两个doChore()函数。可以在未来改进程序，以便让线程除了进行i=i-1之外，做更多的操作，比如打印剩余票数，找钱，或者喝口水之类的。第一个doChore()依然在Lock内部，所以可以安全地使用共享资源 (critical operations, 比如打印剩余票数)。第二个doChore()时，Lock已经被释放，所以不能再去使用共享资源。这时候可以做一些不使用共享资源的操作 (non-critical operation, 比如找钱、喝水)。我故意让doChore()等待了0.5秒，以代表这些额外的操作可能花费的时间。你可以定义的函数来代替doChore()。