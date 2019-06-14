# Django

[Django 教程 | 菜鸟教程](https://www.runoob.com/django/django-tutorial.html)

## 1. 创建新项目  

在命令行指定文件夹下输入：  

```
django-admin.py startproject testdj

```
可以建立一个新项目，文件夹下会发现testdj的文件夹，其中已有若干文件：  

```
manage.py
文件夹testdj
	__init__.py
	settings.py
	urls.py
	wsgi.py

```
进入testdj下运行manage.py即可启动服务器（注意第二个参数是runserver）。
```
python manage.py runserver
```

默认地址为：http://127.0.0.1:8000/

现在它是个空页面。

想要同时试试Django1.1和Django2.2的效果，但是提示这个端口已被占用。想想也是啊。赶紧找什么地方设置端口号的。settings里面并没有。后来发现，仍然是在manage.py运行的参数中：  

```
python manage.py runserver 127.0.0.1:5050
```
本来想用0.0.0.0，结果提示必须要把它加入允许的地址内。

现在有两个Django空页面运行起来了😤

## 2. 做点什么

两大方法来显示：

### 2.1 url函数

在子文件夹下新建了一个view.py，其中包含一个hello函数。为了方便urls.py来引用它。

```
# view.py

from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")
```

```
# urls.py

from django.conf.urls import url
from . import view

urlpatterns = [url(r'^$', view.hello), ]

```
这个urlpatterns一看就是个正则表达式匹配，但是r字符串表示空行。request参数如何传入呢？

页面可以显示helloworld。

### 2.2 path函数

另一种办法，view.py不变，urls.py变化一下。

到了/hello页面上显示了：  

```
from . import view
from django.urls import path

urlpatterns = [path('hello/', view.hello), ]

```
但是这两个不能同时。urlpatterns是固定变量，改名了就不工作了。

#### path实现多目录

发现列表的作用就是支持多路径的：  

```
from . import view
from django.urls import path

urlpatterns = [path('hello/', view.hello), path('world', view.hello),]

```
这样写，world路径下也能看到helloworld。根目录在path函数中是用空字符串表示：  

```
urlpatterns = [path('hello/', view.hello), path('world', view.hello), path('', view.hello), ]
```
加上最后一项，根目录也能看到helloworld了。

**注意：**表示路径的参数中，加了'/'就要在访问时也加上。没加在访问时也不要加。否则就没有这个页面了。

#### url实现多目录

如果是用url实现多目录，则是：  

```
urlpatterns = [url(r'^$', view.hello), url(r'^index/$', view.hello), url(r'^hi/$', view.hello), ]
```

现在也知道了空行匹配什么意思了，就是根目录。不空则为子目录名称。

可能是`debug=True`的原因，做这些改动都不用重启服务器。

## 3. Django模板

既然bottle可以用template，想必Django这么以大而全著称的也不会少了。

和manage.py并列，新建一个templates文件夹，其中包含一个普通html文件。

这回需要在settings中设置一下templates的路径了：  

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates', ], #新修改的内容
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
view.py文件需要修改：  
```
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello world!'
    # return HttpResponse('Hello world!')
    return render(request, 'hello.html', context)
```
现在打开hello路径，就可以看到h1形式的hello world。

### 模板语法  

`{{}}`内包含变量  
可以嵌套for循环，但是不能在变量中继续引用列表子项。


