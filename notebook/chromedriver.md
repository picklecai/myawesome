# 在selenium中使用Chrome浏览器  

顺利地安装完selenium并成功导入后，想用我习惯的Chrome却不行了。

默认调用语句：  

`browser = webdriver.Chrome()`

错误提示是：  


```
FileNotFoundError Traceback (most recent call last) ~/anaconda/envs/python35/lib/python3.7/site-packages/selenium/webdriver/common/service.py in start(self)
……
……

WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

```

于是按照提示，去Google上下载了这个chromedriver。  

有人说最快的方法就是把这个文件放到当前目录下，我以为是我的程序所在的目录，失败…… 
又有人说要添加到环境变量中，或者放到当前python的安装目录中。考虑到我现在用的其实是anaconda下虚拟的一个python3目录，os.path乱折腾了一通后，突然发现错误提示中有路径:  
`~/anaconda/envs/python35/lib/python3.7/site-packages/selenium/webdriver/common/service.py `  

于是到这里来看，发现有专门的Chrome文件夹，和这个common是并列的，放进去，失败……  

又折腾了一通，有人说，放任意位置都行，只要把path作为参数传进来。于是调用语句换成了这样晒儿的：  

```
path = '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/selenium/webdriver/chrome/'
browser = webdriver.Chrome(path)
```
现在换错误提示了：  

```
---------------------------------------------------------------------------
PermissionError                           Traceback (most recent call last)
~/anaconda/envs/python35/lib/python3.7/site-packages/selenium/webdriver/common/service.py in start(self)
……
……
WebDriverException: Message: '' executable may have wrong permissions. Please see https://sites.google.com/a/chromium.org/chromedriver/home

```
 Message都变成''了。凌乱。。。。
 
 有人说在Windows下文件目录要写文件名称，于是调用代码改成了这样：  
 ```
path = '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver.exe'
browser = webdriver.Chrome(path)
```
没想到错误提示又回去了，仍然说找不到文件。也没有人说Mac下怎样了。 
……
……
……
突发灵感，去掉了`.exe	`，变成了这样：  

```
path = '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver'
browser = webdriver.Chrome(path)
```

花了比之前若干次稍微长一点的时间，突然一个新的Chrome窗口跳出来了，并友情提示：  
> Chrome正收到自动测试软件的控制。  

URL窗口写着data。  

这就成功了啊！！！
值得写个教程！！！！！

随便扔个地方的方案总算实现了。先用起来再说。

## 重新来过

由于中间重装了ipython，所以以前的chromedriver路径不对了，又重新安装。

这次系统提示的路径是：  
`~/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py 
`

于是到这个位置放了解压出来的chromedriver：  

`/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver`  

本来以为按照以前的过程，现在万无一失了。结果提示是：  

```
SessionNotCreatedException: Message: session not created: Chrome version must be between 70 and 73
  (Driver info: chromedriver=73.0.3683.68 (47787ec04b6e38e22703e856e101e840b65afe72),platform=Mac OS X 10.14.6 x86_64)

```

检查了一下我本机的chrome版本：`版本 78.0.3904.70（正式版本） （64 位）`

在这里[mac 搭建selenium与ChromeDriver环境 - 简书](https://www.jianshu.com/p/39716ea15d99)发现一个下载地址：[Downloads - ChromeDriver - WebDriver for Chrome](http://chromedriver.chromium.org/downloads)

对应78版本再下载一个，发布日期是2019-10-21。

成功。  

以前的版本赶紧扔掉。




