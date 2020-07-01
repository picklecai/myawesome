# Django从0开始做一个网站

去年7月份想学Django，没有找到合适的教材。想把宝宝成长记录从bottle改成Django，也没有成功。现在需要做一个企业官网，脑中第一反应就是Django。于是翻出了去年的笔记，一步一步照着来，居然就理解了app的含义。原因是它本来就是为了做一个新闻资讯系统而诞生的，所以我从新闻模块入手，歪打正着，刚刚好。  

现在决定把笔记从原来的地方挪开，以利于以后查看。

## 1. 创建新项目及启动项目

### 1.1 django-admin后是否加py的问题

2020.05.27：

从这一步就很意外，和之前不一样了。这次是在windows下安装了python3.7.6和Django3.0.6后，很高兴地按照上面的方法新建项目，却没有成功。

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

针对Django3.0以上，[编写你的第一个 Django 应用，第 1 部分 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial01/)说的就是不带py的：

```
 django-admin startproject mysite
```



---

### 1.2 端口号被占用的问题

2020.06.17：

今天启动项目出现幺蛾子了。

```
 python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 17, 2020 - 11:08:34
Django version 3.0.6, using settings 'zeropoint.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Error: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
```

[Error: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。_gsls200808的专栏-CSDN博客](https://blog.csdn.net/gsls200808/article/details/52456136)

按照这个人的，在刚才的目录下输入：

```
 netstat -ano|findstr 8000
```

结果有很多：

```
 TCP    0.0.0.0:8000           0.0.0.0:0              LISTENING       2444
  TCP    0.0.0.0:18000          0.0.0.0:0              LISTENING       2444
  TCP    127.0.0.1:8000         127.0.0.1:57541        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57542        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57547        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57549        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57551        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57552        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57553        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57554        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57562        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57619        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57639        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57651        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57657        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57665        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57669        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57671        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57679        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57687        TIME_WAIT       0
  TCP    127.0.0.1:8000         127.0.0.1:57691        TIME_WAIT       0
  TCP    127.0.0.1:57541        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57542        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57546        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57547        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57548        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57549        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57550        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57551        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57552        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57553        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57558        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57562        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57579        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57592        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57604        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57619        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57623        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57634        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57635        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57637        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57639        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57643        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57645        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57651        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57657        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57659        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57662        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57663        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57669        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57671        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57681        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57685        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57687        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57689        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:57693        127.0.0.1:8000         TIME_WAIT       0
```

第二条命令：

```
 tasklist |findstr 2444
```

结果显示为：

```
CLodopPrint32.exe             2444 Services                   0      3,532 K
```

查了这个CLodopPrint32.exe，说是个web打印程序。[Lodop是什么？ - 淡定的米哥 - OSCHINA](https://my.oschina.net/miger/blog/261142)

这两天也没有做什么跟web打印有关的事情啊。和前天的区别在于：昨天成功安装了国信CA助手。于是停掉了国信CA和行助手两个助手。但也没有什么帮助。

使用第三条命令：

```
 taskkill /pid 2444 /F
错误: 无法终止 PID 为 2444 的进程。
原因: 拒绝访问。
```

在任务管理器中停止行助手和国信CA助手，也没有帮助。等等，突然发现任务管理器里真的有这个进程：

> CLodopPrint32.exe
> 文件描述：Web打印服务C-Lodop ()
> 创建时间：‎2020‎年‎6‎月‎15‎日，‏‎16:35:09

手动停止这个进程。再运行runserver，果然成功了。

### 1.3 端口继续被占用

2020.06.19：

启动后，出现：

```
[19/Jun/2020 13:10:20] "GET /c_hello?asker=backuper HTTP/1.1" 404 3093
Not Found: /c_hello
```

搜索了，又说被占用了。敢情表现还不一样啊。确实不一样，上一个占用，服务器是无法运行起来的，但这次，服务器运行起来了。只是刚才这个提示老刷屏。

```

PS C:\Users\asus> netstat -ano|findstr 8000
  TCP    0.0.0.0:8000           0.0.0.0:0              LISTENING       16096
  TCP    0.0.0.0:18000          0.0.0.0:0              LISTENING       16096
  TCP    127.0.0.1:8000         0.0.0.0:0              LISTENING       13108
  TCP    127.0.0.1:18000        127.0.0.1:56939        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56942        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56944        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56949        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56953        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56958        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56960        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56963        TIME_WAIT       0
  TCP    127.0.0.1:18000        127.0.0.1:56967        TIME_WAIT       0
  TCP    127.0.0.1:56938        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56941        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56943        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56948        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56952        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56957        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56959        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56962        127.0.0.1:8000         TIME_WAIT       0
  TCP    127.0.0.1:56966        127.0.0.1:8000         TIME_WAIT       0
  TCP    [::]:8000              [::]:0                 LISTENING       16096
```

继续看看16096是谁：

```
 tasklist |findstr 16096
CLodopPrint32.exe            16096 Console                    5      9,708 K
```

还是它啊，老熟人啦。我现在知道了，这是国信CA助手带来的。

改它的端口号，测试后，发现一个不占用，另一个还在占用，而且18000还不能更改。

从任务管理器里停掉这个进程，马上它又自己启动了。

在win启动项里去掉它，仍然会开机启动。在它自己的菜单里停掉服务，仍然没有用。

我一气之下，卸载了这个软件。

于是，世界一下子清净了。但愿下个月启动CA不成功时能想到这里吧。现在不管了。

## 2. 使用模板

根目录下建立一个templates文件夹，其中建立nav.html、frame.html后，建立各个成品页码，如index.html。

### 2.1 templates路径设置

在正式开始写页面之前，得在设置中做好templates的路径：

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



### 2.2 模板页面

打算用nav作为顶部导航菜单部分的模板，frame作为全页面的模板。

```
# nav.html的内容如下：

{% load static %}
<nav>
    <a href="/">
        <img src="{% static '/images/logo.png' %}">
        <p class="comName">零点坐标 </p>
    </a>
    <ul> 
        <li><a href="/">首页</li>  
        <li><a href="/product">产品服务</li> 
        <li><a href="/solution">解决方案</li>
        <li><a href="/case">应用案例</li>
        <li><a href="/news">新闻资讯</li>
        <li><a href="/about">关于我们</li>
    </ul>
</nav>
<div class="tel">
    <img src="{% static '/images/tel.png' %}">186-8888-6666</img>
    <p>工作时间：9:00-17:30</p>
    <a href=""></a>
</div>
```

如果不是有静态文件（图片）要引用的话，这个导航条文件都可以看看不出来是模板文件。

frame.html文件更简单，只要各个部分都有就行：

```
# frame.html的内容

<head>
        {% load static %}
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="{% static '/styles/main.css' %}">
        <title>{% block title %}{% endblock %}</title>
        <meta name="description" content="{% block description %}{% endblock %}">
</head>
<body>
    {% block content %}{% endblock %}
    <div id="foot">
        <p>Copyright 2020-2022 © 苏州零点坐标信息技术有限公司</p>
        <p>All Rights Reserved   苏ICP备08000108号</p>
    </div>
</body>
```

这个文件的要点：

1. 静态文件是css样式文件
2. head部分，title、description是变量；body部分，content是变量。
3. foot部分统一

引用它们的文件，建立一个全站首页index看看：

```
# index.html的内容：

<!DOCTYPE html>
<html>
    {% extends 'frame.html' %}
    {% load static %}
    {% block title %}Home-Zeropoint IT{% endblock %}
    {% block description %}我们在美丽的太湖之滨。{% endblock %}
    <body>
        {% block content %}
        <div class="banner">
            <img id="placeholder" src="{% static '/images/hills.jpg' %} " class="banner" />
            {% include 'nav.html' %}
            <div class="bannerItem">
                <a href="{% static '/images/hills.jpg' %}" onmouseover="showPic(this); return false;" onclick="return false;" >·</a></li>
                <a href="{% static '/images/stone.jpg' %}" onmouseover="showPic(this); return false;" onclick="return false;" >·</a></li>
                <a href="{% static '/images/sea.jpg' %}"   onmouseover="showPic(this); return false;" onclick="return false;" >·</a></li>
            </div>            
        </div>
        <div id="content">
        </div>
        <script type="text/javascript"  src="{% static '/scripts/banner.js' %}"></script>
        {% endblock %}
    </body>
</html>
```

这个文件的要点：

1. 首先要把上面的三个变量都填入。
2. 它既要引用静态文件，又要使用已有模板，故开头两句既要extend，又要load static。且在中间引用了完全不需要变量的nav文件，所以又使用了include。
3. content部分的内容暂时忽略。
4. 属于它自己独有的是banner轮播图，这个用了JavaScript做，没有用python。

## 3. 模板页面的前台展现

现在有了index.html，全站算是有了第一个页面，可以测试页面效果了。

### 3.1 设置基本的view和url

根目录下的view.py，需要设置好index函数：

```
# view.py

from django.shortcuts import render

def index(request):
    context = {
        
    }
    return render(request, 'index.html', context)
```

根目录下的urls.py，需要设置好路径：

```
# urls.py

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), 		   
    path('index/', view.index)
] 

# 或者这样：
urlpatterns = [
    path('admin/', admin.site.urls), 		   
    url(r'^$', view.index, name='index')
] 
```

现在应该有朴素的内容了。

为什么是朴素的内容呢？因为静态文件还没有引入，既没有图片，也没有css样式。

### 3.2 静态文件的使用

静态文件包括图片、css文件、js文件等。

#### 3.2.1 settings文件路径设置

在settings里设置静态文件路径：

确认`django.contrib.staticfiles` 在`INSTALLED_APPS`中。

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
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static') ]

```

#### 3.2.2 建立新目录

在static下分别建立三个文件夹：images，scripts，styles，分别用作图片、脚本、样式的放置位置。

#### 3.2.3 html文件中的引用

上面的代码有涉及。

先在涉及到使用静态文件的html文件开头加上：

```
{% load static %}
```

告知我们要使用static下面的文件了。

css文件的引用：

在head部分：

```
<link rel="stylesheet" type="text/css" href="{% static 'styles/main.css' %}">
```

图片文件的引用：

在涉及到图片引用处：

```
<img src="{% static '/images/logo.png' %}" />
```

js文件的引用：

js文件一般在`</body>`之前：

```
<script type="text/javascript"  src="{% static '/scripts/banner.js' %}"></script>
```

和css的差不多。

## 4. icon文件

看到其他网站都能把自己的logo放在标签页上方，觉得很洋气啊。所以就找了找这方面的做法，还真找到了。

[Django添加favicon.ico图标_- Fsd-CSDN博客](https://blog.csdn.net/Px01Ih8/article/details/82322022)

首先先制作一个ico文件，使用PS或者某些在线生成ico的网站即可。按照作者指示，在下面的网站生成：

http://www.bitbug.net/

下载后将此文件命名为“favicon.ico”后放在static/images/下。

作者介绍了好几种方法。我用下面这个办法成功了！

在url.py中添加：

```
from Django.views.generic.base import RedirectView
urlpatterns=[
    ...
    # favicon.cio
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/images/favicon.ico')),     
]
```

把请求”/favicon.ico”，指向static/images/favicon.ico 这个文件，重新部署一下项目就可以看到效果。

## 5. 地图嵌入页面

静态文件解决好了之后，做个静态页面就不成啥问题了。于是开始做aboutme页面。写写文字，插插图片，调整调整css。突然作了一下，想到联系我们一般都会展示公司地图。于是入坑了地图嵌入。

### 5.1 获取地图代码

很顺利地找到了百度地图写的引用代码。

[创建地图-百度地图生成器](http://api.map.baidu.com/lbsapi/creatmap/)

这个页面默认的是gb-2312，在我的网站里显示为乱码，因此改成了万能的utf-8。

### 5.2 嵌入页面

原计划是把这一堆html、css、js分别拆开，放到现有页面中去。但是试了好几天，哪怕独立显示没有任何问题，一进django的页面，马上就不显示了。这么简单的问题，搜半天也没见到一样问题的。

突然见到了使用iframe的。于是改方案。

### 5.3 iframe嵌入

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

到这里为止，不涉及后台的静态页面网站就做好了。

下面开始“作大死”，玩后台~~~

这一玩，就玩了20多天。。。

## 6. 做一个带后台管理的新闻模块

[一杯茶的时间，上手 Django 框架开发 - 掘金](https://juejin.im/post/5dff47ec6fb9a0164c7bb171)

### 6.1 支架：基本流程

#### 6.1.1 创建app（application）

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

#### 6.1.2 页面和前台的联系

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



#### 6.1.3 创建数据库

##### 6.1.3.1 第一次创建字段

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

##### 6.1.3.2  增加新字段

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

#### 6.1.4 创建后台

##### 6.1.4.1 创建后台超级管理员

其实不能叫创建后台，后台早就有了，admin页面一直在那里。

```
urlpatterns = [
    path('admin/', admin.site.urls),]
```

现在只是创建管理员而已：

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

##### 6.1.4.2 配置后台管理接口：

在 news/admin.py 中填入代码如下：

```
from django.contrib import admin

from .models import Post

admin.site.register(Post)
```

##### 6.1.4.3 后台显示中文

有个小小的要求，现在打开后台是英文的，希望是中文的，怎么办？

settings中的语言选项修改：

```
LANGUAGE_CODE = 'zh-hans'
```

打开后台发现显示中文了。

#### 6.1.5 增加了数据库后页面和前台的联系

##### 6.1.5.1 后台增加文章

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

前台可见！！！！！

*★,°*:.☆(￣▽￣)/$:*.°★*  

☀☀☀

🌹🌹🌹🌹

☘☘☘

🌙🌙🌙

感觉尾巴要翘上天了~~~~

这里的`Post.objects.all()`值得注意一下。以前用bottle时，sqlite是要自己写SQL语句嵌入程序的，现在为什么没有写就成功了呢？就是这句话起的作用。

一杯茶作者说：

> 强大的 ORM（Object Relation Mapping，对象关系映射）模块，使得用 Python 操作数据库非常轻松，免去了使用 SQL 的麻烦。
>
> 简单来说，ORM 能够将面向对象的代码转换成相应的 SQL 语句，从而对数据库进行操作。SQL 是用于访问和处理数据库的标准的计算机语言，但是直接写在代码里面显然难以维护，而且对使用者的要求也非常高，写的糟糕的 SQL 代码查询效率非常低下。因此，使用设计良好的 ORM 不仅让代码可读性更好，也能帮助开发者进行查询优化，节省不少力气。
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



##### 6.1.5.2 附：ORM教程

[Django ORM常用操作介绍（新手必看）-《Django 2.0入门文档手册》 - Python学习网](https://www.py.cn/manual/django-orm-operating.html)

### 6.2 前台页面展示

#### 6.2.1 文章排序

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

#### 6.2.2 文章分页

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

配套url：

```
path('', views.index, name='index'),
```



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



道理上说，也可以把最新新闻条目放到首页上去了。明天可以考虑试试（已成功）。



[Django Pagination 完善分页 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1099806)

ListView从哪里来？一开头就懵圈了。上一篇并没有提到，事实上上一篇根本没有用到类。

还是这位大兄弟，[基于类的通用视图：ListView 和 DetailView_Django博客教程_追梦人物的博客](https://www.zmrenwu.com/courses/django-blog-tutorial/materials/19/)，在这里找到了。

> 要写一个类视图，首先需要继承 Django 提供的某个类视图。至于继承哪个类视图，需要根据你的视图功能而定。比如这里 `IndexView` 的功能是从数据库中获取文章（Post）列表，`ListView` 就是从数据库中获取某个模型列表数据的，所以 `IndexView` 继承 `ListView`。

url.py也要改，不用views.index了，改用下面这个：

```
    # path('', views.index, name='index'),
    path('', views.Indexview.as_view(), name='index'),
```

原因是：

>  `IndexView` 是一个类，不能直接替代 `index` 函数。好在将类视图转换成函数视图非常简单，只需调用类视图的 `as_view()` 方法即可

好了，有了父类，可以继续下文了。

上一篇文章不是开头那篇，是这篇：

[Django Pagination 简单分页_Django博客教程_追梦人物的博客](https://www.zmrenwu.com/courses/django-blog-tutorial/materials/20/)

views.py中，Indexview的类要这么写：

```
class Indexview(ListView):
    """docstring for Indexview"""
    model = Post
    template_name = 'news/index.html'
    context_object_name = 'news_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        # 首先获得父类生成的传递给模板的字典
        context = super().get_context_data(**kwargs)
        # 父类生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量，
        # paginator 是 Paginator 的一个实例，
        # page_obj 是 Page 的一个实例，
        # is_paginated 是一个布尔变量，用于指示是否已分页。
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        # 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        # 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
        context.update(pagination_data)
        # 将更新后的 context 返回，以便 ListView 使用这个字典中的模板变量去渲染模板。
        # 注意此时 context 字典中已有了显示分页导航条所需的数据。
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return{}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }
        return data
```

index.html文件作如下改动，注意只改导航条部分，不改正文内容：

```
<div class="pagination">
                <!--
                {% if news_list.has_previous %}
                    <a href="?page={{news_list.previous_page_number}}">上一页</a>
                {% endif %}
                <span class="pagination">
                    第 {{ news_list.number }} 页 / 共 {{ news_list.paginator.num_pages }} 页
                  </span>
                {% if news_list.has_next %}
                    <a href="?page={{news_list.next_page_number}}">下一页</a>
                {% endif %}  
                -->
                {% if is_paginated %}
                    {% if first %}
                        <a href="?page=1">1</a>
                    {% endif %}
                    {% if left %}
                        {% if left_has_more %}
                            <span>...</span>
                        {% endif %}
                        {% for i in left %}
                            <a href="?page={{ i }}">{{ i }}</a>
                        {% endfor %}
                    {% endif %}
                    <a href="?page={{ page_obj.number }}" style="color: red">{{ page_obj.number }}</a>
                    {% if right %}
                        {% for i in right %}
                            <a href="?page={{ i }}">{{ i }}</a>
                        {% endfor %}
                        {% if right_has_more %}
                            <span>...</span>
                        {% endif %}
                    {% endif %}
                    {% if last %}
                        <a href="?page={{ paginator.num_pages }}">{{ paginator.num_pages }}</a>
                    {% endif %}
                {% endif %}              
            </div>
```

这三个文件改下来，就可以顺利实现新页码导航效果了。

#### 6.2.3 首条不同

在网站首页引用新闻模块，打算实现的效果是：第一条新闻显示图片，其他新闻只显示标题。

前提：引用新闻模块的前若干选项。

这个其实很简单，前几天想多了，把分页第一页放进来了。实际上只要数组取前若干个就好了。

```
news_list = Post.objects.all()[:8]
```

到了前台html，果然有这样专门用于首页不同的：`{% if forloop.first %}`确实是用来判断是不是第一条的，如果是，下面就写它的显示样式。否则，就写另一种显示样式。

```
                        {% for elem in news_list %}
                            {% if forloop.first %}
                                <div class="indexCont3">
                                    <a href="{% url 'news:article_detail' elem.id %} ">
                                        <img src="{{ MEDIA_URL }}{{ elem.image }}">
                                        <h2>{{ elem.title }}</h2> 
                                    </a>
                                </div>
                            {% else %}
                                <div class="indexCont2">
                                    <a href="{% url 'news:article_detail' elem.id %} ">
                                        {{ elem.title }} <span> {{ elem.date }} </span>
                                    </a>
                                </div>
                            {% endif %}
                        {% endfor %}
```



#### 6.2.4 文章详情页

[Django搭建个人博客：编写文章详情页面 - Django搭建个人博客 - SegmentFault 思否](https://segmentfault.com/a/1190000016459742)

第一步，在news下的views中增加详情函数：  

```
def article_detail(request, id):
    article = Post.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'news/detail.html', context)

