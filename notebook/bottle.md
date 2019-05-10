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


