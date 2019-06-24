# Django

[Django 教程 | 菜鸟教程](https://www.runoob.com/django/django-tutorial.html)

《The Django Book》（中文版），这是一本教材。感觉有点旧，还是2008年的。
最新版：[Mastering Django 2 – The Book - Python Django Tutorials](https://djangobook.com/)

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
注意，url函数的正则表达式中，**^后面不能再加`/`**，直接加路径名称（比如time）。

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
from django.template import Template, Context t = Template('Item 2 is {{ items.2 }}.') c = Context({'items': ['apples', 'bananas', 'carrots']}) >>> t.render(c) ```

不允许使用负数列表索引。像 {{ items.-1 }} 这样的模板变量将会引发TemplateSyntaxError 异常。 

假设你要向模板传递一个 Python 字典。要**通过字典键访问该字典的值**，可使用一个句点:
```
from django.template import Template, Context person = {'name': 'Sally', 'age': '43'} t = Template('{{ person.name }} is {{ person.age }} years old.') 
c = Context({'person': person}) t.render(c)
```
输出：  
``` 'Sally is 43 years old.' 
```
同样，也可以通过句点来**访问对象的属性**。

比方说， Python 的 datetime.date 对象有 year 、 month 和 day 几个属性，你同样可以在模板中使用句点来访问这些属性: 
```
from django.template import Template, Context 
import datetime d = datetime.date(1993, 5, 2) d.year 
（输出）1993 d.month （输出）5 d.day （输出）2 t = Template('The month is {{ date.month }} and the year is {{ date.year }}.') >>> c = Context({'date': d}) t.render(c)
```
输出：
``` 'The month is 5 and the year is 1993.' 
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
from django.template import Template, Context t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}') 
t.render(Context({'var': 'hello'}))
```
输出：
``` 'hello -- HELLO -- False'
```

``` t.render(Context({'var': '123'}))
```
输出：  
``` '123 -- 123 -- True' 
```

注意你不能在方法调用中使用圆括号。而且也无法给该方法传递参数;你只能调用不需参数
的方法。

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

创建一个 Template 对象最简单的方法就是直接实例化它。 Template 类就在 django.template 模块中，构造函数接受一个参数。

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

t = Template("My name is {{ name }}.") c = Context({"name": "Stephane"}) t.render(c) 

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
在整个html文件的顶部，`<html>`标签之外，加上这一句：`{% load static %}`，也有写作`{% load staticfiles %}`的，亲试无影响。

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

## 5. 存取数据

[Django中SQLite3的使用 - qq_34485436的博客 - CSDN博客](https://blog.csdn.net/qq_34485436/article/details/72805908)
[Django 模型 | 菜鸟教程](https://www.runoob.com/django/django-model.html)

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


在项目根目录下命令行输入：  

```
django-admin startapp TestModel
```
根目录下就多了一个文件夹TestModel，其中有一大堆文件。

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

在命令行中输入`命令python3 manage.py makemigrations `




