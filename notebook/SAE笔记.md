# SAE笔记  

[免运维的云计算服务 - 新浪云](https://www.sinacloud.com/)

玩了半天，不要关机了连地址都没记住。写在这里吧。

## 0. 安装

`source activate python35`
`pip install sae-python-dev`  
pip3安装失败，改用pip安装了，一堆error，不过能import

```
ERROR: graphlab-create 1.8.5 requires awscli==1.6.2, which is not installed.
ERROR: graphlab-create 1.8.5 requires genson==0.1.0, which is not installed.
ERROR: graphlab-create 1.8.5 requires mixpanel-py==3.1.1, which is not installed.
ERROR: graphlab-create 1.8.5 requires sseclient==0.0.8, which is not installed.
ERROR: graphlab-create 1.8.5 has requirement boto==2.33.0, but you'll have boto 2.38.0 which is incompatible.
ERROR: graphlab-create 1.8.5 has requirement certifi==2015.04.28, but you'll have certifi 2018.11.29 which is incompatible.
ERROR: graphlab-create 1.8.5 has requirement decorator==3.4.0, but you'll have decorator 4.0.4 which is incompatible.
ERROR: graphlab-create 1.8.5 has requirement jsonschema==2.5.0, but you'll have jsonschema 2.4.0 which is incompatible.
ERROR: graphlab-create 1.8.5 has requirement requests==2.3.0, but you'll have requests 2.21.0 which is incompatible.
ERROR: graphlab-create 1.8.5 has requirement tornado==4.1, but you'll have tornado 4.3 which is incompatible.
```

## 1. 创建新应用  

控制台，点击创建新应用。原本担心只支持python2.7，发现如果选择独享环境就能自定义。代码管理方式也可以选择git。二级域名选择了pickle。


## 2. 代码管理  

在菜单 运行环境管理——代码管理中，可以看到git仓库。

进入代码所在目录，  
```
git clone https://git.sinacloud.com/pickle
```
后面要求输入安全邮箱和密码。安全邮箱就在这个页面上写着。  

成功后，由于第一次运行，啥也没有，所以终端提示说：  
```
warning: You appear to have cloned an empty repository.
```
然后进入这个文件夹：`cd pickle`

编辑代码并部署代码

```
#添加本地的文件改动
git add .
```

把四个代码文件都拖入新文件夹中， 然后运行下面的：  

```
#添加本地修改的备注信息
git commit -m 'Init my first app'

#将改动推送到远程仓库
git push origin master
```

commit这句成功了，但是push这句给出了提示： 

```
error: failed to push some refs to 'https://git.sinacloud.com/pickle'
```

全部提示是：

```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.07 KiB | 1.04 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote: 导出 Git 代码中...
remote: 构建程序中...
remote: Save files ok
-----> Unable to select a buildpack
remote: {"Code":1,"Error":"build image failed: exit status 1."}
remote: 错误：构建镜像失败
remote: error: hook declined to update refs/heads/master
To https://git.sinacloud.com/pickle
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to 'https://git.sinacloud.com/pickle'
```

#### 措施1:  

不知道从哪里知道的（[新浪云](https://www.sinacloud.com/doc/sae/docker/python-getting-started.html)）要加runtime来说明python版本。

#### 措施2:  

安装sae了。虽然不知道有啥用。

结果错误提示变成：  

```
Compressing objects: 100% (11/11), done.
Writing objects: 100% (14/14), 2.77 KiB | 1.39 MiB/s, done.
Total 14 (delta 2), reused 0 (delta 0)
remote: 导出 Git 代码中...
remote: 构建程序中...
remote: Save files ok
-----> Python app detected
-----> Network Connection Success
       !     Requested runtime ($ cat runtime.txt
       python-3.7.2) is not available for this stack (cedar-14).
       !     Aborting.  More info: https://devcenter.heroku.com/articles/python-support
remote: {"Code":1,"Error":"build image failed: exit status 1."}
remote: 错误：构建镜像失败
remote: error: hook declined to update refs/heads/master
To https://git.sinacloud.com/pickle
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to 'https://git.sinacloud.com/pickle'
```

又把这个文件删了。从`git add .` 开始，重新再来一遍。  现在的提示：  

```

remote: 部署程序中 .............
To https://git.sinacloud.com/pickle
 * [new branch]      master -> master
 
```

至少不出错了吧。但是启动失败。

又把那个文件runtime扒拉出来，先把python版本改成3.6.8，依然如故。然后把第一句去掉，只留下版本号这一句，貌似成功。

```
remote: 部署程序中 ....
To https://git.sinacloud.com/pickle
   0544d08..0339720  master -> master
```

但是启动依旧错误。

突然发现config.yaml、index.wsgi这两个文件是共享环境需要的，现在我这个独立环境不需要了。删了吧。创建app的任务，转到主程序上。


#### 措施3:提交工单 

[在新浪云上部署Django应用程序 - SmartPython - SegmentFault 思否](https://segmentfault.com/a/1190000004980818)

这个人的看法是，只要本地能启动，就能上传上去。容器启动运行中可能是客观原因，建议找客服。于是提交了一个工单。

客服回复：

> “代码根目录下没有Procfile，没有指定你的python进程怎么启动，所以启动不了。”

我目录下的这文件，扩展名不对。研究了一下，发现是要在显示简介里，把扩展名去掉。如果像windows一样在文件名中改，是不成的。  

现在果然启动了。。。。。

## 3. 代码修改  

### 3.1 第一个版本：能启动

现在第一个能启动的服务，代码是这样的，备注在这里：  

```
#main.py  

# _*_coding:utf-8_*_
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://www.sinacloud.com")
        self.set_header('content-type', 'text/plain')
        self.write('Hello, World! ' + str(response.body[:100]))

application = tornado.web.Application([(r"/", MainHandler), ])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(5050 or os.environ['PORT'])
    tornado.ioloop.IOLoop.current().start()
```

与之对应的其他文件：  
```
# Procfile(注意：没有任何扩展名)
-------------------------------------------------
web: python main.py runserver 0.0.0.0:5050

# requirements.txt
-------------------------------------------------
tornado==4.2.1
gunicorn
pillow

# runtime.txt
-------------------------------------------------
python-3.7.2

# sinacloud-packages.txt
-------------------------------------------------
# cat sinacloud-packages.txt
curl
wget
vim
# apt-get install -y curl wget vim

```

下来开始折腾了：  

### 3.2 第二个版本，不能启动  

```
#main.py 

from bottle import Bottle
import sae

app = Bottle()


@app.route('/')
def hello(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<h1> Hello world!</h1>']

application = sae.create_wsgi_app(app)

```

与之对应的其他文件：  

```
# Procfile
-------------------------------------------------
web: python main.py runserver 0.0.0.0:5050

# requirements.txt
-------------------------------------------------
tornado==4.2.1
pillow

# runtime.txt
-------------------------------------------------
python-3.7.2

```

### 3.3 第三个版本：不能启动

```
#main.py

# _*_coding:utf-8_*_
import time
import os
from bottle import run, route, post, template, request


def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])


@route('/')
def index():
    return template('index', savetxt=False)


@post('/', method='POST')
def save():
    newline = request.forms.decode('utf-8').get('record')
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()
    return template('index', savetxt=True)


@route('/history')
def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        return template('history', history=notelist)


if __name__ == '__main__':
    global HOST, PORT
    HOST = '0.0.0.0'
    PORT = 5050
    run(host=HOST, port=PORT, debug=True, reloader=True, app=application)

```

配套文件和3.2相比没有变化。  

### 3.4 第四个版本：可以运行，但是页面502——改端口为5050后完好无损   

main的内容来自这里：[Python3 --- Tornado简介 - __静禅__ - CSDN博客](https://blog.csdn.net/Ka_Ka314/article/details/81163740)

```
#main.py

import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello World!")

if __name__ == '__main__':
    app = tornado.web.Application([(r"/", IndexHandler), ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
    
```
配套文件和3.2相比，变更了tornado版本。  

```
# Procfile
-------------------------------------------------
web: python main.py runserver 0.0.0.0:5050

# requirements.txt
-------------------------------------------------
tornado==5.1.1
pillow

# runtime.txt
-------------------------------------------------
python-3.7.2

```  
页面的反应是：  

```
502 Bad Gateway
-------------------------------------------------
nginx-l7

```

### 3.5 第五个版本：可以运行，但是页面502——改端口为5050后完好无损  

main的内容来自这里：[Python3 --- Tornado简介 - __静禅__ - CSDN博客](https://blog.csdn.net/Ka_Ka314/article/details/81163740)

```
#main.py

import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        self.write("Hello World!")


if __name__ == "__main__":
    app = tornado.web.Application([(r"/", IndexHandler), ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()

```

配套文件和3.4相比没有变化。  


突然发现，这个程序里的端口不是5050！！！重点啊！赶紧改成5050，马上页面就不502了，显示出了‘Hello World!’！

所以我觉得第四个版本可能也是这个原因。试验了一下，果然如此。那个版本也看到了内容，这回我写的是‘Hello World! No http_server.’

### 3.6 第一个版本——按四、五版本的格式改写，实际为它们的扩展版  

```

#main.py

import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient


class IndexHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://www.sinacloud.com")
        self.set_header('content-type', 'text/plain')
        self.write('Hello, World! ' + '\n' + str(response.body[500:700]))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/", IndexHandler), ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(5050 or os.environ['PORT'])
    tornado.ioloop.IOLoop.current().start()
    
```

### 3.7 第六个版本：不能启动

```
from bottle import Bottle, run
import sae

app = Bottle()


@app.route('/')
def hello():
    return "Hello, world! - Bottle"

application = sae.create_wsgi_app(app)

```

配套文件，在requiement中加入bottle，试图解决之前不能启动的问题。结果表明这样做没有作用。

```
# Procfile
-------------------------------------------------
web: python main.py runserver 0.0.0.0:5050

# requirements.txt
-------------------------------------------------
tornado==5.1.1
bottle
pillow

# runtime.txt
-------------------------------------------------
python-3.7.2

```  

sae后台的日志反馈是：  

```
ModuleNotFoundError: No module named 'sae'
    import sae
  File "main.py", line 3, in <module>
Traceback (most recent call last):
ModuleNotFoundError: No module named 'sae'
    import sae
  File "main.py", line 3, in <module>
Traceback (most recent call last):
ModuleNotFoundError: No module named 'sae'
    import sae
  File "main.py", line 3, in <module>
Traceback (most recent call last):
ModuleNotFoundError: No module named 'sae'
    import sae
  File "main.py", line 3, in <module>
Traceback (most recent call last):
ModuleNotFoundError: No module named 'sae'
    import sae
  File "main.py", line 3, in <module>
Traceback (most recent call last):
```

又在requirements.txt增加了sae，反馈是：  

```
remote: Save files ok
-----> Python app detected
-----> Network Connection Success
-----> Installing requirements with pip
       Collecting sae (from -r /tmp/build/requirements.txt (line 3))
       Could not find a version that satisfies the requirement sae (from -r /tmp/build/requirements.txt (line 3)) (from versions: )
       No matching distribution found for sae (from -r /tmp/build/requirements.txt (line 3))
remote: {"Code":1,"Error":"build image failed: exit status 1."}
remote: 错误：构建镜像失败
remote: error: hook declined to update refs/heads/master
To https://git.sinacloud.com/pickle
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to 'https://git.sinacloud.com/pickle'
```

### 3.8 第七个版本——能运行

仔细看了一下，3.7这个版本和3.2，是差不多的。所以可能我是在瞎折腾。于是决定写一个最简单的bottle程序来试试：  

```
#main.py

from bottle import route, run


@route('/')
def hello():
    return "Hello, world! - Bottle"

run(host='0.0.0.0', port=5050, debug=True, reloader=True)
```

既然刚才说sae无法在服务器安装，那就不奉陪了。于是从requirement中去掉了它。现在配套文件是这样：  

```
# Procfile
-------------------------------------------------
web: python main.py runserver 0.0.0.0:5050

# requirements.txt
-------------------------------------------------
tornado==5.1.1
bottle
pillow

# runtime.txt
-------------------------------------------------
python-3.7.2

``` 

竟然运行成功了！！！页面显示出了我写的内容：'Hello, world! - Bottle'

果然瞎折腾。bottle直接就能上！不用依赖于tornado！！！

### 3.9 第八个版本——能运行  

茅塞顿开，于是摒弃了一切花花肠子，把原始的内容拿来贴到main.py上。 当然，port和host还是注意了一下，改成sae要求的。

```
#main.py

import time
import os
from bottle import run, route, post, template, request


@route('/')
def index():
    return template('index', savetxt=False)


@post('/', method='POST')
def save():
    newline = request.forms.decode('utf-8').get('record')
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()
    return template('index', savetxt=True)


@route('/history')
def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        return template('history', history=notelist)


if __name__ == '__main__':
    global HOST, PORT
    HOST = '0.0.0.0'
    PORT = 5050
    run(host=HOST, port=PORT, debug=True, reloader=True)

```

配套文件和上个版本比没有变化。

这回没有去看后台，直接刷新http://pickle.applinzi.com/，看到了梦寐以求的页面内容，链接、H1标题、文本框、按钮，都在。

唯一的问题是history页面没有内容。可以没有保存内容，但页面静态内容也没有。看了一下代码，明白了。因为存储问题，带来的是if不执行。把return包裹在里面，自然啥都没有。

### 3.10 第九个版本——能运行

改了一下history页面显示的问题。原本想着只是为了页面能有内容，存储问题慢慢解决的。
```
#main.py

# _*_coding:utf-8_*_
import time
import os
from bottle import run, route, post, template, request


@route('/')
def index():
    return template('index', savetxt=False)


@post('/', method='POST')
def save():
    newline = request.forms.decode('utf-8').get('record')
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()
    return template('index', savetxt=True)


@route('/history')
def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
    else:
        notelist = []
    return template('history', history=notelist)


if __name__ == '__main__':
    global HOST, PORT
    HOST = '0.0.0.0'
    PORT = 5050
    run(host=HOST, port=PORT, debug=True, reloader=True)

```

结果。。。。成功了！页面能显示内容了。也就是说，我在服务器上建立了一个临时文件，用来存我的乱七八糟的记录。

那是不是要增加一个清空功能啊。毕竟我都是瞎写的记录啊！

改了一下配套文件：

```
# Procfile
-------------------------------------------------
web: python main.py runserver 0.0.0.0:5050

# requirements.txt
-------------------------------------------------
bottle

# runtime.txt
-------------------------------------------------
python-3.7.2

``` 
重新更新提交了。再运行，没有问题。但是发现历史记录没有了。
那不需要我增加清空功能了。每次重新上传程序，就会清空之前的历史文件的。包括我去掉的依赖库也会卸载。