```

`Post.objects.get(id=id)`这句是按id选取文章。

第二步，在urls.py中增加路径：

```
path('/article-detail/<int:id>/', views.article_detail, name='article_detail')
```

这里犯了一个低级错误，没注意中英文状态，冒号写成了中文。大妈说：  

> 永远不用中文标点符号！

第三步，做一个真正的details.html：

```
        <div id="content">
            <h1> {{ article.title }}</h1>
            <p>  {{ article.content }} </p>
        </div> 
```

现在按照urls.py中的路径可以访问详情页了。

第四步，链接到详情页：

在列表页增加`<a></a>`，href的内容一直是我发愁的。按照这个页面[URL dispatcher | Django documentation | Django](https://docs.djangoproject.com/en/3.0/topics/http/urls/)的说法，将href写成这样：

```
<a href="{% url 'news:article_detail' article.id %}">
                                    <p class="second">{{ elem.date }}</p>
                                    <div class="primary">
                                        <p class="newsTitle" >{{ elem.title }}</p>
                                        <p class="newsZhengwen" >{{ elem.abstract }}</p>
                                    </div> 
                                    <img src="{{ MEDIA_URL }}{{ elem.image }}" class="newsimage">
                                </a>
```

明明这个人说news是app的名字的，但是运行起来给的提示是：

```
'news' is not a registered namespace
```

[python - Django - is not a registered namespace - Stack Overflow](https://stackoverflow.com/questions/41883254/django-is-not-a-registered-namespace)这个人似乎遇到的问题和我一样，说是urls

里没有这个name的命名。试试根目录下的urls.py：

```
path('news', include(('news.urls','news'), namespace='news'))
```

现在的错误提示是：

```
Reverse for 'article_detail' with arguments '('',)' not found. 1 pattern(s) tried: ['news/article\\-detail/(?P<id>[0-9]+)/$']
```

[python - Reverse for 'edit_post' with arguments '('',)' not found. 1 pattern(s) tried: ['edit_post/(?P<post_id>\\d+)/$'] - Stack Overflow](https://stackoverflow.com/questions/50810841/reverse-for-edit-post-with-arguments-not-found-1-patterns-tried)，这个人说是因为index里用了‘article'变量，但是views.py中的context却没有这个变量。想想有道理啊。

```
def index(request):
    news_list = Post.objects.all()
    paginator = Paginator(news_list, 5)
    page = request.GET.get('page')
    article = Post.objects.get(id=id)  #新增加的
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    context = {
        'news_list': news_list,
        'article': article #新增加的
    }
    return render(request, 'news/index.html', context)
