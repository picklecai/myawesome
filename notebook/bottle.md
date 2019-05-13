# bottle

[bottle在GitHub上的源码：bottle.py](https://github.com/bottlepy/bottle/blob/master/bottle.py)

[Bottle Tutorial 官方教程中文翻译 | Yi's Blog](https://chowyi.com/Bottle-Tutorial-%E5%AE%98%E6%96%B9%E6%95%99%E7%A8%8B%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91/)

## 1. 第一个成功例子

这里的样例是成功的！  

```
from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)
```

### 1.1 这个例子中import的函数：route, run

在bottle.py中，

```
def route(self,

              path=None,

              method='GET',

              callback=None,

              name=None,

              apply=None,

              skip=None, **config):

        """ A decorator to bind a function to a request URL. Example::

                @app.route('/hello/<name>')

                def hello(name):

                    return 'Hello %s' % name

                   """

```
上个例子中使用的就是这个参数path。默认method是Get。

```
def run(app=None,

        server='wsgiref',

        host='127.0.0.1',

        port=8080,

        interval=1,

        reloader=False,

        quiet=False,

        plugins=None,

        debug=None,

        config=None, **kargs):

```

见到的例子有使用app，host，port，debug这几个参数的。  

## 2. template  

[瓶框（bottle）架学习之模版使用 - zandaoguang的博客 - CSDN博客](https://blog.csdn.net/zandaoguang/article/details/77387358)

好像是给网页引入变量。

```
from bottle import template

template('I am a {{state}} woman. ', state='Chinese')

```
这个输出是'I am a Chinese woman.'

```
from bottle import template

template('Hello {{name if name else "world"}}', name=None)

```

这个很厉害，在{{}}里面居然嵌入了一堆语句，有点像列表推导式。  

于是输出了'Hello world'


### 2.1 变量  

简单粗暴地理解为，<>在url上，{{}}在页面内容上  

```
@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

```

[Bottle官方教程中文翻译](https://chowyi.com/Bottle-Tutorial-%E5%AE%98%E6%96%B9%E6%95%99%E7%A8%8B%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91/)对<>的说明：  

> 包含通配符的路由(route)称作动态路由(相对于静态路由)，它可以匹配不止一个URL。一个简单的通配符(e.g. <name>)由包含在尖括号中直到下一个斜杠/前的一个或多个字符构成。例如，/hello/<name>既可以匹配请求/hello/alice，也可以匹配请求/hello/bob，但是不能匹配/hello,/hello/或hello/mr/smith。


## 3 过滤器  

```
from bottle import route, run

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)
    return template('{{id}} is {{isinstance(id, int)}} ', id=id)
run(host='localhost', port=8080, debug=True)
```

这段程序的作用是：如果路径/object/加的变量是个int，就在页面上写上‘int is True’，返回代码是200.否则就404。当然，在404的情况下，页面也是无法返回内容的。除非用try-except(按我以前思路写出来的，不行)？  assert不知道干啥的……

大雾，，，，，原来assert不是为了抛出啥的，如果正确，就啥都没有。

[python3 assert - 一步一个脚印的往前走！ - CSDN博客](https://blog.csdn.net/shijichao2/article/details/61421735)

> 应用场景
	.	通常情况传递参数不会有误，但编写大量的参数检查影响编程效率，而且不需要检查参数的合法性。
	.	排除非预期的结果。

## 4. HTTP调用与返回  

### 4.1 一个简单的登录验证界面  

```
from bottle import get, post, request, run

@get('/login')
def login():
    return '''
    <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
    </form>
    '''

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    
def check_login(username, password):
    if username == 'ahcai' and password == '123456':
        return True

run(host='localhost', port=8000, debug=True)
```

这个界面虽然简单，却完整。

前台界面用get装饰器，后台验证用post装饰器。check_login可以用之前做过的加密字典来操作。这里只是简单写了一下，类似于pass而已。

之前对request很有熟悉感，原来是bottle里的，并不是爬虫request那个。不过作用也类似吧。也是为了获得页面上的内容。  

### 4.2 Template模版文件  

```
from bottle import route, run

@route('/hello')
@route('/hello/<name>')
def hello(name='world'):
    return template('hello_template.tpl', name=name)
run(host='localhost', port=8080, debug=True)
```

500错误提示：  

```
Sorry, the requested URL 'http://localhost:8000/hello/ahcai' caused an error:

Template 'hello_template.tpl' not found.
```

造了一个hello_template.tpl文件放在同目录下，运行成功了。  

所以模版文件就是一堆写好的页面，运行时放在同目录下就行了。有点印象了。  


## 5. Youtube视频和GitHub文档——关于template，bottle等  

还遇到了一些上传下载文档的。因为和我的目的有点远，就没看。

[Intro to Templates in Bottle - YouTube](https://www.youtube.com/watch?v=kDJFjC3Fjxc)  

从这里知道了template页面中可以循环打印列表：  

```
% for i in range(len(history)):
    <p> {{history[i]}} </p>
```

还可以用if-else根据True或False，让页面打印不同的内容。

知道了end的作用。如果同时用了if和for，前面的if必须end，否则后面的for就不工作了。  

```
% if True:
    <h1>It's Pickle.</h1>
% else:
    <h1>It's Ahcai</h1>

% end

% for i in range(10):
    <p>This is loop index: {{i}} </p>
```

[Bottle Python Web Framework - Static Files - YouTube](https://www.youtube.com/watch?v=JZEgN03vigk)

讲页面载入静态文件，例如图片。

原来`reloader=True`的作用是，即使python程序发生了改变，也不需要重新启动，只要刷新就好了。

[Creating a RESTFul API With Python and Bottle - YouTube](https://www.youtube.com/watch?v=BHAUJUuhiDw)

在页面中载入字典，除了get和post，还有delete方法  

[Bottle Routing Tutorial - YouTube](https://www.youtube.com/watch?v=Mb06RZBaL9w)

这个是基础，怎么架网页，怎么使用变量，怎么写动态网页，以及在route中加入method。

[Python Web Frameworks: 5 Bottle Todo Templates 2 - YouTube](https://www.youtube.com/watch?v=mY8DynrzIzk)

静态文件也可以用来挂css文件。

[How To Create Custom Error Pages in Bottle - YouTube](https://www.youtube.com/watch?v=4bUMh2cEJ7c)

出错页面，404，405，500

[Accessing URL Query Strings in Bottle - YouTube](https://www.youtube.com/watch?v=v0BXg1W9bt0)

字符串参数放到url中。  


【以下为两个来自github的教程】：  

[nummy/bottle-cn: bottle中文文档](https://github.com/nummy/bottle-cn)

bottle中文文档  

[bottle-doc-zh-cn/tutorial_app.rst at master · myzhan/bottle-doc-zh-cn](https://github.com/myzhan/bottle-doc-zh-cn/blob/master/docs/tutorial_app.rst)

貌似开发一个todolist，包含对sqlite3的应用。后面用得上。

## 5. 改bottle程序  

### 5.1 接受表单内容  

想让程序获得页面上输入的内容，无论是return还是独立的template文件，都需要用form包裹起来

```
    <form action='/' method="post">
        <h1>输入新记录</h1>
        <input name="record" type="text" />
        <p></p>
        <input value="save" type="submit" />
    </form>
```

### 5.2 页面上呈现不一样的返回内容

想在输入成功后，返回不一样的内容，同时还能继续工作，就可以用if-else给页面写不同的内容  

```
% if savetxt == False:
    <h1>打印历史记录</h1>
    <a href='/history'>点击这里</a>
    <form action='/' method="post">
        <h1>输入新记录</h1>
        <input name="record" type="text" />
        <p></p>
        <input value="save" type="submit" />
    </form>

% else:
    <h1>打印历史记录</h1>
    <a href='/history'>点击这里</a>
    <form action='/' method="post">
        <p>保存成功，继续输入：</p>
        <h1>输入新记录</h1>
        <input name="record" type="text" />
        <p></p>
        <input value="save" type="submit" />
    </form>
```

template文件中，程序部分要用%开头。看到有写end的，但貌似不写也没问题。不知道这部分是不是python语法。  


### 5.3 在页面上逐行打印list内容  

打印字符串变量，是直接不分行的。但是记事本文件中是分行的， 所以改用list。逐行读出来，怎么逐行写进去呢？要在template文件中用for循环：  

```
% for i in range(len(history)):
    <p> {{history[i]}} </p>
```

### 5.4 兼容网页形式和命令行形式  

退出网页后，继续接受命令行端的输入。  

找了很久bottle停止的办法，后来发现要求就写着简单的Ctrl+C。那就是第一次点击这个组合时，并没有无安全退出。之前试两个端口没成功，现在把if not run 这种句子拿掉，直接在socket连接中使用第二个端口。客户端程序里也用第二个端口，成功了。  

所以代码就是简单的两行：  
```
    run(host=HOST, port=PORT1, debug=True, reloader=True)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.bind((HOST, PORT2))
```
无须其他累赘。

另外，之所以这么长时间没发现Ctrl+C是可以的，是因为每次一按这个组合，就出现这样的提示：  

```
OSError: [Errno 48] Address already in use
```  
事实上之后能运行。但我不知道啊。现在我怀疑不用两个port也是可以的。经过实验，还是要用两个port。否则客户端就连接不上。s

### 5.5 网页端输入中文的问题  

在网页上输入中文，出来是乱码。但是结果又已经是string，不能对它decode了。找了很久解决方案，最后发现，可以先decode再get：  

```
newline = request.POST.decode('utf-8').get('record')  # 先decode再get，中文无碍
```
这里用的是POST，用forms也一样吧。试了确实这样。重点是**先decode再get**。

### 5.6 两层quit问题  

在客户端程序中，设置了两层quit，一层是choose，一层是输入内容。结果内层（输入内容）的quit输入后，服务端是可以退出的。而外层（和打印输入新内容并列的）的quit输入后，服务端不能自己退出。但此时重启命令行客户端，也会被服务器拒绝连接。  

其实它们使用了同样的`sys.exit(0)`。

```
        choose = input('1. 打印历史记录 2. 输入今日记录 （输入quit退出程序）')
        if choose == '1':
            nbwebserver.print_history()
        elif choose == '2':
            data = input('今日记录，请输入（输入quit退出程序）：')
            if data == 'quit':
                sys.exit(0)
            else:
                s.sendall(bytes(data.encode('utf-8')))
                data = s.recv(1024)
                print('Data:', time.strftime('%Y/%m/%d %H:%M:%S'), data.decode('utf-8'))
                nbwebserver.save_new(data.decode('utf-8'))
        elif choose == 'quit':
            sys.exit(0)
```

这里**不明白**。

### 5.7 改进

对比以前写的程序，以上全是改进。由衷感叹：现在写的，比以前写的漂亮多了！！！

