# web 爬虫  

时隔多日，又回到了爬虫部分了。像《精通正则表达式》那样深入浅出的书暂时还是没有找到，先把手头这几本从顺手的开始理吧。《Automatic...》一如既往地深入浅出，一共讲了4个模块。  

## 1. webbrowser

这个模块功能非常简单，就是自动打开网址。所以以后批量打开网址的事情就再也不愁了。  
网址来源可以从参数输入，也可以从剪切板输入。现在比一个月之前更觉得剪切板输入最方便。

```
import webbrowser, pyperclip, re

mdUrls = pyperclip.paste().replace('\t','').split('\n')
urlRegex = re.compile(r'\((http.*)\)')
for mdUrl in mdUrls:
    url = urlRegex.search(mdUrl).group(1)
    webbrowser.open(url)
```
写这个是因为我贴的内容中有tab，如果没有，就不必去掉'\t'了。

## 2. requests

下载并保存到文件的完整过程：  

***
- 调用`requests.get()`下载该文件
- 用`'wb'`调用open()，以写二进制的方式打开一个新文件
- 利用Response对象的`iter_content()`方法做循环
- 在每次迭代中调用`write()`，将内容写入该文件
- 调用`close()`关闭该文件
***

### 2.1 `requests.get(url)`

作者说：忘记我曾经说过urllib2，想下载，就用requests。这就是澳大利亚那个人写的书我抄完第一章就再也抄不下去的原因。

发现导入requests后，只做了一件事，就是使用`requests.get(url)`，以后所有的操作都是基于这个get的结果来做的。  

判断状态时用了`requests.codes.ok`这个属性。

### 2.2 `requests.get(url)`的结果Response对象  

```
import requests
res = requests.get(url)
```
#### 2.2.1 检查下载是否成功  

```
res.raise_for_status()
``` 
或者
```
res.status_code == requests.codes.ok
```
#### 2.2.2 提取页面文本字符串  

这是个属性。

```
res.text
```

#### 2.2.3 

`res.iter_content(100000)`

用法：  

```
import requests

res = requests.get(url0)
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
```

目的：  

用wb模式打开文件，写入内容是 `res.iter_content(100000)`  
作者说，使用iter_content是为了确保requests模块即使在**下载巨大**的文件时也**不会消耗太多**内存。

**The chunk size is the number of bytes it should read into memory. **

[快速上手 — Requests 2.18.1 文档](https://2.python-requests.org//zh_CN/latest/user/quickstart.html)

在罕见的情况下，你可能想获取来自服务器的原始套接字响应，那么你可以访问 r.raw。 如果你确实想这么干，那请你确保在初始请求中设置了 stream=True。具体你可以这么做：
```
r = requests.get('https://api.github.com/events', stream=True)
r.raw
<requests.packages.urllib3.response.HTTPResponse object at 0x101194810>

r.raw.read(10)
'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```
但一般情况下，你应该以下面的模式将文本流保存到文件：
```
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
```
使用 Response.iter_content 将会处理大量你直接使用 Response.raw 不得不处理的。 当流下载时，上面是优先推荐的获取内容方式。 Note that chunk_size can be freely adjusted to a number that may better fit your use cases.

#### 2.2.4 查看编码

也是属性。

```
res.encoding
```

#### 2.2.5 查看headers

也是属性 

```
res.headers
```

### 2.2 其他方法  

[快速上手 — Requests 2.18.1 文档](https://2.python-requests.org//zh_CN/latest/user/quickstart.html)

```
r = requests.get('https://api.github.com/events')
```
现在，我们有一个名为 r 的 Response 对象。我们可以从这个对象中获取所有我们想要的信息。
Requests 简便的 API 意味着所有 HTTP 请求类型都是显而易见的。例如，你可以这样发送一个 HTTP POST 请求：
```
>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
```
漂亮，对吧？那么其他 HTTP 请求类型：PUT，DELETE，HEAD 以及 OPTIONS 又是如何的呢？都是一样的简单：
```
>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')

```

## 3. BeautifulSoup

### 3.1 BeautifulSoup的作用对象  

`bs4.BeautifulSoup()`的作用对象，既可以是上面的`res.text`，也可以是本地打开的open()的file对象。

### 3.1 soup的方法：select 或 select_one

```
htmlSoup.select('title')
htmlSoup.select_one('title').text
```
第一个得到的是列表，表示所有。  

第二个得到的是第一个匹配的，只是其中一个，所以可以用text属性。

输出不同： 

```
Out[53]:
[<title>Joel on Software</title>]


Out[54]:
'Joel on Software'

```
### 3.2 select的参数——css选择器

#### 3.2.1 怎么取

空格表示前面包含后面。例如：`'div span'`，表示父级是div当前级是span。
`[]`表示当前级别自身的属性

```
htmlSoup.select('ul li a[href="#tab-1"]')
```
`>`表示直接父子级，中间没有其他元素

```
htmlSoup.select('form>div>input')
```

对class类，什么时候用'.'，什么时候用[class=""]？  
当class类有空格时，用'.'无法解决问题：  

```
for i in range(10):
    print(htmlSoup.select('div[class="editor-category-posts top-10"] ul>li>a[rel="bookmark"]')[i].text, '\n')
```

如果不加上'top-10'的限定，该页面隐藏了161个相同类别的内容，结果会有171个之多，而不是TOP 10！！

#### 3.2.2 取了之后

`.text`与`.getText()`功能相当，都是取文本内容。

`.attrs`表示当前级别对象的属性构成的字典。

`str()`可将取到的结果整个转为字符。

`.get(属性名)`可取到属性值。  

```
print(htmlSoup.select('div>p>span>a')[0].get('href'))
```

#### 下载漫画的大体步骤

1. 取得两类地址：一类是漫画页面地址，一类是漫画图片地址。前者经过`url-res-soup`后用于亮点：找到漫画元素，找到下一张漫画页面地址。后者经过`url-res`后，利用`res.iter_content`保存漫画
2. 找到入口和出口：入口就是当前有漫画的初始页面，出口就是最后一页（其后再无漫画页），要找到最后一页的特征。
3. 为什么会从下载漫画开始？个人觉得是图片的数据结构相对简单。

保存漫画的代码：  

```
imageFile = open('文件夹' + os.path.basename(comicImageUrl), 'wb')
for chunk in comicImageRes.iter_content(100000):
    imageFile.write(chunk)
```

## 反爬虫

手动可以打开，但是requests请求却404.这里有个类似情况的人：[python爬取网页报错提示状态码404，可是在浏览器里可以打开网页-CSDN论坛](https://bbs.csdn.net/topics/391986299)  

按照他说的加上了user-agent就好了：  

```
headers = {'User-Agent':'Mozilla/8.0 (compatible; MSIE 8.0; Windows 7)'}
res = requests.get(url, headers=headers)
```