```

但是这个id必须有个出处，如果是从参数里来，和article_detail函数一样写成`def index(request, id)`，那么输入网址时就必须也要输入id才行。这显然不符合情况。

试着在上面这个函数里加了一个循环：

```
def index(request):
    news_list = Post.objects.all()
    for newsObj in news_list:
        article = Post.objects.get(id=newsObj.id)
    ……
    context = {
        'news_list': news_list,
        'article': article #新增加的
    }
```

现在看到所有文章都指向了最后一篇文章，因为循环到最后，保留下来的就是最后一篇的id了。

弄明白了原因，又各种乱七八糟试，还在文章详情页里添加了一个回主页的链接（实际上顶部菜单已经能做这件事了）：

```
<a href="{% url 'news:index' %}" style="color: #000">新闻列表</a>
```

通过这个改动，明白了引用机制是：news这个app（的views.py）下的index函数所指向的页面，是它要链接到的页面。  

决定放弃上面这步改动，index函数不变。

```
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
        'news_list': news_list,
    }
    return render(request, 'news/index.html', context)
```

回到链接详情这里来：

```
<a href="{% url 'news:article_detail' article.id %} ">
```

现在的问题就是没有取出正确的article来。  

又向上看了几行：

```
{% for elem in news_list %}
                        <li>
                            <div class="newscontent">
                                <hr/>
                                <a href="{% url 'news:article_detail' article.id %} ">
                                    <p class="second">{{ elem.date }}</p>
