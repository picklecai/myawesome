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

编写好spider的文件后，按照教程运行`scrapy crawl books -o books.csv`居然说没有crawl这个命令。  

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

Scrapy框架提出以下问题让用户在Spider子类中回答：  

> 爬虫从哪个或哪些页面开始爬取？  
> 对于一个已下载的页面，提取其中哪些数据？  
> 爬取完当前页面后，接下来爬取哪个或哪些页面？

实现一个Spider只需要完成下面4个步骤：  

> 步骤1: 继承scrapy.Spider。  
> 步骤2: 为Spider取名。
> 步骤3: 设定起始爬取点。  
> 步骤4:实现页面解析函数。  

response连接url的方法`urljoin()`，如果链接中的下一页是相对地址，可以用它来构造下一页：

```
response = HtmlResponse(url=url, body=res.text, encoding='utf8')
response.url
response.urljoin(nextUrl)
```

## 4. selector提取数据

**css和xpath的语法，这本书讲得最详细。**

### 4.1 Selector对象

#### 4.1.1 创建对象

```
from scrapy.selector import Selector
selector = Selector(text=text)

from scrapy.http import HtmlResponse
response = HtmlResponse(url=url, body=body, encoding='utf8')
selector = Selector(response=response)
```
原来**Selector也有response参数**，不只是text参数。不过response的值必须由HtmlResponse来。

#### 4.1.2 选中数据

```
selector.xpath('')
```

#### 4.1.3 提取数据

```
selector.xpath('').extract()
selector.xpath('').re('')
```
无须先extract再re，直接re就可以了。

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

#### 4.3.1 xml文档的节点：  

- 根节点
- 元素节点：eg. body, html, div, p, a 等
- 属性节点：eg. href
- 文本节点

#### 4.3.2 从1开始计数：  

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

#### 4.3.3 xpath的常用基本语法：  

> 1. `/`：描述一个从根开始的绝对路径。
> 2. `E1/E2`：选中E1子节点中的所有E2。
> 3. `//E`：选中文档中的所有E，无论在什么位置。
> 4. `E1//E2`：选中E1后代节点中的所有E2，无论在后代中的生命位置。
> 5. `E/text()`：选中E的文本子节点。
> 6. `E/*`：选中E的所有元素子节点。
> 7. `*/E`：选中孙节点中的所有E。
> 8. `E/@ATTR`：选中E的ATTR属性。
> 9. `//@ATTR`：选中文档中所有ATTR属性。
> 10. `E/@*`：选中E的所有属性
> 11. `.`：选中当前节点，用来描述相对路径。
> 12. `..`：选中当前节点的父节点，用来描述相对路径。
> 13. `node[谓语]`：谓语用来查找某个特定的节点或者包含某个特定值的节点。

`string()`默认只给出第一个结果，想要其他的，得加上序号。  

```
selector.xpath('string(//li)') # 第一个，但是是列表形式。
selector.xpath('string(//li[4])') # 第四个
```

`contains()`函数，第一个参数是@ATTR，第二个参数是该属性的值。

### 4.4 css

css语法比xpath更简单，但功能不如xpath强大。

#### 4.4.1 css选择器的常用基本语法： 

> 1. `E`：选中E元素。 
> 2. `*`：选中所有元素。
> 3. `E:empty`：选中没有子元素的E元素。  


> 4. `E1,E2`：选中E1和E2元素。  
> 5. `E1 E2`：选中E1后代元素中的E2元素。  
> 6. `E1>E2`：选中E1子元素中的E2元素。  
> 7. `E1+E2`：选中E1兄弟元素中的E2元素。  


> 8. `[ATTR]`：选中包含ATTR属性的元素。  
> 9. `[ATTR=VALUE]`：选中包含ATTR属性且值为VALUE的元素。（这里是等于）  
> 10. `[ATTR~=VALUE]`：选中包含ATTR属性且其值包含VALUE的元素。（这里是包含）  


> 11. `E:nth-child(n)`：选中E元素，且该元素必须是其父元素的第n个子元素。
> 12. `E:nth-last-child(n)`：选中E元素，且该元素必须是其父元素的倒数第n个子元素。
> 13. `E:first-child`：选中E元素，该元素必须是其父元素的第一个子元素。
> 14. `E:last-child`：选中E元素，该元素必须是其父元素的倒数第一个子元素。


> 15. `.CLASS`：选中class属性包含CLASS的元素。 （这里是包含）
> 16. `#ID`：选中id属性为ID的元素。 （这里是等于）


> 17. `E::text`：选中E元素的文本节点。
> 18. `E::attr(ATTR)`：选中E元素的ATTR属性值




