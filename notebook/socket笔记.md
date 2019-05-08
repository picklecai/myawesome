# socket内网程序笔记

## 1. socket程序运行  

由于这个无法用ipython，于是写了终端程序。

样例上没有写python，运行的是`.xxxx.py`，结论是不行：  

```
Permission denied
```

后来发现是要写权限才能终端直接运行的。那就算了，也不差python这一个词。

在终端运行`python  xxx.py`，还是不行。

```
Traceback (most recent call last):
  File "echo-server.py", line 8, in <module>
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
AttributeError: __exit__
```

后来发现可能是with语句在python2中不行。  

于是把python3调动起来：`source activate python35`

再用`python  xxx.py`，可以了。

## 2. 在哪里运行

1. 两个程序都在终端中运行，关闭ipython  
2. 开着ipython，两个程序都在终端中运行。原本以为ipython在运行时是没法运行socket程序的，没想到完全可以。
3. 开着ipython，一个程序在ipython中运行，一个在终端运行。无论哪个运行客户端哪个运行服务端，都可以。但是如果两个都在ipython中，客户端会因为服务端占据了资源而无法继续。如果终端和ipython都在运行服务端，会提示：`[Errno 48] Address already in use`  

## 3. 基本socket方法  

来自这里：[Python 网络编程 | 菜鸟教程](https://www.runoob.com/python/python-socket.html)  

### 3.1 创建socket对象  

```
socket.socket(参数1family,参数2type,参数3protocol)
```

- 参数1family，一般有两种：AF_UNIX，AF_INET  
- 参数2type，一般有两种：SOCK_DGRAM，SOCK_STREAM，前者代表遵守UDP协议，后者代表遵守TCP协议  
- 参数3protocol，一般默认为0  

### 3.2 常见方法  

假设`s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)`

#### 3.2.1 服务器端方法  

```
s.bind((HOST, PORT))  
s.listen()  
s.accept()
```

> - bind的作用是绑定地址(HOST, PORT)到socket。在AF_INET下,以元组(HOST, PORT)的形式表示地址。 
> - listen表示开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
> - accept被动接受TCP客户端连接,(阻塞式)等待连接的到来。它的结果为连接和地址。 `conn, addr = s.accept()` 


#### 3.2.2 客户端方法  

```
s.connect()
s.connect_ex()
```
> - connect主动初始化TCP服务器连接，。一般address的格式为元组(HOST, PORT)，如果连接出错，返回socket.error错误。
> - connect_ex是connect()函数的扩展版本,出错时返回出错码,而不是抛出异常。

#### 3.2.3 公共方法

##### TCP协议数据发送和接收  

```
s.recv()
s.send()
s.sendall()
```
> - recv接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
> - send发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
> - sendall完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。

##### UDP协议数据发送和接收  

```
s.recvfrom()
s.sendto()
```
> - 接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
> - 发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。

##### 针对socket对象的  

```
s.close()

s.getpeername()
s.getsockname()

s.setsockopt(level,optname,value)
s.getsockopt(level,optname[.buflen])

s.settimeout(timeout)
s.gettimeout()

s.fileno()

s.setblocking(flag)

s.makefile()
```
> - close是关闭socket。如果创建socket对象时用了with，就可以不用close关闭
> 
> - getpeername返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）
> - getsockname返回套接字自己的地址。通常是一个元组(ipaddr,port)
> 
> - setsockopt设置给定套接字选项的值。
> - getsockopt返回套接字选项的值。
> 
> - settimeout设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
> - gettimeout返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
> 
> - fileno返回套接字的文件描述符
> 
> - setblocking中，如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
> 
> - makefile创建一个与该套接字相关连的文件