```

突然灵光一闪，elem不就是这个article吗？`.get(id=id)`不过是一种取法，另一种取法就是对`Post对象.all()`结果进行循环啊。

于是把`article`改成elem。

```
{% for elem in news_list %}
                        <li>
                            <div class="newscontent">
                                <hr/>
                                <a href="{% url 'news:article_detail' elem.id %} ">
                                    <p class="second">{{ elem.date }}</p>
```

万事大吉~！🌹

感谢以上作者，让我彻底理解了其中的传递过程。

#### 6.2.5 上一篇和下一篇

重点是view.py的改写。刚开始想复杂了，觉得要用类。后来发现类还是写不来，注意是对内部太不熟悉。于是就在原来的函数基础上改写了。

参照：[Django针对上一篇和下一篇文章标题的实现逻辑_i168wintop的博客-CSDN博客](https://blog.csdn.net/i168wintop/article/details/100077288)

##### 6.2.5.1 起初写法

view.py的改写：

```
def article_detail(request, id):
    news_list = Post.objects.all()
    curr_article = Post.objects.get(id=id)
    for index, article in enumerate(news_list):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(news_list) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        # 通过id判断当前文章
        if article.id == id:
            curr_article = article
            if previous_index != 0:
                previous_article = news_list[previous_index]
            else:
                previous_article = None
            if next_index != index:
                next_article = news_list[next_index]
            else:
                next_article = None
            break

    context = {
        'article': curr_article,
        'previous_article': previous_article,
        'next_article': next_article,
    }
    return render(request, 'news/detail.html', context)
```

for循环主要的作用是让文章和它的id建立联系。for循环中的文章和当前文章建立了联系后，就能用id去判断上一篇是什么，下一篇是什么了。

原作者没有考虑第一篇和最后一篇的特殊性，只让它显示现有的第一篇和最后一篇。考虑了一下，把第一篇的前一篇和最后一篇的后一篇都改成None。然后在前台用if判断来显示其他内容。这是学的新闻首页那个“暂无新闻”。

##### 6.2.5.2 一个bug

2020.06.22：

这里发现了一个bug。

新闻第二篇，index=1，按理它的`previous_index == 0`，这是真的，因为前一篇就是第一篇。可是按照上面的判断，如果`previous_index != 0`，才显示前一篇。否则就说这是None，已经是第一篇了。这样第二篇的前一篇就显示不了了，被认为也是第一篇。

于是修改：

```
def article_detail(request, id):
    news_list = Post.objects.all()
    curr_article = Post.objects.get(id=id)
    for index, article in enumerate(news_list):
        if index == 0:
            previous_index = 'None'
            next_index = index + 1
        elif index == len(news_list) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        # 通过id判断当前文章
        if article.id == id:
            curr_article = article
            if previous_index == 'None':
                previous_article = None
            else:
                previous_article = news_list[previous_index]
            if next_index != index:
                next_article = news_list[next_index]
            else:
                next_article = None
            break
```

之所以给None加上引号，是因为起初没想换ifelse顺序，None被认为和0是相同的。使用`!==`没成功。于是就改成了字符串。



detail.html文件：

```
            {% if previous_article %}
                <a class="previous" href="{% url 'news:article_detail' previous_article.id %}">上一篇: {{ previous_article.title }} </a>
            {% else %}
                <div class="previous">已经是第一篇了</div>
            {% endif %}
            {% if next_article %}
                <a class="next" href="{% url 'news:article_detail' next_article.id %}">下一篇: {{ next_article.title }} </a>
            {% else %}
                <div class="next">已经是最后一篇了</div>
            {% endif %}
```

##### 6.2.5.3 另一个bug

当文章只有1篇时，下一篇的bug也出现了。发现原来因为此时`index==0`，但`len(list)==1`，所以

```
elif index == len(news_list) - 1:
            previous_index = index - 1
            next_index = index
```

这里，`next_index == 0`了。

修改如下：

```
for index, caseArc in enumerate(case_list):
        if len(case_list) != 1:
            if index == 0:
                previous_index = 'None'
                next_index = index + 1
            elif index == len(case_list) - 1:
                previous_index = index - 1
                next_index = index
            else:
                previous_index = index - 1
                next_index = index + 1
        else:
            previous_index = next_index = 'None'
        # 通过id判断当前文章
        if caseArc.id == id:
            curr_case = caseArc
            if previous_index == 'None':
                previous_caseArc = None
            else:
                previous_caseArc = case_list[previous_index]
            if next_index == 'None':
                next_caseArc = None
            elif next_index == index:
                next_caseArc = None
            else:
                next_caseArc = case_list[next_index]
            break
```

这样在前台产生了一个前后皆空的情况需要专门写：

```
            {% if previous_caseArc != next_caseArc %}
                {% if previous_caseArc %}
                    <a class="previous" href="{% url 'case:case_detail' previous_caseArc.id %}">上一篇: {{ previous_caseArc.title }} </a>
                {% else %}
                    <div class="previous">已经是第一篇了</div>
                {% endif %}
                {% if next_caseArc %}
                    <a class="next" href="{% url 'case:case_detail' next_caseArc.id %}">下一篇: {{ next_caseArc.title }} </a>
                {% else %}
                    <div class="next">已经是最后一篇了</div>
                {% endif %}
            {% else %}
                <br/>
            {% endif %}
```

只要前不等于后，就照常。否则只写一个空行就行了。

#### 6.2.6 新闻增加分类的前台页面

仿照detail.html的做法，逐步实施。

第一步，在news下的views中增加分类函数：

```
def category(request, id):
    cate = Category.objects.get(id=id)
    context = {
        'cate': cate,
    }
    return render(request, 'news/category.html', context)

