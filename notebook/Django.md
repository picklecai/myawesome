# Django

[Django 教程 | 菜鸟教程](https://www.runoob.com/django/django-tutorial.html)

[Django 文档 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.0/)

《The Django Book》（中文版），这是一本教材。感觉有点旧，还是2008年的。
最新版：[Mastering Django 2 – The Book - Python Django Tutorials](https://djangobook.com/)

看版本：

` python -m django --version`

当前版本是3.0.6

## 1. 创建新项目  

### 1.1 正常

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



### 1.2 意外  

在windows下安装了python3.7.6和Django3.0.6后，很高兴地按照上面的方法新建项目，却没有成功。

只启动django-admin.py文档，不建立文件夹和文件。而且sublime还有找不到localhost的错误。以为这个错误很关键，找了好多地方，后来发现这个似乎无关紧要。

于是看是不是Django和python版本不对付，也没有。

然后看Django的路径是不是加入了系统path里，一看都在。

[django-admin.py startproject testdj 失败 没有工程文件夹 - 皎陽 - 博客园](https://www.cnblogs.com/dingjiaoyang/p/10536803.html) 这里提到的似乎没有加。

不过又加了一条进去，保险一点。

```
>>> import django
>>> django.get_version()
'3.0.6'
>>> import sys
>>> print(sys.executable)
C:\ProgramData\Anaconda3\python.exe
>>> print(django.__file__)
C:\ProgramData\Anaconda3\lib\site-packages\django\__init__.py
```

加入了最后一行的路径。但并没有什么用。

起作用的是他的第三种，不写.py：

```
django-admin.py startproject testdj
```

改为：

```
django-admin startproject testdj
```

这才真正成功。

启动也没有什么幺蛾子，也成功了。

## 2. 做点什么

两大方法来显示：path，url

> 我们把视图函数作为对象传递，而不是调用它。这是 Python (及其它动态语言的) 的一个重要特性:函数是一级对象 (first-class objects)， 也就是说你可以像传递其它变量一样传递它们。很酷吧? 


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

### 2.3 path实现多目录

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

### 2.4 url实现多目录

如果是用url实现多目录，则是：  

```
urlpatterns = [url(r'^$', view.hello), url(r'^index/$', view.hello), url(r'^hi/$', view.hello), ]
```

现在也知道了空行匹配什么意思了，就是根目录。不空则为子目录名称。

可能是`debug=True`的原因，做这些改动都不用重启服务器。

### 2.5 path&url可以同时使用

```
from django.contrib import admin
from . import view
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls), url(r'^time/$', view.clock)
]
```

但是这个从Django1.6后不能用了：  

```
from django.conf.urls.defaults import patterns 
```
注意，url函数的正则表达式中，**`^`后面不能再加`/`**，直接加路径名称（比如time）。

### 2.6 时间显示小函数

```
# view.py

from django.http import HttpResponse
import time

def clock(request):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    html = '<html><body>It is now: %s.</body></html>' % now
    return HttpResponse(html)
```
在view.py文件中的函数被称为视图函数（view function）。

> 每个视图函数都以一个 HttpRequest 对象为第一个参数，该参数通常命名为 request 。 

该页面运行起来后，发现时间不是本时区的时间，而是0点时间。 

> Django 时区 (Time Zone)Django 包含一个默认为 America/Chicago 的 TIME_ZONE 设置。这可能不是你所居住的时区，因此你可以在 settings.py 文件中修改它。 

看到了settings文件中显示为`TIME_ZONE = 'UTC'`。

如果想换其他时区，就到这里[PostgreSQL: Documentation: 8.1: Date/Time Key Words](https://www.postgresql.org/docs/8.1/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE)来替换。例如：东八区可以这么设置settings：  

```
TIME_ZONE = 'Etc/GMT-8'
```

### 2.7 动态显示时间

```
# urls.py

from . import view
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls), url(r'^time/$', view.clock),
    url(r'^time/plus/(\d{1,2}$)', view.timeAhead),
]
```

这个正则表达式中增加了一个分组，该分组可在view文件的timeAhead函数中捕获并运用。

$理论上应该写在括号外面，但这样也可以。

```
# view.py

def timeAhead(request, offset):
    offset = int(offset) # 字符转数字
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %d hours, it\'ll be : %s.</body></html>' % (offset, dt)
    return HttpResponse(html)
```

使用offset这个参数捕获urls正则表达式中的分组。

> 变量offset可以任意命名它，只要符合 Python 的语法。变量名是无关紧要的，重要的是它的位置，它是这个函数的第二个参数 (在 request 的后面)。还可以使用关键字来定义它，而不是用位置。 

### 2.8 `assert False`

在view.py的任意位置，加上`assert False`，就可以看到局部变量值了。

哈哈哈，再也不用print了！！！🌹🌹🌹

## 3. Django模板

### 3.1 模板语法：变量、标签、过滤器  

#### 3.1.1 变量（	variable）  

`{{}}`内包含变量  

例如：  

```
<p>Dear {{ person_name }},</p>
```

#### 3.1.2 模板标签（template tag）

标签(tag)定义比较明确，即:仅通知模板系统完成某些工作 的标签。  
`{% %}`包含标签，可以使用for、if等。

for 标签用于构建简单的循环，允许你遍历循环中的每一项。可以嵌套for循环，但是不能在变量中继续引用列表子项。

if 标签是用来执行逻辑判断的，检测 某变量值 是否为 True 。如果是，模板系统将显示 {% if 变量名 %} 与 {% endif %} 之间的所有内容。如果不是模板系统不会显示它。它当然也支持 {% else %} 以及 其他多种逻辑判断方式。 

解决**引用列表子项**的问题：  

> 在 Django 模板中遍历复杂数据结构的关键是句点字符 (.)。使用句点可以访问字典的键 值、属性、索引和对象的方法。 

**句点可用于访问列表索引** 

例如:

```
from django.template import Template, Context    

t = Template('Item 2 is {{ items.2 }}.')  
c = Context({'items': ['apples', 'bananas', 'carrots']}) 

t.render(c)
```

不允许使用负数列表索引。像 {{ items.-1 }} 这样的模板变量将会引发TemplateSyntaxError 异常。 

假设你要向模板传递一个 Python 字典。要**通过字典键访问该字典的值**，可使用一个句点:

```
from django.template import Template, Context    

person = {'name': 'Sally', 'age': '43'}   
t = Template('{{ person.name }} is {{ person.age }} years old.') 
c = Context({'person': person}) t.render(c)
```

输出：

```
 'Sally is 43 years old.' 
```

同样，也可以通过句点来**访问对象的属性**。

比方说， Python 的 datetime.date 对象有 year 、 month 和 day 几个属性，你同样可以在模板中使用句点来访问这些属性: 

```
from django.template import Template, Context 
import datetime

 d = datetime.date(1993, 5, 2) d.year    
（输出）1993 
  d.month   
（输出）5   
 d.day     
（输出）2    
 t = Template('The month is {{ date.month }} and the year is {{ date.year }}.') >>> c = Context({'date': d}) t.render(c)
```

输出：

```
 'The month is 5 and the year is 1993.' 
```

下例使用了一个自定义类:

```
from django.template import Template, Context 

class Person(object): 
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name
    t = Template('Hello, {{person.firs_name}} {{person.last_name}}.')     c = Context({'person': Person('John', 'Smith')})
    t.render(c)
```

输出： 

```
'Hello, John Smith.'
```

句点还用于**调用对象的方法**。

例如，每个 Python 字符串都有 upper() 和 isdigit() 方法， 你在模板中可以使用同样的句点语法来调用它们: 
```
from django.template import Template, Context

 t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}') 
t.render(Context({'var': 'hello'}))
```

输出：

``` 
'hello -- HELLO -- False'
```

如果是：

```
 t.render(Context({'var': '123'}))
```

输出：  

```
 '123 -- 123 -- True' 
```

注意你不能在方法调用中使用圆括号。而且也无法给该方法传递参数;你只能调用不需参数的方法。

句点查找规则可概括为:

当模板系统在变量名中遇到点时，按照以下顺序尝试进行查找: 

- 字典类型查找 (比如 foo["bar"] ) 
- 属性查找 (比如 foo.bar )
- 方法调用 (比如 foo.bar() )
- 列表类型索引查找 (比如 foo[bar] ) 


#### 3.1.3 过滤器（filter）

`{{x|y}}`，将变量x转变为格式y表达的形式。y的组成是：`xx过滤器:"参数"`

#### 3.1.4 注释

```
{# #}
```

### 3.2 使用模板系统

既然bottle可以用template，想必Django这么以大而全著称的也不会少了。

想要在Python代码中使用模板系统，只需遵循下面两个步骤:   

1. 可以用原始的模板代码字符串创建一个 Template 对象， Django同样支持用指定模板文 件路径的方式创建来 Template 对象; 
2. 调用 Template 对象的 render() 方法并提供给它变量(i.e., 内容). 它将返回一个完整的模板字符串内容,包含了所有标签块与变量解析后的内容. 

使用Django模板系统的基本规则:写模板，创建 Template 对象，创建 Context ，调用 render() 方法。 


#### 3.2.1 创建模板对象

创建一个 Template 对象最简单的方法就是直接实例化它。 Template 类就在 django.template 模块中，构造函数接收一个参数。

```
python manage.py shell
```
进入命令行交互界面。

```
from django.template import Template 
t = Template("My name is {{ name }}.") 
print(t)
```

输出是这样的：
```
<django.template.Template object at 0xb7d5f24c> 

```

系统会在下面的情形抛出 `TemplateSyntaxError` 异常:  

- 无效的块标签
- 无效的参数
- 无效的过滤器
- 过滤器的参数无效
- 无效的模板语法
- 未封闭的块标签 (针对需要封闭的块标签) 


#### 3.2.2 调用模板

##### 3.2.2.1 python程序中调用（template文件不独立）

> 一旦你创建一个 Template 对象，你可以用 context 来传递数据给它。一个context是一系列 变量和它们值的集合。模板使用它来赋值模板变量标签和执行块标签。 context在Django里表现为 Context 类，在 django.template 模块里。它构造是有一个可选参数:一个字典映射变量和它们的值。调用 Template 对象的 render() 方法并传递context来填充模板: 

```

from django.template import Context, Template 

t = Template("My name is {{ name }}.")    
c = Context({"name": "Stephane"})    
t.render(c) 

```
输出：  

```
'My name is Stephane.'
```

使用同一模板源渲染多个Context，只创建 一次 模板 对象，然后对它多次调用 render() 将会更加高效。

``` 
# Bad
for name in ('John', 'Julie', 'Pat'):
    t = Template('Hello, {{ name }}') 
    print(t.render(Context({'name': name})))

# Good
t = Template('Hello, {{ name }}')
for name in ('John', 'Julie', 'Pat'):
    print(t.render(Context({'name': name})))
```


##### 3.2.2.2 独立的template文件

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

### 3.3 使用include、block等节省html重复代码量

#### 3.3.1 include

`{% include '模板名称'%}`可以加载完全重复的部分，例如相同的header、footer等。

> 每当在多个模板中出现相同的代码时， 就应该考虑是否要使用 {% include %} 来减少重复。 


如果使用了静态文件，`{% load staticfiles %}`要放在被include的共同部分（主要是head部分）
```
# index.html

<!DOCTYPE html>
<html>
	{% include 'nav.html' %}
	<form action="{% url 'info' %} " method="POST">
	……
```
```
# nav.html

    <head>
        {% load staticfiles %}
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="{% static '/styles/main.css' %}">
        <title>babyrecord</title>
        <meta name="description" content="">
     ……
```
由于我在这个nav中还包含了body部分的内容，所以nav中使用了完整的`<body></body>`对。index中反而不需要`<body></body>`了。

#### 3.3.2 block

block和include的区别是：include是完全相同的代码，而block则允许定制某些变量。

nav.html改成了以下：

```
# nav.html

<head>
        {% load staticfiles %}
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="{% static '/styles/main.css' %}">
        <title> {% block title %} {% endblock %} </title>
        <meta name="description" content="{% block description %}{% endblock %}">
     …………   
{% block content %}{%  endblock %}
```
这里使用了三个block变量：title，description，content

在index页面中，依次定义这三个变量即可。注意：开头的include改为了extends。  
content可以把每个页面不同的模块都包进去。否则页面只显示nav的内容。

```
# index.html

<!DOCTYPE html>
<html>
	{% extends 'nav.html' %}
	{% block title %} Baby Record {% endblock %}
	{% block description %}宝宝成长记录是一款专用于儿童信息记录的软件。{% endblock %}
	{% block content %}
	<form action="{% url 'info' %} " method="POST">
		{%csrf_token%}
		<div class="labeltitle">
		请记录宝宝今天的表现吧:
        </div>
		</br>    
		<div align="center" style="width:100%;padding:30px;padding-bottom:80px;">
		    <textarea name="newline" rows="6" cols="50" style="width:80%;float:left;"/>开始记录宝宝表现……</textarea>	    	
	    </div>
	    </br>
		<div align="left" style="padding:30px;">
		    <input value="保存" type="submit" style="width:20%;padding:5px;padding-bottom:10px;float:left;" name="saveinfo" />
		</div>
    </form>	
    {% endblock %}	

</html>
```

## 4. 静态文件

[django 项目的html加载css文件 - 小青蛙 - CSDN博客](https://blog.csdn.net/xm_csdn/article/details/74556319)
[Django项目中Html文件链接css文件 - wait_me的博客 - CSDN博客](https://blog.csdn.net/qq_37549042/article/details/85696919)
[在Django中使用css，js等静态文件 - 时光匆匆独白 的博客 - CSDN博客](https://blog.csdn.net/dong_W_/article/details/78767573)
[编写你的第一个 Django 应用，第 6 部分 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial06/)
[Django静态资源部署404解决方式 - topbo的博客 - CSDN博客](https://blog.csdn.net/scissors0707/article/details/79034167)

搞了好几天，灰心丧气的，可算成功一次了！！！🌹🌹🌹

### 4.1 view.py文件

```
# view.py

from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hi everyone, this is Peter Two.'
    return render(request, 'hello.html', context)

```
与平常一样，使用render。

### 4.2 hello.html

这个文件的改法还是很重要的。如果是平常html文件，link的href直接写好相对位置就好了。

```
# hello.html

{% load static %}
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Hello Document</title>
        <link rel="stylesheet" type="text/css" href="{% static 'main.css' %}">
    </head>

    <body>
        <p class="get-title">{{ hello }}</p>
        <p class="get"> What are you doing?</p>
    </body>
</html>
```
在整个html文件的顶部，`<html>`标签之外，加上这一句：`{% load static %}`，也有写作`{% load staticfiles %}`的，亲试无影响。（在windows里安装3.0.6后，多了files就不行了。）

`<link rel="stylesheet" type="text/css" href="{% static 'main.css' %}">`，对这个href，我无数次怀疑写错了。。。

**static文件夹的位置**，是和templates并列的，根目录之下。   


### 4.3 urls.py

为了这个，path和url同用我都试了无误。没想到最后还是在官方文档([Managing static files (e.g. images, JavaScript, CSS) | Django documentation | Django](https://docs.djangoproject.com/en/2.2/howto/static-files/))上发现了正确写法。

```
# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), url(r'^time/$', view.clock),
    url(r'^time/plus/(\d{1,2}$)', view.timeAhead), path('hello/', view.hello)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```
引入settings和static后，需要在整个urlpatterns原先的列表后面加上static函数，参数分别是`STATIC_URL`和`STATIC_ROOT`。这两个值都在settings里定义了。

### 4.4 settings文件

settings文件最重要！！！

首先确认`django.contrib.staticfiles` 在`INSTALLED_APPS`中。

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```
然后定义三个常量：  

```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), '/var/www/static/', ]

```
比较奇怪的是，**STATICFILES_DIRS**没见引用，之前却因为写错了，无论如何过不了。

目前为止，`'/var/www/static/', `这句可要可不要，没有影响效果。未知后事。

以上是css文件直接在static文件夹下的写法。

### 4.5 static下分文件  

常见静态文件，至少有css、js、图片等多种类型，当然希望它们不要混在一起。这就产生了对静态文件分类的需求。

这回只需要改html文件：  

```
<link rel="stylesheet" type="text/css" href="{% static 'styles/main.css' %}">
```
在静态文件根目录下，添加了styles文件夹，css文件是在这个文件夹里的。那就在static文件夹下增加这个文件夹，再把已有的main.css拖进去就完事了。

ps.试过根目录下使用这个命令`python manage.py collectstatic`，真没管用。

### 4.6 图片

    ```
<img src="{% static '/images/logo.png' %}" />
    ```

html文件中的img写法，和css文件一样，增加`{% static %}`外壳。

### 4.7 icon

[Django添加favicon.ico图标_<sdffdsfsdfdfs>sfsfsfsdfsdffds</sdfsDS>Fsd-CSDN博客](https://blog.csdn.net/Px01Ih8/article/details/82322022)

首先先制作一个ico文件，使用PS或者某些在线生成ico的网站即可，我是在下面的网站生成的，当然，你也可以用其他网站！

http://www.bitbug.net/

下载后将此文件命名为“favicon.ico”后放在static//images/下

这个办法成功了！

方法一、在url.py中添加：

```
from Django.views.generic.base import RedirectView
urlpatterns=[
    ...
    # favicon.cio
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/blog/img/favicon.ico')),     
]
```

把请求”/favicon.ico”，指向static/blog/img/favicon.ico 这个文件，重新部署一下项目就可以看到你想要的效果。



### 4.8 地图嵌入页面

1. 获取地图代码

[创建地图-百度地图生成器](http://api.map.baidu.com/lbsapi/creatmap/)

这个页面默认的是gb-2312，在我的网站里显示为乱码，因此改成了万能的utf-8。

2. 嵌入页面

   原计划是把这一堆html、css、js分别拆开，放到现有页面中去。但是试了好几天，哪怕独立显示没有任何问题，一进django的页面，马上就不显示了。这么简单的问题，搜半天也没见到一样问题的。

   突然见到了使用iframe的。于是改方案。

3. iframe嵌入

   首先代码存为独立页面map.html.

   然后在url.py和view.py中让它活：

   ```
   # view.py
   def map(request):
       context = {}
       return render(request, 'map.html', context)
   
   # url.py
       url(r'^map.html$', view.map),
   ```

   这样独立的map.html能访问了。

   加入iframe：

   [网页中插入百度地图的方法_安科网](https://www.ancii.com/abd8uald/)

   ```
   <iframe src="map.html" width="700" height="550" frameborder="0" scrolling="no"></iframe>
   ```

   做到这一步，iframe位置报错：

   > 127.0.0.1 拒绝了我们的连接请求

   [django解决frame拒绝问题_weixin_42886895的博客-CSDN博客_djangox-frame-options](https://blog.csdn.net/weixin_42886895/article/details/88970578)

   按这里说的，在settings.py中加入：  

   ```
   X_FRAME_OPTIONS = 'ALLOWALL url'        # 这个是将值改变为可以响应  url指定地址
   ```

   就成功显示了。

   

   [调用百度地图为什么出现乱码 图标不显示-百度经验](https://jingyan.baidu.com/article/a24b33cd1685fd19fe002b89.html)

   这里能解决图标不显示的问题。

   

## 5. 能读取和写入数据

### 5.1 删除重复页面

原来的文件写了两个baby页面，一个是baby.html，一个是baby2.html。它们之间的区别只在于有没有隐藏模块。思量着合二为一。

现有能工作的代码暂存：  

```
# view.py

def savebaby(request):
    context = {}
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        context['birthtime'] = str(datetime.date(int(request.POST.get('year')), int(request.POST.get('month')), int(request.POST.get('date'))))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = time.strftime("%d/%m/%Y %H:%M:%S")
        context['tips'] = "宝宝：%s" % context['name']
    file = open('./babyinfo.txt', 'w')
    file.write(context['name'] + '\n')
    file.write(context['gender'] + '\n')
    file.write(context['birthtime'] + '\n')
    file.write(context['momemail'] + '\n')
    file.write('宝宝信息最近更新时间：' + context['settingtime'] + '\n')
    file.close()
    return render(request, 'baby.html', context)


def baby(request):
    context = {}
    filename = './babyinfo.txt'
    if os.path.exists(filename):
        data = open(filename, 'r').readlines()
        context['tips'] = data[0]
        context['name'] = context['tips']
        context['gender'] = data[1]
        context['birthtime'] = data[2]
        context['momemail'] = data[3]
    else:
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
    return render(request, 'baby.html', context)

```

```
# urls.py

from . import view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [url(r'^$', view.index),
               url(r'^baby.html/$', view.baby, name='check'),
               url(r'^baby2.html/$', view.savebaby, name='check'),
               url(r'^history.html/$', view.saveinfo, name='info'),
               url(r'^email.html/$', view.email),
               url(r'^camera.html/$', view.camera),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

修改思路：  

view里的两个函数合二为一，如果是post方法，则写入。如果不是，则读取。

修改成功：  

```
# view.py

def baby(request):
    context = {}
    filename = './babyinfo.txt'
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        context['birthtime'] = str(datetime.date(int(request.POST.get('year')), int(request.POST.get('month')), int(request.POST.get('date'))))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = time.strftime("%d/%m/%Y %H:%M:%S")
        context['tips'] = "宝宝：%s" % context['name']
        file = open(filename, 'w')
        file.write(context['name'] + '\n')
        file.write(context['gender'] + '\n')
        file.write(context['birthtime'] + '\n')
        file.write(context['momemail'] + '\n')
        file.write('宝宝信息最近更新时间：' + context['settingtime'] + '\n')
        file.close()
        return render(request, 'baby.html', context)
    else:
        if os.path.exists(filename):
            data = open(filename, 'r').readlines()
            context['tips'] = data[0]
            context['name'] = context['tips']
            context['gender'] = data[1]
            context['birthtime'] = data[2]
            context['momemail'] = data[3]
        else:
            context['name'] = "未设置"
            context['gender'] = "未设置"
            context['birthtime'] = "未设置"
            context['momemail'] = "未设置"
            context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)
```

```
# urls.py

from . import view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [url(r'^$', view.index),
               url(r'^baby.html/$', view.baby, name='check'),
               url(r'^history.html/$', view.saveinfo, name='info'),
               url(r'^email.html/$', view.email),
               url(r'^camera.html/$', view.camera),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### 5.2 如何能存取到数据？

#### 5.2.1 urls.py  

在urls.py中，html文件与view里的函数挂钩，多了一个参数name，用来跟html中的表单挂钩。
```
 url(r'^baby.html/$', view.baby, name='check'),
```
#### 5.2.2 view.py

在view.py中，因为函数需要返回的是baby页面，而baby页面需要一个context，所以先设立一个空context和数据文件名，然后判断页面方法：如果页面方法是POST，函数就实现存储写入数据的功能；如果不是（也就是GET），函数就实现读取数据文件中的数据的功能。无论是读还是写，最终要填入cotext所有内容，页面才不出错。

#### 5.2.3 baby.html 

在baby.html中， 

##### 5.2.3.1 页面变量：
`{{tips}} {{name}}{{gender}}{{birthtime}}{{momemail}}`，这些构成了context的内容，一定要填满。

##### 5.2.3.2 form表单：

其中action中的'check'就是urls.py中的name内容。  
```
<form action={% url 'check' %} method="post">    

	{%csrf_token%}
	…………
</form>
```

##### 5.2.3.3 form表单中的文本框（接收用户输入的输入框）
```
<input name="name" type="text" /><br /><br />
<input name="gender" type="text" /><br /><br />
<input type="number" name="year" min="2005" max="2020" step="1" value="2015">年
<input type="number" name="month" min="1" max="12" step="1" value="1">月
<input type="number" name="date" min="1" max="31" step="1" value="15">日<br /><br />
<input name="email" type="text" /><br /><br />
<input type="submit" align="left" value="保存" name="savebaby" />
```
这些name决定了view中baby函数从哪里接收用户输入：

view.py中是这样接收的，用`request.POST.get('name')`来接收：  

```
if request.method == 'POST':
   context['name'] = request.POST.get('name')
   context['gender'] = request.POST.get('gender')
   context['birthtime'] = str(datetime.date(int(request.POST.get('year')), int(request.POST.get('month')), int(request.POST.get('date'))))
   context['momemail'] = request.POST.get('email')
   context['settingtime'] = time.strftime("%d/%m/%Y %H:%M:%S")
   context['tips'] = "宝宝：%s" % context['name']
```

##### 5.2.3.4 输入和输出的显示与隐藏

这个页面同时有输入模块和输出模块，所以用了一个js来调节各自的显示和隐藏。

```
<input type="button" onclick="showAndHidden1();" align="left" value="更新宝宝信息："/> 

<script type="text/javascript"> 
	function showAndHidden1(){ 
		var div1=document.getElementById("div1"); 
		if(div1.style.display=='none') div1.style.display='block';
		if(div2.style.display=='block') div2.style.display='none';  
		} 
</script>
```

## 6. SQL数据库

[Django中SQLite3的使用 - qq_34485436的博客 - CSDN博客](https://blog.csdn.net/qq_34485436/article/details/72805908)
[Django 模型 | 菜鸟教程](https://www.runoob.com/django/django-model.html)
[Django数据库的使用(sqlite) - - ITeye博客](https://2914905399.iteye.com/blog/2321530)

### 6.1 配置数据库

和数据库关联，需要另外创建一个app。好在我安装的这个，默认就是采用了sqlite3数据库。
settings.py下：

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
以上内容，ENGINE表示使用SQLite3数据库，NAME表示创建了一个名字为db.sqlite3的数据库。 

startproject之后，要赶紧到settings里去改数据库文件名（上面的`'db.sqlite3'`），否则等到runserver后这个文件就建立起来了。

检验数据库配置是否有问题的代码：  

在命令行输入`python manage.py shell`后，

```
>>> from django.db import connection
>>> cursor = connection.cursor()

```
如果没有出错信息，则数据库配置正确。

### 6.2 创建app

#### 6.2.1 了解project 和 app 之间的区别

> project 和 app 之间到底有什么不同呢?它们的区别就是一个是配置另一个是代码: 一个project包含很多个Django app以及对它们的配置。 
> project的作用是提供配置文件，比方说哪里定义数据库连接信息, 安装 的app列表， TEMPLATE_DIRS ，等等。 
> 一个app是一套Django功能的集合，通常包括模型和视图，按Python的包结构的方 式存在。 

#### 6.2.2 创建数据库的app

在项目根目录下命令行输入：  

```
django-admin startapp TestModel
```
根目录下就多了一个文件夹TestModel，其中有一大堆文件。

在settings.py中找到INSTALLED_APPS这一项，
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',               # 添加此项
)

```
#### 6.2.3 验证模型是否有效

在命令行使用 `python manage.py check`，注意不是书上的validate。

[在Django中使用数据库遇到的问题 - yy_menghuanjie的博客 - CSDN博客](https://blog.csdn.net/yy_menghuanjie/article/details/51332075)

不知道这个输出代表什么：

```
System check identified no issues (0 silenced).
```

#### 6.2.4 创建数据库的数据表

修改 TestModel/models.py 文件，代码如下：
```
HelloWorld/TestModel/models.py: 文件代码：
# models.py
from django.db import models
 
class babyinfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, default='男')
    birthtime = models.DateField(default='2015-01-01')

```
需要几个表，就在models.py表中写几个类。

常见的数据类型：  
CharField, DateField, URLField, EmailField, ImageField, IntegerField  
在命令行中输入命令`python manage.py makemigrations `

没有理解这句话，还是下面这个人[Django 模型 | 菜鸟教程](https://www.runoob.com/django/django-model.html)、[在Django中使用数据库遇到的问题 - yy_menghuanjie的博客 - CSDN博客](https://blog.csdn.net/yy_menghuanjie/article/details/51332075)讲得比较好：

```
python manage.py makemigrations books    #用来检测数据库变更和生成数据库迁移文件
python manage.py migrate     #用来迁移数据库
python manage.py sqlmigrate books 0001 # 用来把数据库迁移文件转换成数据库语言
```

但是为什么我执行了几次，都说TestModel没有发生变化呢？migrations文件夹下已有的0001等文件删掉，再依次执行这两行，就又生成了新的initial文件，命令行的反馈也不再是多少个apply没有applying了。

```
python manage.py makemigrations
python manage.py migrate
```

#### 6.2.5 查看数据表内容

根据[Django 模型 | 菜鸟教程](https://www.runoob.com/django/django-model.html)这里，和manage.py并列添加了一个testdb.py，也根据它的内容修改了urls.py：

```
# testdb.py

#!/usr/bin/env python
# _*_coding:utf-8_*_

from django.http import HttpResponse
from TestModel.models import NoteRecord, BabyInfo


def testdb(request):
    test1 = NoteRecord(time='2019-06-26', age='6', record='今天第一次')
    test2 = BabyInfo(name='damao', gender='男', birthtime='2013-11-13',
                     momemail='pickle.ahcai@163.com', settingtime='2019-06-27')
    test1.save()
    test2.save()
    return HttpResponse('<p>数据添加成功</p>')
```
urls改成：

```
# urls.py

from . import view, testdb
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [url(r'^$', view.index),
               url(r'^baby.html/$', view.baby, name='check'),
               url(r'^history.html/$', view.saveinfo, name='info'),
               url(r'^email.html/$', view.email),
               url(r'^camera.html/$', view.camera),
               url(r'^testdb/$', testdb.testdb)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
按道理这时运行host+testdb/应该输出数据添加成功的字样。

但是反复提示：没有noterecord表，babyinfo表没有momemail字段。

使用shell（发现这个shell是个ipython），发现根目录下的babyinfo确实没有momemail结构：
[python中查看.db文件中表格的名字及表格中的字段 - qq_42281053的博客 - CSDN博客](https://blog.csdn.net/qq_42281053/article/details/80714344)

输入`python manage.py shell`，进入终端：  
```
import sqlite3
conn = sqlite3.connect("./babyinfo.db")
cursor = conn.cursor()
sql = """select name from sqlite_master where type='table' order by name"""
cursor.execute(sql)
result = cursor.fetchall()
print result
print type(result)
conn.close()
```
以上也可以用with写成一大段：
```
In [1]: import sqlite3                                                          

In [2]: 
with sqlite3.connect('./babygrow.db') as conn: 
	cursor = conn.cursor() 
	sql = '''select name from sqlite_master where type='table' order by name''' 
	cursor.execute(sql) 
	result = cursor.fetchall() 
	print(result)   
```

输出结果为：
```
[
('TestModel_babyinfo',), 
('auth_group',), 
('auth_group_permissions',), 
('auth_permission',), 
('auth_user',), 
('auth_user_groups',), 
('auth_user_user_permissions',), 
('django_admin_log',), 
('django_content_type',), 
('django_migrations',), 
('django_session',), 
('sqlite_sequence',)]
```
我完全不知道这些是啥，哪来这么多Table（数据表）。

```
import sqlite3
conn = sqlite3.connect("./babyinfo.db")
cursor = conn.cursor()
sql = """pragma table_info(TestModel_babyinfo)"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
conn.close()

```
输出为：

```
[
(0, 'id', 'integer', 1, None, 1), 
(1, 'name', 'varchar(20)', 1, None, 0), 
(2, 'birthtime', 'date', 1, None, 0), 
(3, 'gender', 'varchar(2)', 1, None, 0)
]
```

根据这个结果，改testdb文件： 

```
# testdb.py

#!/usr/bin/env python
# _*_coding:utf-8_*_

from django.http import HttpResponse
from TestModel.models import BabyInfo


def testdb(request):
    test2 = BabyInfo(name='damao', gender='男', birthtime='2013-11-13')
    test2.save()
    return HttpResponse('<p>数据添加成功</p>')
```

结果仍然反馈说`table TestModel_babyinfo has no column named momemail`

删掉原先的initial，在models中删掉momemail和settings两个字段。在命令行重新运行以下两个命令：  

```
python manage.py makemigrations TestModel
python manage.py migrate

```
再在浏览器端运行`http://127.0.0.1:5050/testdb/`，显示数据添加成功。

再次进入shell，运行以下：  

```
In [1]: import sqlite3                                                                     

In [2]: 
with sqlite3.connect('./babyinfo.db') as conn: 
	cursor = conn.cursor() 
	sql = '''pragma table_info(TestModel_babyinfo)''' 
	cursor.execute(sql) 
	result = cursor.fetchall() 
	print(result) 
```
输出：

```
[
(0, 'id', 'integer', 1, None, 1), 
(1, 'name', 'varchar(20)', 1, None, 0), 
(2, 'birthtime', 'date', 1, None, 0), 
(3, 'gender', 'varchar(2)', 1, None, 0)
]
```
和上面的结果没有区别。

看了还得找到查看表记录的语句看看才行。

##### 6.2.5.1 完整的数据库表建立过程

- 1. 新起了一个项目BabyGrow

在打算建立项目的/_src路径下，命令行输入：

```
django-admin.py startproject BabyGrow

```

- 2. 此时这个项目已经建立好了，settings文件中默认给了一个db.sqlite3的文件，在此时改这个文件名为我想要的babygrow.db：

```
# settings.py

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'babygrow.db'),
    }
}
```

- 3. 启动服务以创建这个数据库

进入BabyGrow根目录，运行`python manage.py runserver 65432`，空数据库'babygrow.db'就出现在manage.py所在的文件夹下。  

- 4. 退出runserver，运行`python manage.py shell`，检查数据库配置是否正确：   

```
from django.db import connection                                        
cursor = connection.cursor()    
```

无报错信息，输入exit退出shell。 

- 5. 构建模型

仍然在BabyGrow根目录下（与manage.py同一目录），运行`django-admin startapp BabyGrowModel`构建app。 

- 6. 到settings中去添加这个app：

```
# settings.py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BabyGrowModel'
]
```

- 7. 在根目录命令行下验证模型是否有效：

```
python manage.py check
```

- 8. 添加表结构  

从根目录转向刚才建立的模型目录：`./BabyGrowModel/`，到models.py中添加表：

```
# models.py

from django.db import models

# Create your models here.


class BabyInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, default='男')
    birthtime = models.CharField(max_length=15)
    momemail = models.CharField(max_length=40)
    settingtime = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class NoteRecord(models.Model):
    time = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    record = models.CharField(max_length=150)

    def __str__(self):
        return self.record


```

- 9. 创建表

然后回到根目录下（其实命令行一直在根目录），运行以下两句按照models的要求创建表：

```
python manage.py makemigrations
python manage.py migrate
```

根据输出，表格是创建好了。此时可以看到`./BabyGrowModel/migrations`下生成了一个0001_initial.py文件，其中是创建表的过程。这两个表都在babygrow.db数据库中。

- 10. 检查表格是否创建成功

运行`python manage.py shell`进入shell，检查数据库中是否存在这两个表，表的字段是否如0001_initial.py所述：

```
# 检查有哪些表
In [1]: import sqlite3                                                          

In [2]: 
with sqlite3.connect('./babygrow.db') as conn: 
    cursor = conn.cursor() 
    sql = '''select name from sqlite_master where type='table' order by name''' 
    cursor.execute(sql) 
    result = cursor.fetchall() 
    print(result) 
```
输出：

```
[
('BabyGrowModel_babyinfo',), 
('BabyGrowModel_noterecord',), 
('auth_group',), 
('auth_group_permissions',), 
('auth_permission',), 
('auth_user',), 
('auth_user_groups',), 
('auth_user_user_permissions',), 
('django_admin_log',), 
('django_content_type',), 
('django_migrations',), 
('django_session',), 
('sqlite_sequence',)
]
```
果然依旧是模型名加类名构成的table名称。

```
# 检查表头内容（字段）

In [5]: 
with sqlite3.connect('./babygrow.db') as conn:   
    cursor = conn.cursor()   
    sql = '''pragma table_info(BabyGrowModel_babyinfo)'''   
    cursor.execute(sql)   
    result = cursor.fetchall()   
    print(result) 

In [6]: 
with sqlite3.connect('./babygrow.db') as conn:   
    cursor = conn.cursor()   
    sql = '''pragma table_info(BabyGrowModel_noterecord)'''   
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result) 

```

结果分别输出：

```
[
(0, 'id', 'integer', 1, None, 1), 
(1, 'name', 'varchar(20)', 1, None, 0),
(2, 'gender', 'varchar(2)', 1, None, 0),
(3, 'birthtime', 'varchar(15)', 1, None, 0),
(4, 'momemail', 'varchar(40)', 1, None, 0),
(5, 'settingtime', 'varchar(20)', 1, None, 0)]

[
(0, 'id', 'integer', 1, None, 1),
(1, 'time', 'varchar(20)', 1, None, 0),
(2, 'age', 'varchar(5)', 1, None, 0),
(3, 'record', 'varchar(150)', 1, None, 0)]
```

和models里的class一致。

读取数据表里的记录：

```
with sqlite3.connect('./babygrow.db') as conn:       
    cursor = conn.cursor()       
    sql = '''select * from BabyGrowModel_babyinfo'''       
    cursor.execute(sql)       
    result = cursor.fetchall()       
    print(result)  
```

删除某表格：

```
with sqlite3.connect('./babygrow.db') as conn:         
    cursor = conn.cursor()         
    sql = '''drop table noterecord'''         
    cursor.execute(sql) 
```

#### 6.2.6 和页面结合

[Django简单项目示例，数据库使用自带的sqlite3 - xuerba的博客 - CSDN博客](https://blog.csdn.net/qq_31489933/article/details/84848784)，这里有个结合页面的实例。

【奇怪的错误】

新建的项目babygrow，忘记在settings里设置模板位置了，于是就什么都找不到了：

```
TemplateDoesNotExist at /
```
每个页面都这样。搜了一下，感觉要回去查看一下settings，果然模板dir那里是空列表。改完至少页面出来了。

又意外发现baby页面居然打开了index内容。这是怎么回事呢？发现在if 方法为post的else中，居然返回index，想想这是写错了吧。于是赶紧改成baby.index，果然页面内容就不错了。一开始还想不管三七二十一先把这个else注释掉再说呢。幸好幸好……

baby页面正常后，就开始添加宝宝信息，居然是可以的。

添加完宝宝信息，再添加历史记录，居然也是可以的。

现在唯一的问题就是历史记录页面读取的内容和宝宝信息页面读取的内容了。真没想到上周抓狂到几乎又要睁眼瞎的问题，竟然是这样两个小问题引起的。

改得差不多了。

```
# view.py

def baby(request):
    context = {}
    filename = './babygrow.db'
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        context['birthtime'] = str(datetime.date(int(request.POST.get('year')), int(request.POST.get('month')), int(request.POST.get('date'))))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = str(time.strftime("%d/%m/%Y %H:%M:%S"))
        context['tips'] = "宝宝：%s" % context['name']
        baby = BabyInfo(name=context['name'],
                        gender=context['gender'],
                        birthtime=context['birthtime'],
                        momemail=context['momemail'],
                        settingtime=context['settingtime'])
        baby.save()
        return render(request, 'baby.html', context)
    else:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            cursor.execute('''select name from BabyGrowModel_babyinfo order by settingtime desc limit 0,1''')
            name = str(cursor.fetchall())[3:-4]
            context['name'] = name
            context['tips'] = u"宝宝：%s" % name
            cursor.execute('''select gender from BabyGrowModel_babyinfo order by settingtime desc limit 0,1''')
            context['gender'] = str(cursor.fetchall())[3:-4]
            cursor.execute('''select birthtime from BabyGrowModel_babyinfo order by settingtime desc limit 0,1''')
            context['birthtime'] = str(cursor.fetchall())[3:-4]
            cursor.execute('''select momemail from BabyGrowModel_babyinfo order by settingtime desc limit 0,1''')
            context['momemail'] = str(cursor.fetchall())[3:-4]
            return render(request, 'baby.html', context)

```

这是很有代表性的一段：输入也在此，输出也在此。还有针对数据表的排序筛选。

读取baby信息独立成函数：

```
def readBaby():
    filename = './babygrow.db'
    if os.path.exists(filename):
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            sql1 = '''
                    select name from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                  '''
            cursor.execute(sql1)
            name = str(cursor.fetchall())[3:-4]
            sql2 = '''
                    select gender from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                  '''
            cursor.execute(sql2)
            gender = str(cursor.fetchall())[3:-4]
            sql3 = '''
                    select birthtime from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                    '''
            cursor.execute(sql3)
            birthtime = str(cursor.fetchall())
            birthdate = datetime.datetime(int(birthtime[3:7]),
                                          int(birthtime[8:10]),
                                          int(birthtime[11:13]))
            age = (datetime.datetime.now() - birthdate).days
            birthtime = birthtime[3:-4]
            sql4 = '''
                    select momemail from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                    '''
            cursor.execute(sql4)
            momEmail = str(cursor.fetchall())[3:-4]
            babyDict = dict(zip(
                ['name', 'gender', 'birthtime', 'age', 'momemail'],
                [name, gender, birthtime, age, momEmail]))
            return babyDict
```

感觉有点冗余。

改成了这样：

```
def readBaby():
    filename = './babygrow.db'
    if os.path.exists(filename):
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            sql = '''
                    select * from BabyGrowModel_babyinfo
                    order by settingtime desc
                  '''
            cursor.execute(sql)
            babyList = cursor.fetchall()
            name = str(babyList[0][1])
            gender = str(babyList[0][2])
            birthtime = str(babyList[0][3])
            birthdate = datetime.datetime(int(birthtime[0:4]),
                                          int(birthtime[5:7]),
                                          int(birthtime[8:10]))
            age = (datetime.datetime.now() - birthdate).days
            momEmail = str(babyList[0][4])
            babyDict = dict(zip(
                ['name', 'gender', 'birthtime', 'age', 'momemail'],
                [name, gender, birthtime, age, momEmail]))
            return babyDict
```

少了多次重复读取数据库的操作，读出来的数据还直接是不带引号的。

#### 6.2.7 在程序中建立数据表

现在的问题是：db文件能否像txt文件一样，是由程序创建的，而不是先创建好数据库再写程序呢？

试了一下拿掉已经建立好的database文件，首页可以允许无宝宝信息时的状态，其他页面不行。试着在首页新建宝宝信息，会返回无此表的提示。因为只是建立了一个空数据库文件，数据库中压根没有数据表，更别提字段了。

直接把models下的class搬到view里来，不管用。

以baby为例：

```
def baby(request):
    context = {}
    if not os.path.exists(filename) or readBaby()['name'] == '':
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        context['birthtime'] = str(datetime.date(
            int(request.POST.get('year')),
            int(request.POST.get('month')),
            int(request.POST.get('date'))))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = str(time.strftime("%Y/%m/%d %H:%M:%S"))
        ID = readBaby()['ID'] + 1
        data = (ID, context['name'], context['gender'],
                context['birthtime'], context['momemail'],
                context['settingtime'])
        createBaby(data)
        '''
        baby = BabyInfo(name=context['name'],
                        gender=context['gender'],
                        birthtime=context['birthtime'],
                        momemail=context['momemail'],
                        settingtime=context['settingtime'])
        baby.save()
        '''
        return render(request, 'baby.html', context)
    else:
        context['name'] = readBaby()['name']
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
        context['gender'] = readBaby()['gender']
        context['birthtime'] = readBaby()['birthtime']
        context['momemail'] = readBaby()['momemail']
        return render(request, 'baby.html', context)
```

```
def createBaby(data):
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists babyinfo (
        ID num, name text, gender text,
        birthtime text, momemail text,
        settingtime text
        )'''
        cursor.execute(sql1)
        sql2 = '''
        insert into babyinfo (
        ID, name, gender, birthtime, momemail, settingtime)
        values (?,?,?,?,?,?) '''
        cursor.execute(sql2, data)
```

```
def readBaby():
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists babyinfo (
        ID num, name text, gender text,
        birthtime text, momemail text,
        settingtime text
        )'''
        cursor.execute(sql1)
        sql = '''
        select * from babyinfo
        order by settingtime desc
        '''
        cursor.execute(sql)
        babyList = cursor.fetchall()
        if babyList != []:
            ID = babyList[0][0]
            name = str(babyList[0][1])
            gender = str(babyList[0][2])
            birthtime = str(babyList[0][3])
            birthdate = datetime.datetime(int(birthtime[0:4]),
                                          int(birthtime[5:7]),
                                          int(birthtime[8:10]))
            age = (datetime.datetime.now() - birthdate).days
            momEmail = str(babyList[0][4])
        else:
            ID = 0
            name = ''
            gender = ''
            birthtime = ''
            age = ''
            momEmail = ''
        babyDict = dict(zip(
            ['ID', 'name', 'gender', 'birthtime', 'age', 'momemail'],
            [ID, name, gender, birthtime, age, momEmail]))
        return babyDict
```
以上实现了手动建立数据库文件，并改进了以前每个表格新建一个库的做法，在同一个库中新建文件。

在解决历史记录无内容时页面提示“用户添加信息”时，出了问题。

```
def saveRecord(request):
    context = {}
    if not os.path.exists(filename) or readBaby()['name'] == '':
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)
    else:
        if request.method == 'POST':
            if readRecord() != []:
                ID = readRecord()[0][0] + 1
            else:
                ID = 1
            settingtime = time.strftime('%Y/%m/%d %H:%M:%S')
            age = readBaby()['age']
            record = request.POST.get('newline')
            data = (ID, settingtime, age, record)
            createRecord(data)
            '''
            note = NoteRecord(time=settingtime,
                              age=age,
                              record=record)
            note.save()
            '''
            context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
            context['historylabel'] = readRecord()
            return render(request, 'history.html', context)
        elif not os.path.exists(filename) or readRecord() == []:
            context['tips'] = '%s，今天%s天 \n尚无记录，赶快添加吧！' % (readBaby()['name'], readBaby()['age'])
            return render(request, 'index.html', context)
        else:
            context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
            context['historylabel'] = readRecord()
            return render(request, 'history.html', context)
```

`if post`这一段，如果if的代码段和elif的代码段互换，就会存不了数据。

另外，事实证明，history函数真的没有用。再次删了。

为了有据可查，到目前为止的完整view.py，备注一下：

```
# view.py

#!/usr/bin/env python
# _*_coding:utf-8_*_

from django.shortcuts import render
import os
import sqlite3
import datetime
import time
# from BabyGrowModel.models import BabyInfo, NoteRecord

filename = './babygrow.db'


def index(request):
    context = {}
    if not os.path.exists(filename) or readBaby()['name'] == '':
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
        return render(request, 'index.html', context)


def baby(request):
    context = {}
    if not os.path.exists(filename) or readBaby()['name'] == '':
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        context['birthtime'] = str(datetime.date(
            int(request.POST.get('year')),
            int(request.POST.get('month')),
            int(request.POST.get('date'))))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = str(time.strftime("%Y/%m/%d %H:%M:%S"))
        ID = readBaby()['ID'] + 1
        data = (ID, context['name'], context['gender'],
                context['birthtime'], context['momemail'],
                context['settingtime'])
        createBaby(data)
        age = (datetime.datetime.now() - datetime.datetime(
            int(request.POST.get('year')),
            int(request.POST.get('month')),
            int(request.POST.get('date')))).days
        context['tips'] = '%s，今天%s天' % (context['name'], age)
        '''
        baby = BabyInfo(name=context['name'],
                        gender=context['gender'],
                        birthtime=context['birthtime'],
                        momemail=context['momemail'],
                        settingtime=context['settingtime'])
        baby.save()
        '''
        return render(request, 'baby.html', context)
    else:
        if not os.path.exists(filename) or readBaby()['name'] == '':
            context['name'] = "未设置"
            context['gender'] = "未设置"
            context['birthtime'] = "未设置"
            context['momemail'] = "未设置"
            context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        else:
            context['name'] = readBaby()['name']
            context['tips'] = '%s，今天%s天' % (context['name'], readBaby()['age'])
            context['gender'] = readBaby()['gender']
            context['birthtime'] = readBaby()['birthtime']
            context['momemail'] = readBaby()['momemail']
        return render(request, 'baby.html', context)


def saveRecord(request):
    context = {}
    if not os.path.exists(filename) or readBaby()['name'] == '':
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)
    else:
        if request.method == 'POST':
            if readRecord() != []:
                ID = readRecord()[0][0] + 1
            else:
                ID = 1
            settingtime = time.strftime('%Y/%m/%d %H:%M:%S')
            age = readBaby()['age']
            record = request.POST.get('newline')
            data = (ID, settingtime, age, record)
            createRecord(data)
            '''
            note = NoteRecord(time=settingtime,
                              age=age,
                              record=record)
            note.save()
            '''
            context['tips'] = '%s，今天%s天' % (readBaby()['name'], age)
            context['historylabel'] = readRecord()
            return render(request, 'history.html', context)
        elif not os.path.exists(filename) or readRecord() == []:
            context['tips'] = '%s，今天%s天 \n尚无记录，赶快添加吧！' % (
                readBaby()['name'], readBaby()['age'])
            return render(request, 'index.html', context)
        else:
            context['tips'] = '%s，今天%s天' % (
                readBaby()['name'], readBaby()['age'])
            context['historylabel'] = readRecord()
            return render(request, 'history.html', context)


def validateEmail(email):
    import re
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return 1
    return 0


def email(request):
    context = {}
    if not os.path.exists(filename) or readBaby()['name'] == '':
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
        context['momemail'] = readBaby()['momemail']
        return render(request, 'email.html', context)


def camera(request):
    context = {}
    if not os.path.exists(filename) or readBaby()['name'] == '':
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
        context['photoid'] = '3'
        context['photoname'] = readBaby()
        return render(request, 'camera.html', context)


def createBaby(data):
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists babyinfo (
        ID num, name text, gender text,
        birthtime text, momemail text,
        settingtime text
        )'''
        cursor.execute(sql1)
        sql2 = '''
        insert into babyinfo (
        ID, name, gender, birthtime, momemail, settingtime)
        values (?,?,?,?,?,?) '''
        cursor.execute(sql2, data)


def createRecord(data):
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists noterecord (
        ID num, time text, age text, record text
        )'''
        cursor.execute(sql1)
        sql2 = '''
        insert into noterecord (
        ID, time, age, record)
        values (?,?,?,?) '''
        cursor.execute(sql2, data)


def readBaby():
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists babyinfo (
        ID num, name text, gender text,
        birthtime text, momemail text,
        settingtime text
        )'''
        cursor.execute(sql1)
        sql = '''
        select * from babyinfo
        order by settingtime desc
        '''
        cursor.execute(sql)
        babyList = cursor.fetchall()
        if babyList != []:
            ID = babyList[0][0]
            name = str(babyList[0][1])
            gender = str(babyList[0][2])
            birthtime = str(babyList[0][3])
            birthdate = datetime.datetime(int(birthtime[0:4]),
                                          int(birthtime[5:7]),
                                          int(birthtime[8:10]))
            age = (datetime.datetime.now() - birthdate).days
            momEmail = str(babyList[0][4])
        else:
            ID = 0
            name = ''
            gender = ''
            birthtime = ''
            age = ''
            momEmail = ''
        babyDict = dict(zip(
            ['ID', 'name', 'gender', 'birthtime', 'age', 'momemail'],
            [ID, name, gender, birthtime, age, momEmail]))
        return babyDict


def readRecord():
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists noterecord (
        ID num, time text, age text, record text
        )'''
        cursor.execute(sql1)
        sql = '''
        select * from noterecord
        order by time desc
        '''
        cursor.execute(sql)
        historylabel = cursor.fetchall()
        return historylabel

```

有些纯粹是为了不超过79字符转弯的。。。。。

这个版本：  

1. 能从零开始创建数据库及其中表格。无需依赖于models事先创建。
2. 一个数据库含多个表格，不像15年的版本那样每个表格都占据了一个数据库。
3. 因为数据库文件是在程序运行起来后创建的，所以有初始状态：包括没有宝宝个人信息时、有宝宝个人信息没有记录内容时。没有宝宝个人信息时，各个页面都指向添加新宝宝这个内容。有个人信息没有记录内容时，历史记录这个页面指向添加新内容这个页面。
4. 读取数据库的部分，单独成为函数，可以复用。其中也考虑了数据表内容为空的情况。
5. 保存内容到数据库的部分，单独成为函数。
6. 依赖于读取数据库的过程是独立的，发送email页面中，email可以读取。虽然目前还没有添加发送功能。
7. 宝宝信息和记录内容这两个页面，接受用户输入时，除了存数据库之外，也都包含读取数据库内容到页面上来展示的功能。
8. 注释部分，是使用models创建好的数据库和表格进行操作。不能考虑初始状态。

datetime有两种，一种是datetime.datetime，另一种是datetime.date。前者表达现在是.now()，后者表达今天是.today()

居然还有这种神奇的操作：`name = gender = birthtime = age = momEmail = ''`，真没见过。切记，不能写成`name, gender, birthtime, age, momEmail = ''`，否则需要五个`''`。

## 7. 实现多宝宝管理

### 7.1 Django模板中的下拉框

用select

[django中 下拉框 - 程序园](http://www.voidcn.com/article/p-rozhutoq-gb.html)



## 8. 做带后台管理的新闻模块

[一杯茶的时间，上手 Django 框架开发 - 掘金](https://juejin.im/post/5dff47ec6fb9a0164c7bb171)

### 8.1 创建app（application）

```
python manage.py startapp news
```

添加到settings：

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
]
```

### 8.2 加内容

独立的app，有自己独立的views和urls，所以现在主站的urls里要加一句：

```
path('news', include('news.urls')),
```

用来替代原来那句`view.news`，这样访问主站/news时，就会去app下的urls文件里找路由。新闻模块会有很多页面，独立到app下面的url中，好管理。

主站view里的那个news函数也可以换地方了，换到news app下面的views里去。

现在来写news app下的urls。

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='index'),
]

```

它的意思是：app的主页（就整站来说，就是/news这个页面），要调用app下的views文件中的news函数。

想到这个模块后面还有挺多页面，这个函数叫news太不方便，还是改为index吧。

```
# news app下面的views.py

# Create your views here.
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'news.html', context)

```

```
# news app下面的urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

```

现在去访问主站/news，像之前一样显示了那个带导航菜单和底部foot的模板页面。惊讶的是，这整个过程中，并没有另外再造一个templates文件夹来。news.html文件仍然在原处未动。

仍然是新闻模块会有很多页面的问题，在这个主站templates下，建立一个news文件夹。未来把新闻模块所有网页都放在其中。这样做，上面的index函数，就要把`news.html`换成`news/news.html`，那索性不叫`news.html`了，也叫`index.html`吧。



### 8.3 创建数据库

到news app下的models.py中去创建数据结构。

以前一直不知道我建立的testModel是个啥。现在做新闻模块知道了，它就是这个网站的一个子模块。可以是新闻，可以是解决方案，可以是案例。反正是个站内小站。

```
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.title

```

数据结构创建好后，用manage.py创建迁移文件：

```
 python manage.py makemigrations
```

运行结果如下：

```
Migrations for 'news':
  news\migrations\0001_initial.py
    - Create model Post
```

现在进行数据库迁移：

```
python manage.py migrate
```

运行过程：  

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  Applying news.0001_initial... OK
```

前面17行，对应了启动服务器时那句：  

```
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

最后一行是news模块的。



### 8.4 创建后台管理员

其实不能叫创建后台，后台早就有了，admin页面一直在那里。现在只是创建管理员而已：

```
python manage.py createsuperuser
```

创建如下：

```
Username (leave blank to use 'asus'): admin
Email address: caimeijuan@emapgis.com
Password:
Password (again):
Superuser created successfully.
```

配置后台管理接口：

在 news/admin.py 中填入代码如下：

```
from django.contrib import admin

from .models import Post

admin.site.register(Post)
```

### 8.5 后台增加文章

再进入后台管理系统，可以看到 news 应用和 Post 模型了。

此时后台可以正常工作了，不过前台还没有内容。那是因为index没有指向后台数据库。

之前的index函数：

```
def index(request):
    context = {
        'news_list': [
            {
                "title": "战疫情 | 零点坐标免费服务于沙溪镇防疫部门",
                "date": "2020-06-10",
                "content": "地理信息中心提供新冠肺炎疫情防控在线地图服务,地理信息中心提供新冠肺炎疫情防控在线地图服务,地理信息中心提供新冠肺炎疫情防控在线地图服务,锦丰镇日前使用无人机巡河，大大提高了巡河效率.",
            },
            {
                "title": "无人机在巡河方面的妙用",
                "date": "2020-05-22",
                "content": "锦丰镇日前使用无人机巡河，大大提高了巡河效率.锦丰镇日前使用无人机巡河，大大提高了巡河效率.锦丰镇日前使用无人机巡河，大大提高了巡河效率.锦丰镇日前使用无人机巡河，大大提高了巡河效率.",
            },
        ]
    }
    return render(request, 'news/index.html', context)
```

用的是字典。

现在改为：

```
from django.shortcuts import render
from .models import Post


def index(request):
    context = {
        'news_list': Post.objects.all()
    }
    return render(request, 'news/index.html', context)

```

前台可见！！！！！*★,°*:.☆(￣▽￣)/$:*.°★*  感觉尾巴要翘上天了~~~~

这里的`Post.objects.all()`值得注意一下。以前用bottle时，sqlite是要自己写SQL语句潜入程序的，现在为什么没有写就成功了呢？就是这句话起的作用。

一杯茶作者说：

> 强大的 ORM（Object Relation Mapping，对象关系映射）模块，使得用 Python 操作数据库非常轻松，免去了使用 SQL 的麻烦。
>
> 简单来说，ORM 能够将面向对象的代码转换成相应的 SQL 语句，从而对数据库进行操作。SQL 是用于访问和处理数据库的标准的计算机语言，但是直接写在代码里面显然难以维护，而且对使用者的要求也非常高，写的糟糕的 SQL 代码查询效率非常低下。因此，使用设计良好的 ORM 不仅让代码可读性更好，也能帮助开发者进行查询优化，节省不少力气。
>
>
> 作者：图雀社区
> 链接：https://juejin.im/post/5dff47ec6fb9a0164c7bb171
> 来源：掘金
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

一些简单的 Django ORM 例子：

```
# 查询所有模型
# 等价于 SELECT * FROM Blog
Blog.objects.all()

# 查询单个模型
# 等价于 SELECT * FROM Blog WHERE ID=1
Blog.objects.get(id=1)

# 添加单个模型
# 等价于 INSERT INTO Blog (title, content) VALUES ('hello', 'world')
blog = Blog(title='hello', content='world')
blog.save()
```

### 8.6 增加新字段

新增一个abstract摘要字段。按一杯茶作者所说，先在models.py中增加字段：

```
abstract = models.TextField()
```

然后让manage.py去makemigrations。但是出错了：  

```
>>> python manage.py makemigrations
You are trying to add a non-nullable field 'abstract' to post without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
```

原来新增字段，是要有个默认值的。或者设置null为True。null值默认是False，就是不允许空的意思。于是改models.py：

```
abstract = models.TextField(null=True)
```

现在makemigrations不出错了。  

继续运行` python manage.py migrate`，打开后台，每篇文章都有了摘要字段。

这时想要让前台显示的字段发生变化，只要改变index.html里的字段就好了，无须再更改index函数。

#### 附：ORM教程

[Django ORM常用操作介绍（新手必看）-《Django 2.0入门文档手册》 - Python学习网](https://www.py.cn/manual/django-orm-operating.html)



### 8.7 文章排序

[Django中对数据查询结果进行排序的方法_python_脚本之家](https://www.jb51.net/article/69602.htm)

在models.py中可以指定默认排序方法：

```
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    abstract = models.TextField(null=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
```

注意：负号是加在引号内部的。加了负号表示从最新时间往前排，不加表示从最早时间往后排。



[Django-ORM 之查询排序 | Python 技术论坛](https://learnku.com/articles/39113)

这个排序语句，不知道加在哪里。它是优先于上面那个统一默认排序的。



### 8.8 文章分页

一开始想的是找个css样式，把页码导航先写出来。后来一想，没有变量，写出来也是空壳子啊。结果就搜到了Django自己就有这个模块。怪不得称利器！啥都有。

[使用 Django Pagination 实现简单的分页功能 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1099696)

引入了新的模块`from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger`，专门用来分页的。index函数要作如下更改，再不能一股脑儿在一个页面展示了：

```
# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def index(request):
    news_list = Post.objects.all()
    paginator = Paginator(news_list, 5)
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    context = {
        'news_list': news_list
    }
    return render(request, 'news/index.html', context)

```

分页的功能就做好了。

下面只要在前台添上页码导航就行了：

```
<div class="pagination">
    {% if news_list.has_previous %}
    	<a href="?page={{news_list.previous_page_number}}">上一页</a>
    {% endif %}
    <span class="pagination">
    	第 {{ news_list.number }} 页 / 共 {{ news_list.paginator.num_pages }} 页
    </span>
    {% if news_list.has_next %}
    	<a href="?page={{news_list.next_page_number}}">下一页</a>
    {% endif %}                
</div>
```



道理上说，也可以把最新新闻条目放到首页上去了。明天可以考虑试试。

