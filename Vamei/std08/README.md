## Python 标准库08: 多线程与同步 (threading包)
Python主要通过标准库中的threading包来实现多线程。在当今网络时代，每个服务器都会接收到大量的请求。服务器可以利用多线程的方式来处理这些请求，以提高对网络端口的读写效率。Python是一种网络服务器的后台工作语言 (比如豆瓣网)，所以多线程也就很自然被Python语言支持。

(关于多线程的原理和C实现方法，请参考我之前写的[Linux多线程与同步](https://www.cnblogs.com/vamei/archive/2012/10/09/2715393.html)，要了解race condition, mutex和condition variable的概念)

    