```

在文章详情函数里增加：

```
        if article.id == id:
            curr_article = article
            cate = article.category
```

这个cate才真正建立文章和分类的联系。

第二步，在urls.py中增加路径：

```
    path('category/<int:id>', views.category, name='category')
```

第三步，做一个真正的category.html：

```
            <p style="text-align: left"> <a href="{% url 'news:index' %}" >新闻资讯</a> >> {{ cate.name }}</p>
            <h1 class="newsTitle" > {{ cate.name }}</h1>
```

第四步，链接到分类页：

在detail.html中，面包屑部分，需要加上这个链接。

```
<p style="text-align: left"> <a href="{% url 'news:index' %}" >新闻资讯</a> >> <a href="{% url 'news:category' cate.id %}"> {{cate.name}}</a> >> {{ article.title }}</p>
```

到目前为止，顺利。只是分类页面比较单薄，只有分类名称，没有下属文章。

第五步，在category.html中增加文章列表。

```

def category(request, id):
    cate = Category.objects.get(id=id)
    cate_news = Post.objects.get(category=cate)
    context = {
        'cate': cate,
        'cate_news': cate_news
    }
    return render(request, 'news/category.html', context)

```

在这里增加了cate_news字段，用了存储一个分类下的文章列表。

在category.html中增加读取文章列表的部分：

```
                 <div class="indexCont1">
                     {% if cate_news %}                
                        <ul>
                            {% for elem in cate_news %}
                                    <li>
                                        <a href="{% url 'news:article_detail' elem.id %} ">
                                            <img src="{{ MEDIA_URL }}{{ elem.image }}">
                                            <h2>{{ elem.title }}</h2> 
                                        </a>
                                    </li>
                            {% endfor %}
                        </ul>
                    {% else %}
                        <p>暂无新闻</p>
                    {% endif %}
                </div>
```

现在出错了，系统好委屈：

```
MultipleObjectsReturned at /newscategory/2
get() returned more than one Post -- it returned 11!

……

    cate_news = Post.objects.get(category=cate) 
```

查了一下，get这个方法，就是只要一个的。结果有11条我当然知道，我都在后台看到了。

[django入门：get() returned more than one topic_foryouslgme的博客-CSDN博客_get() returned more than one blog -- it returned 2](https://blog.csdn.net/foryouslgme/article/details/51375246)

这篇文章说：要用filter.

```
# views.py

def category(request, id):
    cate = Category.objects.get(id=id)
    cate_news = Post.objects.filter(category=cate)
    context = {
        'cate': cate,
        'cate_news': cate_news
    }
    return render(request, 'news/category.html', context)

```

现在成功了。

附：后来改成了这样：

```
def category(request, id):
    cates = Category.objects.all()
    cate_curr = Category.objects.get(id=id)
    cate_news = Post.objects.filter(category=cate_curr)
    context = {
        'cates': cates,
        'cate_curr': cate_curr,
        'cate_news': cate_news
    }
    return render(request, 'news/category.html', context)

```

搭配url：

```
path('category/<int:id>', views.category, name='category')
```





还剩下最后一个问题：新闻首页如何安排两个分类？

感觉这个用js最好，做成选项卡。选项卡1是第一个分类，点击显示此分类下的文章。选项卡2是第二个分类，点击显示此分类下的文章。

如果不点击，就显示全部。

[js实现简单选项卡功能_javascript技巧_脚本之家](https://www.jb51.net/article/146020.htm)

#### 6.2.7  新闻首页安排两个分类

2020.06.30

**最后一种方法的弊端：上一篇下一篇没有了。不知道是不是list的消失造成的。**

分别尝试了几种方法：

1. 纯css写选项卡，重要控件是input，有人用radio的type，有人用text的type。我没有成功。放弃。
2. 用js写选项卡，只要把分类新闻部分写成div，然后控制div 的显示与隐藏。这个方法可行。缺点是我在同一个页面里既写全部，又写分类新闻，导致分类新闻只能跟着全部的页码来走。比如第一页一共5条全部新闻，其中2条是分类一，3条是分类2。操作上就是这样的：打开第一页，点击全部，5条。点击分类一，2条。点击分类2，3条。这在逻辑上太奇怪了。具体实现过程在[js实现tab标签页切换.md](./js实现tab标签页切换.md)中。
3. 用js写选项卡，但使用框架装分类新闻内容。只要把全部新闻、各分类新闻全部做成可以独立访问的iframe，index中，用js对iframe的src进行更改。这个也实现了。具体实现参考了banner图那个做法。js脚本比上一个方法简单很多。但是问题来了，样式难控制不说，iframe的滚动条不好处理不说，点击里面的任何链接，都是在这个框架范围内的。而且地址栏不体现任何细分地址，因为都在框架内。从分类、到详情页，全部去头去尾，乱七八糟。遂弃之。
4. 山穷水尽之余，突然觉得想多了，直接让选项卡标签链接到新页面不就好了吗？button的href是假的，那就onclick啊。果然实现了。

第二种方法的news部分的index.html文件：

```
<!DOCTYPE html>
<html>
    {% extends 'frame.html' %}
    {% load static %}
    {% block title %}News-Zeropoint IT{% endblock %}
    {% block description %}三维电子沙盘新闻资讯。{% endblock %}
    <body>
        {% block content %}
        <div class="daohang">
            {% include 'nav.html' %}
        </div>        
        <div id="content">
            <div class="tabs">
                <button class="cateChoose" > 全部 </button>
                {% for cate in cates %}
                    <button class="cateChoose" > {{cate.name}} </button>
                {% endfor %}
            </div>

            <div class="tabContent">
                <div name="tabContent" class="show">
                    {% if news_list %}
                        <ul>
                            {% for elem in news_list %}
                                <li>
                                    <div class="newscontent">
                                        <hr/>
                                        <a href="{% url 'news:article_detail' elem.id %} ">
                                            <p class="second">{{ elem.date| date:"m-d Y" }}</p>
                                            <div class="primary">
                                                <p class="newsTitle" >{{ elem.title }}</p>
                                                <p class="newsZhengwen" >{{ elem.abstract }}</p>
                                            </div> 
                                            <img src="{{ MEDIA_URL }}{{ elem.image }}" class="newsimage">
                                        </a>
                                    </div>
                                </li>
                            {% endfor %}
                        </ul>
                    {% else %}
                        <p>暂无新闻</p>
                    {% endif %}
                </div>

                {% for cate in cates %}
                <div name="tabContent" class="hidden">
                    {% if news_list %}
                        {% for news_art in news_list %}
                            {% ifequal news_art.category cate %}
                                <li>
                                    <div class="newscontent">
                                        <hr/>
                                        <a href="{% url 'news:article_detail' news_art.id %} ">
                                            <p class="second">{{ news_art.date| date:"m-d Y" }}</p>
                                            <div class="primary">
                                                <p class="newsTitle" >{{ news_art.title }}</p>
                                                <p class="newsZhengwen" >{{ news_art.abstract }}</p>
                                            </div> 
                                            <img src="{{ MEDIA_URL }}{{ news_art.image }}" class="newsimage">
                                        </a>
                                    </div>
                                </li>
                            {% endifequal %}
                        {% endfor %}
                    {% else %}
                        <p>暂无新闻</p>
                    {% endif %}
                </div>
                {% endfor %}
                
                <div class="pagination">
                    <!--
                    {% if news_list.has_previous %}
                        <a href="?page={{news_list.previous_page_number}}">上一页</a>
                    {% endif %}
                    <span class="pagination">
                        第 {{ news_list.number }} 页 / 共 {{ news_list.paginator.num_pages }} 页
                      </span>
                    {% if news_list.has_next %}
                        <a href="?page={{news_list.next_page_number}}">下一页</a>
                    {% endif %}  
                    -->
                    {% if is_paginated %}
                        {% if first %}
                            <a href="?page=1">1</a>
                        {% endif %}
                        {% if left %}
                            {% if left_has_more %}
                                <span>...</span>
                            {% endif %}
                            {% for i in left %}
                                <a href="?page={{ i }}">{{ i }}</a>
                            {% endfor %}
                        {% endif %}
                        <a href="?page={{ page_obj.number }}" style="color: red">{{ page_obj.number }}</a>
                        {% if right %}
                            {% for i in right %}
                                <a href="?page={{ i }}">{{ i }}</a>
                            {% endfor %}
                            {% if right_has_more %}
                                <span>...</span>
                            {% endif %}
                        {% endif %}
                        {% if last %}
                            <a href="?page={{ paginator.num_pages }}">{{ paginator.num_pages }}</a>
                        {% endif %}
                    {% endif %}              
                </div>
                <br>
            </div>

        <script type="text/javascript"  src="{% static '/scripts/catenews.js' %}"></script>
        {% endblock %}
    </body>
