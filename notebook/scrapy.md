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


## 2. 项目建立和运行的步骤  


```
《精通Scrapy网络爬虫》
作者: 刘硕  
出版社: 清华大学出版社  
出版年: 2017-10-1  
定价: 59元
```

### 2.1 建立项目  

与Django类似，也是先要建立项目再进行后续。在命令行中输入：  

```
scrapy startproject + 项目名
```
之所以不加路径名称，是因为这句命令本来就是在待建立项目的位置下运行的。  

### 2.2 快速初始化spider

先进入项目所在文件夹，再genspider：  

```
cd example
scrapy genspider spiderName example.com
```
genspider后的参数，第一个是spider的名称，并不是项目名称，而是spider程序中`name=...`那个名称；第二个是待爬取的网址，会出现在spider程序中。但目前我还搞不清是第一个地址还是allowdomain，猜测是第一个地址。

此后spider的初始程序就有了，建立了`./spiders/spiderName.py`，并在其中建立了一个spiderNameSpider的类。

### 2.3 写spider

补充完整spiderName.py，使用xpath和css等方式从页面中爬数据。

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

### 2.4 封装数据（可选）

如果不希望用字典存储数据结果，可以使用scrapy的Item进行。打开`items.py`文件，进行编辑：

```
from scrapy import Item, Field

class BookItem(Item):
    name = Field()
    price = Field()
    ...
```

该文件编辑好后，只要在spider文件中import就可以正常使用了。

```
from ..items import Item类名称

```

也可以写成：  

```
from 项目名称.items import Item类名称
```

### 2.5 处理数据（可选）

使用scrapy的pipeline进行结果数据的处理，例如转换数据格式、去除重复数据等。

打开`pipelines.py`进行编辑：  

```
class PriceConverterPipeline(object):
    exchange_rate = 8.5309      # 需要用到的处理系数

    def process_item(self, item, spider):
        # 处理过程
        price = float(item['price'][1:]) * self.exchange_rate
        item['price'] = '¥%.2f' % price
        # 返回处理后的item
        return item
```
主要就是写处理函数，然后返回处理后的item。

写好后，打开`settings.py`，将`ITEM_PIPELINES = {`这一段从注释中放出来，字典的键是`项目名称.pipelines.Pipeline名称`，字典的值在0~1000之间，同时启用多个Item Pipeline时，Scrapy根据这些数值决定各Item Pipeline处理数据的先后次序，数值小的在前。

（才发现这里和导出数据有关，而非处理数据）

此外，如果希望csv文件中的字段名之间有指定排序，也可以在`settings.py`中进行设置。添加这句：  

```
FEED_EXPORT_FIELDS = ['upc', 'name', 'price', 'stock', 'review_rating', 'review_num']
```
列表中放置指定字段序列。

### 2.6 项目运行

**解决问题“无crawl”**

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

## 3. selector提取数据

**css和xpath的语法，这本书讲得最详细。**

### 3.1 Selector对象

#### 3.1.1 创建对象

```
from scrapy.selector import Selector
selector = Selector(text=text)

from scrapy.http import HtmlResponse
response = HtmlResponse(url=url, body=body, encoding='utf8')
selector = Selector(response=response)
```
原来**Selector也有response参数**，不只是text参数。不过response的值必须由HtmlResponse来。

#### 3.1.2 选中数据

```
selector.xpath('')
```

#### 3.1.3 提取数据

```
selector.xpath('').extract()
selector.xpath('').re('')
```
无须先extract再re，直接re就可以了。

### 3.2 Response内置Selector

```
from scrapy.http import HtmlResponse
response = HtmlResponse(url=url, body=body, encoding='utf8')
response.selector
respose.xpath('').extract()
response.css('').extract()
```

### 3.3 Xpath

> html属于xml

#### 3.3.1 xml文档的节点：  

- 根节点
- 元素节点：eg. body, html, div, p, a 等
- 属性节点：eg. href
- 文本节点

#### 3.3.2 从1开始计数：  

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

