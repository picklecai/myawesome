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


[TCP编程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/897692888725344/923056653167136)

> 大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

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

[Python Socket 编程详细介绍](https://gist.github.com/kevinkindom/108ffd675cb9253f8f71)

> 	•	TCP发送数据时，已建立好TCP链接，所以不需要指定地址，而UDP是面向无连接的，每次发送都需要指定发送给谁。
>	•	服务器与客户端不能直接发送列表，元素，字典等带有数据类型的格式，发送的内容必须是字符串数据。

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


## 4. 样例程序的问题  

本来这一页的程序是这样的：  

```
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
 
s.listen(5)                 # 等待客户端连接
while True:
    c.addr = s.accept()     # 建立客户端连接
    print '连接地址：', addr
    c.send('欢迎访问菜鸟教程！')
    c.close()                # 关闭连接
```
gethostname在我本机运行，提示：
```
   s.bind((HOST, PORT))
socket.gaierror: [Errno 8] nodename nor servname provided, or not known
```
于是改成了127IP地址。  

send的消息，又提示：  
```
Traceback (most recent call last):
  File "server.py", line 14, in <module>
    c.send('欢迎访问苦丁茶园地')
TypeError: a bytes-like object is required, not 'str'
```

直接加上b显然不行：  
```
 File "server.py", line 14
    c.send(b'欢迎访问苦丁茶园地')
          ^
SyntaxError: bytes can only contain ASCII literal characters.
```
于是发送的消息改成了英文。 

然后发现客户端消息发好了服务器端不会自动退出。

```
# _*_coding:utf-8_*_
import socket

# HOST = socket.gethostname()
HOST = '127.0.0.1'
PORT = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Address:', addr)
    c.send(b'welcome kudingcha Tea Garden')
c.close()
```
运行完了服务端是这样：  

```
Address: ('127.0.0.1', 53320)


```
这时如果继续运行客户端，它就继续输出这样的句子。  

以为是关闭s的事情，后来发现哪是关闭啊，是没有条件让它退出while。  

于是加上if-break大法：  

```
        c, addr = s.accept()
        if not c.recv(1024): 
            break
        print('Address:', addr)
        c.send(b'welcome kudingcha Tea Garden')
        c.close()
```
这下直接不接收消息了，客户端打印出一个b''了事。  

于是老老实实把它挪到close之前了。  

现在是全新的server程序：  

```
# 正确可运行程序
# _*_coding:utf-8_*_
import socket

# HOST = socket.gethostname()
HOST = '127.0.0.1'
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print('Address:', addr)
        c.send(b'welcome kudingcha Tea Garden')
        if not c.recv(1024):  # 没有这句，不自动退出。不能紧跟accept之后，否则不发送了。
            break
        c.close()
```
现在知道了，昨天那个教程里先使用`with conn`再`while`，也是为了省一句`conn.close`。  

要想让这个程序和昨天那个一样，accept不在while里面，必须要在while里加上recv的步骤：  

```
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    c, addr = s.accept()
    with c:
        print('Address:', addr)
        while True:
            c.recv(1024)
            c.send(b'welcome kudingcha Tea Garden')
```
这样是一个运行良好不会自动断的服务端。不过客户端也不断了。大家都这么干耗着。并且客户端并没有收到消息。

服务器强行断开后，客户端得到的是这样的空消息： 
```
b''
```

这样写即使加上if，也还是这个状态。

突然发现了一个区别。昨天的程序是客户端发来的消息。今天是服务端发出的消息，所以不需要先recv。于是改成了这样：  

```
# 正确可运行程序
# _*_coding:utf-8_*_
import socket

# HOST = socket.gethostname()
HOST = '127.0.0.1'
PORT = 12344

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    c, addr = s.accept()
    with c:
        print('Address:', addr)
        while True:
            c.send(b'welcome kudingcha Tea Garden')
            if not c.recv(1024):  # 没有这句，不自动退出。不能紧跟accept之后，否则不发送了。
                break
```
效果和刚才那个发完自动关闭的是一样的了。但是if如果去掉，就会产生这样的错误：  

```
raceback (most recent call last):
  File "server.py", line 15, in <module>
    c.send(b'welcome kudingcha Tea Garden')
BrokenPipeError: [Errno 32] Broken pipe
```

纳闷，为什么要把**接收到的客户端消息反发送回去**呢？  

### 其他  

```
    data = s.recv(1024)

print('Received', repr(data))
```
[Python repr() 函数 | 菜鸟教程](https://www.runoob.com/python/python-func-repr.html)  

repr就是返回一个对象的string形式。  

## 5. selectors  

[python中的selectors模块 - 殷大侠 - 博客园](https://www.cnblogs.com/yinheyi/p/8127871.html)

> 它的功能是实现高效的I/O multiplexing, 常用于非阻塞的socket的编程中； 

### 1. 类：  

#### 为什么是DefaultSelector？

定义对象是这样的：  
```
sel = selectors.DefaultSelector()
```
> 模块定义了一个 BaseSelector的抽象基类， 以及它的子类，包括：SelectSelector， PollSelector, EpollSelector, DevpollSelector, KqueueSelector.    

可以看到这里并没有DefaultSelector。  

> DefaultSelector类其实是以上其中一个子类的别名而已，它**自动选择为当前环境中最有效的Selector**，所以平时用 DefaultSelector类就可以了，其它用不着。

#### SelectorKey类  

一般用这个类的实例 来描述一个已经注册的文件对象的状态。  

这个类的几个属性常用到：  

- fileobj：   表示已经注册的文件对象；
- fd:          表示文件对象的描述符，是一个整数，它是文件对象的 fileno()方法的返回值；
- events:    表示注册一个文件对象时，我们等待的events, event Mask, 是可读呢还是可写呢！！
- data:       表示注册一个文件对象是邦定的data；

在多连接程序中，key来自event，key就是SelectorKey类。 
 
```
events = sel.select(timeout=None)
    for key, mask in events:
        ………………
```



### 2. 两个常量  

模块定义了两个常量，用于描述 event Mask  

EVENT_READ ：      表示可读的； 它的值其实是1；
EVENT_WRITE：      表示可写的； 它的值其实是2；


### 3. 三个方法  

多连接程序中，其实只用了它三种方法。

```
sel.register(fileobj, events, data=None)
sel.unregister(fileobj)
sel.select(timeout=None)
```

- register的作用：注册一个文件对象。  

	- 参数：  
		- fileobj——即可以是fd 也可以是一个拥有fileno()方法的对象；
		- events——上面的event Mask常量；   
		- data   
		 
	- 返回值：  
		- 一个SelectorKey类的实例；   
 
- unregister的作用：注销一个已经注册过的文件对象；

	- 返回值：
		- 一个SelectorKey类的实例；

- select的作用：用于选择满足我们监听的event的文件对象；

	- 返回值：
		- 是一个(key, events)的元组， 其中key是一个SelectorKey类的实例， 而events 就是 event Mask（EVENT_READ或EVENT_WRITE,或者二者的组合)


## 6. 修改内网版notebook

### 6.1 奇怪的exit和quit

```
data = input('今日记录，请输入（输入quit退出程序）：')
s.send(bytes(data))
data = s.recv(1024)
print('Data:', time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()), repr(data))
```
除了exit和quit，其他都报语法错误。
而这两个，结果是这样的：  

```
今日记录，请输入（输入quit退出程序）：exit
('Data:', '2019/05/09 15:31:43', "'Use exit() or Ctrl-D (i.e. EOF) to exit'")
```
很奇怪这是个啥。后来发现原来是print的结果。

```
>>> print(exit)
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> print(quit)
Use quit() or Ctrl-D (i.e. EOF) to exit
```
原来这样。。。。。可不是嘛？就是我让人家print的呀。。。

### 6.2 控制程序退出  

在客户端和服务端，控制程序退出的机制是不一样的。  

客户端负责输入数据，所以只要data输入了指定字符，例如“quit”，就可以客户端退出了。

在服务端，客户端输入的这个字符是没有用的，因为这个字符输入了后，客户端就退出了，并没有发送到服务端。所以服务端就处于无消息可接的状态。所以它得用自己的退出机制，就是样例程序中那个’若收不到新消息就退出‘。

分别是这样：  

```
# client
data = input('今日记录，请输入（输入quit退出程序）：')
if data == 'quit':
    sys.exit(0)
```

```
# server 
  # 如果没有这句话控制，一旦客户端退出，它就会陷入死循环. 
  # if sdata == 'quit'并不能拯救它死循环命运
if not data:
    break
```
测试结果：  

- 当大家都在终端运行时，正常。  
- 当服务端在ipython运行，客户端在终端运行时，正常。  
- 当服务端在终端运行，客户端在ipython运行时，客户端输入quit已退出，终端的服务器却没有退出。  


### 6.3 中文问题解决  

主要是客户端和存储文本：  

```
data = input('今日记录，请输入（输入quit退出程序）：')
if data == 'quit':
    sys.exit(0)
else:
    s.sendall(bytes(data.encode('utf-8')))
    data = s.recv(1024)
    print('Data:', time.strftime('%Y/%m/%d %H:%M:%S'), data.decode('utf-8'))
    nbserver.save(data.decode('utf-8'))
```
要用`data.decode('utf-8')`，不要用`repr(data)`，不要用`str(data)`，后面两个都会出现这样的结果：  

```
2019/05/09 16:37:08
b'\xe6\x88\x91\xe6\x98\xaf\xe4\xb8\x80\xe4\xb8\xaa\xe4\xb8\xad\xe6\x96\x87'

2019/05/09 16:38:01
b'\xe6\x88\x91\xe8\xbf\x98\xe6\x98\xaf\xe6\x98\xaf\xe8\xbf\x98\xe6\x98\xaf\xe4\xb8\x80\xe4\xb8\xaa\xe4\xb8\xad\xe6\x96\x87'

```

### 6.4 print和save的函数，放在哪里？  

发现这两个函数，放在客户端，直接用，也是可以的。根本不需要放在服务端去import。那么以前为什么要放在服务端呢？？？？

还有个问题是，在客户端，它们不能在被调用之后再定义。

[python函数的定义必须在调用前面(函数调用函数例外) - Senvenno27 - CSDN博客](https://blog.csdn.net/u011361880/article/details/74570713)

这里说，函数调用函数例外。

那么就是说如果把其他部分组织为一个main，就没关系了？？？

试了试，果然如此。

那是因为自从用ipython以来，不喜欢写main()发现的情况。  

所以**def main的作用**，一个是可以import，一个是可以把函数放在后面定义。