</html>
```





最后一种方法的html文件：

```
#news index.html

<div class="tabs">
	<button class="cateChoose1" onclick="window.location.href = '/news'"> 全部 </button>
    {% for cate in cates %}
    	<button class="cateChoose2" onclick="window.location.href = 'category/{{ forloop.counter}} '"> {{cate.name}} </button>
    {% endfor %}
</div>
```

```
# news category.html

<div class="tabs">
    <button class="cateChoose2"  onclick="window.location.href = '/news'" > 全部 </button>
    {% for cate in cates %}
        {% ifequal cate cate_curr %}
        <button class="cateChoose1" onclick="window.location.href = '{{ forloop.counter}} '"> {{cate.name}} </button>
        {% else %}
        <button class="cateChoose2" onclick="window.location.href = '{{ forloop.counter}} '"> {{cate.name}} </button>
        {% endifequal %}
    {% endfor %}
</div>
```

完整的index.html文件：

```
<!DOCTYPE html>
<html>
    {% extends 'frame.html' %}
    {% load static %}
    {% block title %}News-Zeropoint IT{% endblock %}
    {% block description %}三维电子沙盘新闻资讯。{% endblock %}
    <body>
        {% block content %}
        <div class="daohang">
            {% include 'nav.html' %}
        </div>        
        <div id="content">
            <div class="tabs">
                <button class="cateChoose1" onclick="window.location.href = '/news'"> 全部 </button>
                {% for cate in cates %}
                    <button class="cateChoose2" onclick="window.location.href = 'category/{{ forloop.counter}} '"> {{cate.name}} </button>
                {% endfor %}
            </div>

            <div class="tabContent">
                {% if news_list %}
                    <ul>
                        {% for elem in news_list %}
                            <li>
                                <div class="newscontent">
                                    <hr/>
                                    <a href="{% url 'news:article_detail' elem.id %} ">
                                        <p class="second">{{ elem.date| date:"m-d Y" }}</p>
                                        <div class="primary">
                                            <p class="newsTitle" >{{ elem.title }}</p>
                                            <p class="newsZhengwen" >{{ elem.abstract }}</p>
                                        </div> 
                                        <img src="{{ MEDIA_URL }}{{ elem.image }}" class="newsimage">
                                    </a>
                                </div>
                            </li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <p>暂无新闻</p>
                {% endif %}
            </div>
                
            <div class="pagination">
                {% if is_paginated %}
                    {% if first %}
                        <a href="?page=1">1</a>
                    {% endif %}
                    {% if left %}
                        {% if left_has_more %}
                            <span>...</span>
                        {% endif %}
                        {% for i in left %}
                            <a href="?page={{ i }}">{{ i }}</a>
                        {% endfor %}
                    {% endif %}
                    <a href="?page={{ page_obj.number }}" style="color: red">{{ page_obj.number }}</a>
                    {% if right %}
                        {% for i in right %}
                            <a href="?page={{ i }}">{{ i }}</a>
                        {% endfor %}
                        {% if right_has_more %}
                            <span>...</span>
                        {% endif %}
                    {% endif %}
                    {% if last %}
                        <a href="?page={{ paginator.num_pages }}">{{ paginator.num_pages }}</a>
                    {% endif %}
                {% endif %}              
            </div>
            <br>
        </div>
        {% endblock %}
    </body>
</html>
```





后者的ifequal，不过是为了让分类页识别出哪个是此页的分类。

道理非常简单。看着也还行。总之是前面想多了。现在可以安心搞分类的页码了（因为是独立页面，不用考虑index混杂在一起的情况。

#### 6.2.8 分类页面的分页页码

想用和首页一样的分页，就需要用ListView。但是ListView默认是不分类的，所以得找到能让它分类的方法。

[Django 教程 6: 通用列表和详细信息视图 - 学习 Web 开发 | MDN](https://developer.mozilla.org/zh-CN/docs/learn/Server-side/Django/Generic_views)

[内置基于类的通用视图| Django文档| Django的](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/)

这两个教程，说了model还应该是文章，而不是分类。分类只是用来filter的工具。

```
class Categoryview(ListView):
    """docstring for Indexview"""
    model = Post
    template_name = 'news/category.html'
    context_object_name = 'news_list'
    paginate_by = 5
```

需要写一个`get_queryset`方法来进行筛选：

```
from django.shortcuts import render, get_object_or_404

def get_queryset(self):
    self.category = get_object_or_404(Category, id=self.kwargs['id'])
    return Post.objects.filter(category=self.category)
```

`get_object_or_404`是新引进来的，它的作用是找对象，找不到就返回404。差不多这个意思吧。

[Django shortcut functions | Django documentation | Django](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/)

> ## `get_list_or_404()`[¶](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#get-list-or-404)
>
> - `get_list_or_404`(*klass*, **args*, ***kwargs*)[¶](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#django.shortcuts.get_list_or_404)
>
>   Returns the result of [`filter()`](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.filter) on a given model manager cast to a list, raising [`Http404`](https://docs.djangoproject.com/en/3.0/topics/http/views/#django.http.Http404) if the resulting list is empty.
>
> 
>
> ### Required arguments[¶](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#id3)
>
> - `klass`
>
>   A [`Model`](https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model), [`Manager`](https://docs.djangoproject.com/en/3.0/topics/db/managers/#django.db.models.Manager) or [`QuerySet`](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet) instance from which to get the list.
>
> - `**kwargs`
>
>   Lookup parameters, which should be in the format accepted by `get()` and `filter()`.
>
> 
>
> ### Example[¶](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#id4)
>
> The following example gets all published objects from `MyModel`:
>
> ```
> from django.shortcuts import get_list_or_404
> 
> def my_view(request):
>     my_objects = get_list_or_404(MyModel, published=True)
> ```
>
> This example is equivalent to:
>
> ```
> from django.http import Http404
> 
> def my_view(request):
>     my_objects = list(MyModel.objects.filter(published=True))
>     if not my_objects:
>         raise Http404("No MyModel matches the given query.")
> ```

上面的句子里，`id=self.kwargs['id']`折腾很久才明白，这个引号'id'，是来自url里那个`<>`。我一直以为参数就一定要写在方法后面的括号里。但是对照教程上的publisher，终于明白，来自这里：

```
path('category/<int:id>', views.Categoryview.as_view(), name='category'),
```

于是真的取到了当前分类。

在这种写法上，如果像之前那样直接写`id=id`，系统会提示：

```
field 'id' expected a number but got <built-in function id>.
```

到这里为止，主要的就写好了。

昨天的发现，data中可以增加需要的context字典键值。例如：

```
        cates = Category.objects.all()
        cate_curr = Category.objects.get(id=self.kwargs['id'])

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'cates': cates,
            'cate_curr': cate_curr,
        }
        return data