#### 3.3.3 xpath的常用基本语法：  

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

### 3.4 css

css语法比xpath更简单，但功能不如xpath强大。

#### 3.4.1 css选择器的常用基本语法： 

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


## 4. LinkExtactor提取链接


```
from scrapy.linkextractors import LinkExtractor

le = LinkExtractor(restrict_css='....')
links = le.extract_links(response)
if links:
    next_url = links[0].url
    yield scrapy.Request(next_url, callback=self.xx)
```
对于LinkExtractor的结果，需要先用extract_links方法得到列表，然后对列表中的数据项取url，才能算作结果。

如果LinkExtractor参数为空，则提取出当前页面的所有链接。  

参数：  

- 1. allow：接受正则表达式或列表，以筛选符合正则条件的结果url。
- 2. deny：也接受正则表达式或列表，但符合条件的url被结果排除。
- 3. allow_domains：接受域名或域名列表，以筛选符合条件的结果url。
- 4. deny_domains：接受域名或域名列表，但符合条件的url被结果排除。
- 5. restrict_xpaths：接受xpath表达式或列表，以筛选符合条件的结果url。
- 6. restrict_css：接受css表达式或列表，以筛选符合条件的结果url。
- 7. tags：接受标签或标签列表，提取指定标签内的链接，默认为['a', 'area']。
- 8. attrs：接受属性或属性列表，提取指定属性内的链接，默认为['href']。
- 9. process_value：接受一个形如`func(value)`的回调函数，用该函数来对提取到的链接进行处理。一般返回处理后的value，如果想要抛弃处理结果，就返回None。

除了最后一个，其他的可分两类：一类是筛选，一类是排除。排除的方法主要有根据正则表达式和域名两种。而筛选的方式则要多一些，除了正则表达式和域名外，还有xpath、css、tags、attrs几种。

## 5. 使用Exporter导出数据

scrapy中负责导出数据的组建被称为Exporter（导出器），scrapy内部实现了多个Exporter，每个实现一种数据格式的导出：  

- JSON（JsonItemExporter）
- JSON lines（JsonLinesItemExporter）
- CSV（CsvItemExporter）
- XML（XmlItemExporter）
- Pickle（PickleItemExporter）
- Marshal（MarshalItemExporter）

前四种是常用的文本数据格式，后两种是python特有的。一般使用这几种就够了，如果是其他数据格式，可以自己写Exporter。

## 5.1 已有类型的Exporter操作

提供：  

- 导出文件路径
- 导出数据格式（即选用哪个Exporter）

既可以通过命令行参数指定，也可以通过配置文件指定。

### 5.1.1 命令行参数指定

前面使用的运行命令就是一个用命令行参数指定的示例：  

```
scrapy crawl books -o books.csv
```

其中`-o books.csv`指定了导出文件的路径。这里没有指定导出数据格式，是通过文件扩展名判断将会使用csv作为导出数据格式的。所以如果改为`-o books.json`，程序会通过扩展名判定为导出json格式。

使用`-t`参数指定导出数据格式：  

```
scrapy crawl books -t csv -o books1.data
scrapy crawl books -t json -o books2.data
scrapy crawl books -t xml -o books3.data
```

`%(name)s`和`%(time)s`两个可以让文件名中带有spidername和下载时间。

### 5.1.2 配置文件指定

- FEED_URI：导出文件路径
- FEED_FORMAT：导出数据格式
- FEED_EXPORT_ENCODING：导出文件编码，默认情况下：json使用数字编码，其他使用utf8编码。
- FEED_EXPORT_FIELDS：导出数据包含的字段（默认导出所有字段），并指定次序。【这就是上面用过的】
- FEED_EXPORTERS：用户自定义Exporter字典，添加新的导出数据格式时使用。

（我想知道写在哪里，是settings.py吗？貌似是的，因为上面的例子中，FEED_EXPORT_FIELDS就是写在settings中的。而且观察了一下默认文件和文件夹，似乎也没有其他文件可以写。

## 5.2 添加导出数据格式


