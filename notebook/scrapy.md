# Scrapy学习笔记

## 1. 安装

```
pip install scrapy
```

安装后测一下版本号：  

```
>>> import scrapy
>>> scrapy.version_info
(1, 8, 0)
```

命令行中直接输入`scrapy`，输出为：  

```
Scrapy 1.8.0 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command
```

以上两个操作说明scrapy安装成功。


## 2. 操作——开始项目  

《精通Scrapy网络爬虫》
作者: 刘硕  
出版社: 清华大学出版社  
出版年: 2017-10-1  
定价: 59元  


与Django类似，也是先要建立项目再进行后续。  
在命令行中输入：  

```
scrapy startproject + 项目名 + 项目路径
```

编写好spder的文件后，按照教程运行`scrapy crawl books -o books.csv`居然说没有crawl这个命令。  

从[Python Scrapy 命令行工具 - 简书](https://www.jianshu.com/p/ee56e7b01b3a)发现，scrapy的命令分全局命令和项目命令。

终端中输入：

```
scrapy genspdier -l
```

结果并没有什么异样：  

```
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed
```
其中有crawl啊？？

从[Scrapy：运行爬虫程序的方式 - 智人N - 博客园](https://www.cnblogs.com/luo630/p/9262486.html)发现，所谓项目命令，是要在项目下运行。仔细看看终端路径，才发现，不知道什么时候回到了本机根目录去而未发现。

赶紧回项目，运行，刷刷刷，很厉害的样子。运行完了打开csv文件，果然1000条记录。

## 3. spider  

**所谓框架，就是做填空题。**

> 实现一个Spider只需要完成下面4个步骤：  
> 步骤1: 继承scrapy.Spider。  
> 步骤2: 为Spider取名。
> 步骤3: 设定起始爬取点。  
> 步骤4:实现页面解析函数。  

## 4. selector提取数据

### 4.1 Selector对象

#### 4.1.1 创建对象

```
from scrapy.selector import Selector
selector = Selector(text=text)

from scrapy.http import HtmlResponse
response = HtmlResponse(url=url, body=body, encoding='utf8')
selector = Selector(response=response)
```

#### 4.1.2 选中数据

```
selector.xpath('')
```

#### 4.1.3 提取数据

```
selector.xpath('').extract()
selector.xpath('').re('')
```

### 4.2 Response内置Selector

```
from scrapy.http import HtmlResponse
response = HtmlResponse(url=url, body=body, encoding='utf8')
response.selector
respose.xpath('').extract()
response.css('').extract()
```

### 4.3 Xpath

> html属于xml

xml文档的节点：  

- 根节点
- 元素节点：eg. body, html, div, p, a 等
- 属性节点：eg. href
- 文本节点

**居然不是从0开始计数的，而是从1开始计数的。**

html内容为：  

```
body = '''
<html>
    <head>
        <base href='http://example.com/' />
        <title>Example WebSite</title>
    </head>
    <body>
        <div id='images'>
            <a href='image1.html'>Name: Image 1<br/><img src='image1.jpg' /></a>
            <a href='image2.html'>Name: Image 2<br/><img src='image2.jpg' /></a>
            <a href='image3.html'>Name: Image 3<br/><img src='image3.jpg' /></a>
            <a href='image4.html'>Name: Image 4<br/><img src='image4.jpg' /></a>
            <a href='image5.html'>Name: Image 5<br/><img src='image5.jpg' /></a>
        </div>
    </body>
</html>
'''
```

```
response.xpath('//a[1]/@*') 
```

输出为：  

```
[<Selector xpath='//a[1]/@*' data='image1.html'>]

```