```

因为那个选项卡标签，还是需要分类数组和当前分类的。于是就加在这里。

完整的view：

```
class Categoryview(ListView):
    """docstring for Indexview"""
    model = Post
    template_name = 'news/category.html'
    context_object_name = 'news_list'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['id'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        print(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return{}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        cates = Category.objects.all()
        cate_curr = Category.objects.get(id=self.kwargs['id'])

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'cates': cates,
            'cate_curr': cate_curr,
        }
        return data
```

```
# urls.py

app_name = 'news'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Indexview.as_view(), name='index'),
    path('article-detail/<int:id>', views.article_detail, name='article_detail'),
    # path('category/<int:id>', views.category, name='category')
    path('category/<int:id>', views.Categoryview.as_view(), name='category'), #替代上面一句
]
```

完整的category.html页：

```
<div class="tabs">
    <button class="cateChoose2"  onclick="window.location.href = '/news'" > 全部 </button>
    {% for cate in cates %}
        {% ifequal cate cate_curr %}
        <button class="cateChoose1" onclick="window.location.href = '{{ forloop.counter}} '"> {{cate.name}} </button>
        {% else %}
        <button class="cateChoose2" onclick="window.location.href = '{{ forloop.counter}} '"> {{cate.name}} </button>
        {% endifequal %}
    {% endfor %}
</div>

<div class="tabContent">            
    {% if news_list %}
        <ul>
            {% for elem in news_list %}
                <li>
                    <div class="newscontent">
                        <hr/>
                        <a href="{% url 'news:article_detail' elem.id %} ">
                            <p class="second">{{ elem.date| date:"m-d Y" }}</p>
                            <div class="primary">
                                <p class="newsTitle" >{{ elem.title }}</p>
                                <p class="newsZhengwen" >{{ elem.abstract }}</p>
                            </div> 
                            <img src="{{ MEDIA_URL }}{{ elem.image }}" class="newsimage">
                        </a>
                    </div>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>暂无新闻</p>
    {% endif %}
</div>  

<div class="pagination">
    {% if is_paginated %}
        {% if first %}
            <a href="?page=1">1</a>
        {% endif %}
        {% if left %}
            {% if left_has_more %}
                <span>...</span>
            {% endif %}
            {% for i in left %}
                <a href="?page={{ i }}">{{ i }}</a>
            {% endfor %}
        {% endif %}
        <a href="?page={{ page_obj.number }}" style="color: red">{{ page_obj.number }}</a>
        {% if right %}
            {% for i in right %}
                <a href="?page={{ i }}">{{ i }}</a>
            {% endfor %}
            {% if right_has_more %}
                <span>...</span>
            {% endif %}
        {% endif %}
        {% if last %}
            <a href="?page={{ paginator.num_pages }}">{{ paginator.num_pages }}</a>
        {% endif %}
    {% endif %}              
</div>
<br>
```

#### 6.2.9 news分类页面的奇怪bug

新增加了两个分类。除了上面说的排序方法造成紊乱之外，还有个新的奇怪问题：新增的两个分类下，tab标签部分，只有全部，没有各分类标签。也就是下面这段代码没有工作：

```
# catagory.html


{% for cate in cates %}
    {% ifequal cate cate_curr %}
    	<button class="cateChoose1" onclick="window.location.href = '{{ forloop.counter}} '"> {{cate.name}} </button>
    {% else %}
    	<button class="cateChoose2" onclick="window.location.href = '{{ forloop.counter}} '"> {{cate.name}} </button>
    {% endifequal %}
{% endfor %}
```

然而正文部分是好的。我新增了文章，就出现文章。不新增文章，就写“暂无新闻”。

在昨天之前已有的两个分类下，不存在这个问题。说明数据库新增记录是传递到位的，不管是后台还是前台，都能接受到这两个新的分类记录，甚至之下的文章也接受到了。

苦思冥想，无果。甚至跑去找测试方法，意外看到了test自动化测试的内容：[编写你的第一个 Django 应用，第 5 部分 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/)。

继续左思右想：

- 这个问题没有明确的错误返回代码，不能像往常一样，贴入错误提示，总有人跟你犯一样的错误。

- 这是html页面，不能在终端print，也不能在浏览器console里看结果。怎么测试呢？

- 又回头怀疑数据库传递不到位，虽然view函数是统一的，category.html页面也是统一的。makemigrations和migrate各做了一遍，结果毫无疑问：数据库结构没有任何新的变化，因此不会工作。
- 怀疑css问题，去掉了两个样式里的`::after`部分，也没啥用。想想各页面其实在系统里是一个页面，怎么会和这个css样式有关系呢？

觉得走投无路。决定粗暴地在页面里加变量：

```
<p>{{cate}}</p>
```

无内容。

```
<p>{{cates}}</p>
```

有变化了，旧分类页面这里显示了所有分类内容，而新增分类页面这里是空。

突然想起来当前分类已经被我改成了curr，于是又改成：

```
<p>{{cate_curr}}</p>
```

仍旧如此：旧分类页面显示自身分类，新分类页面啥也没有。

一筹莫展··························

死马且当活马医。后台加记录吧。

快速在新分类中的一个，添加了5篇新文章。5篇是分页数字。这样这个分类一共6篇文章，必须分页。

刷新页面，奇迹出现了！这个分类和旧分类一样了，啥都有。

恍然大悟！

回去看view函数：

```
data = {
    'left': left,
    'right': right,
    'left_has_more': left_has_more,
    'right_has_more': right_has_more,
    'first': first,
    'last': last,
    'cates': cates,
    'cate_curr': cate_curr,
}
return data
```

这是前天自己摸索出来的，在使用了ListView的情况下，如果想增加新的页面变量，就加到data里来。

在get_context中，是这样写的：

```
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        print(pagination_data)
        return context
```

`context.update(pagination_data)`，意思是无论之前怎样，最后都是要把上面那个data更新上去的。却原来data的意思是有分页就返回这些，没有分页就不返回这些。这就咔咔了😭😭😭😭😭

转念一想，是不是在update之前写入的字典键就是本来就有的呢？比如`context['category'] = self.category`

上面那个粗暴打印，改成了这样：

```
<p>{{category}}</p>
```

果然打印出了当前分类。

原来根本不用再写一个cate_curr。本来就有了。

现在修改有方向了。

data中的cates和cate_curr去掉，连带data之外给它俩赋值的都去掉。让凯撒的归凯撒吧。

修改get_context如下：

```
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cates = Category.objects.all() #新增
        context['category'] = self.category
        context['cates'] = cates # 新增
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        print(pagination_data)
        return context
```

以后可知道了，要加上下文，还是得在这个函数里玩。前天自己摸索的是一条错误路径。

#### 6.2.10 模板过滤器

##### 6.2.10.1 日期格式

```
 {{ article.date | date:"Y-m-d"}} 
```

##### 6.2.10.2 取前n个字符

```
{{elem.abstract | slice:":100"}}
```

用slice，千万不能想当然以为是数组[:100]这样的。

### 6.3 后台功能

#### 6.3.1 上传题图

##### 6.3.1.1 数据库中增加字段

图片也是个字段，所以第一步就是model.py中增加image字段：

```
image = models.ImageField(upload_to='', null=True)
```

然后执行makemigrations和migrate。

这时候去后台看，已经有了image字段，可以上传了。但是传到哪里去，还没设置。

##### 6.3.1.2 图片路径设置

在settings.py中设置：

```
MEDIA_URL = '/newsimages/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'images', 'newsimages')
```

它的templates部分也要增加：

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]
```

`.media`这一句就是增加的。

urls.py中要作如下改动：

```
urlpatterns = [
    path('admin/', admin.site.urls), path('news', include('news.urls')),
    url(r'^$', view.index), url(r'^product$', view.product),
    url(r'^solution$', view.solution), url(r'^case$', view.case),
    url(r'^about$', view.about),
    url(r'^map.html$', view.map),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/images/favicon.ico')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

把settings中设置的媒体路径添加进去。不过添加方式和之前的页面不同，是加在列表后面的。

##### 6.3.1.3 前台显示

```
<img src="{{ MEDIA_URL }}{{ elem.image }}">
```

未设置样式，但是刷新前台，已经可以看到图片了。

#### 6.3.2 正文内容改用富文本编辑器

##### 6.3.2.1 基本使用

[Django搭建个人博客：使用django-ckeditor富文本编辑器 - 掘金](https://juejin.im/post/5c9396276fb9a070fa3763ff)

[Django搭建个人博客：使用django-ckeditor富文本编辑器 - 杜赛的个人网站](https://www.dusaiphoto.com/article/detail/60/)

第一步：安装ckeditor

```
pip install django-ckeditor
```

第二步：在settings中设置

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'django.contrib.sitemaps',
    'ckeditor',
]
```



第三步：到models中使用富文本编辑

```
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    abstract = models.TextField(null=True, max_length=200)
    content = RichTextField() #新修改的
    image = models.ImageField(upload_to='', null=True)

```

第四步：makemigrations和migrate

做完打开后台，富文本编辑器已经显示出来了。可以进行编辑。但是编辑完回到前台一看，显示了`<p></p>`这些，还是整段显示的。所以还差一步要做。

第五步：修改前台html显示方式

```
<p class="zhengwen">  {{ article.content | safe}} </p>
```

增加了`| safe`部分。这样前台显示就正常了。

不过产生了一个新问题：由于有了富文本编辑器可以编辑样式，所以原本写在html里的css就失去了作用。

##### 6.3.2.2 正文上传图片

刚才的做法，无法上传图片，只能填写url地址插入图片。

[django-ckeditor后台富文本编辑器 - 杨仕航的博客](http://yshblog.com/blog/193)

这里说了怎么添加插入图片功能。

第一步：添加uploader的app

settings里作这样的改动。

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'django.contrib.sitemaps',
    'ckeditor',
    'ckeditor_uploader',  #新增
]
```

第二步：settings中增加路径

```
MEDIA_URL = '/newsimages/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'images', 'newsimages')
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT  #新增，根据实际需要写等号后面的内容
```

第三步：修改url中的路径配置

在根目录的url.py文件中增加：

```
    path('ckeditor/', include('ckeditor_uploader.urls')),
```

第四步：修改models.py

```
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='', null=True)
    abstract = models.TextField(null=True, max_length=200)
    content = RichTextUploadingField()
```

刚才的RichTextField用现在的RichTextUploadingField代替。

修改后，照例makemigrations和migrate。

重新打开后台，就发现图片里有了上传按钮。

##### 6.3.2.3 对toolbar的配置

在settings中添加类似这样的一段，可以对toolbar进行配置：

```
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width': '1000px',
        'height': '500px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'full',
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize']
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet']),
    }
}

```

其中，` 'toolbar': 'full',`一句，有几种类型。full是最全的一类，Custom则遵从后面的'toolbar_Custom'配置，`Basic`则是最简的。

##### 6.3.2.4 富文本编辑器和全局css冲突问题

自从使用了富文本编辑器后，新闻详情页的正文就变成了默认格式，在detail.html中写的css样式失效了。研究了几天后，有两个解决方案：

1. 每次新增文章，都打开源代码格式，在头尾包一个`<div class="zhengwen"></div>`。
2. 到detail.html里仔细观察，发现我现在写的是`<p class="zhengwen"></div>`。想想不对啊，我现在都富文本编辑了。每篇正文都好多段落呢。岂能用一个段落来概括？于是改成了`<div class="zhengwen"></div>`。再打开新闻详情页，发现一劳永逸了。

怪不得这个问题搜不到答案，想来是太简单了，所以没有人犯这个错误。😭

#### 6.3.3 新闻增加分类的后台设置

2020.06.24

一直想要个能分类的新闻模块，例如“行业新闻”和“公司新闻”。想了一上午，觉得应该就是增加数据库字段的事情。不过正确的分类应该是下拉框选择，而不是输入。结果找了半天，并不能找到什么叫下拉框的输入控件，能选择的是数据类型，字符串、数值、布尔等。觉得肯定是想错了。于是找“新闻分类”的文章，终于在这两篇文章的拼凑下，搞懂了：分类是独立的类（数据表），它应该与文章数据表建立外键联系。之前的思路全错了。

两篇很有帮助的文章：

[Django前后端分离开发-新闻管理系统(二) - 简书](https://www.jianshu.com/p/562de40917ac)

[Django 开发内容管理系统 - Django 教程 - 自强学堂](https://code.ziqiangxuetang.com/django/django-cms-develop.html)

在它们的启发下，居然真的做成了后台部分。

一共只需要改两个地方，一个是models，一个是admin。前者是数据库结构，后者是后台操作。

```
#models.py

from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# 增加分类的类
class Category(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类' #后台显示的复数，也就是分类和分类们。如果不写，会显示“分类s”，有点滑稽。所以大家都写上。
        ordering = ['name']


class Post(models.Model):
    title = models.CharField(max_length=200)
    #增加分类字段，与分类class产生关联。
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 
    date = models.DateField()
    image = models.ImageField(upload_to='', null=True)
    abstract = models.TextField(null=True, max_length=200)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

```

做完这个改动，makemigrations和migrate一下就好了。

```
# admin.py

from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    list_per_page = 10


class CateAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count')

    def article_count(self, obj):
        return Post.objects.filter(category=obj).count()


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CateAdmin)

```



原先models中只有一个Post类，所以只import了Post。现在全引入方便一些。

增加的这两个类，是在后台显示时方便看一些。

至此，打开后台，就能添加类别，并在文章中设置类别了。

[ManyToOneRel和ForeignKey的区别？ - 问答 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/ask/38817)

这篇提到了一对多和多对多等。对于类别来说，就是一个类别下可以有多篇文章，而一篇文章只能属于一个分类，所以选择了ManyToOne。一开始写的就是这个，但是参数没搞懂，就按前面文章里一样，写了外键。

现在轮到前台页面了。

2020.07.01

发现了此处一个bug：分类的排序标准写了name，导致增加新的分类时tab错乱，于是回去改成id。tab就好了。

```
class Category(models.Model):
    """docstring for ClassName"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['id']
```

新增的分类，在按name排序时，排在原分类之前。但是点击时又跳动。改了后，就按id 的1234来了。