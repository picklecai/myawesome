# web 框架

目的只是了解一下，能看懂程序，能翻译成bottle框架。

[web.py 0.3 新手指南 (web.py)](http://webpy.org/tutorial3.zh-cn)

## 1. 运行起来

```
# _*_coding:utf-8_*_

import web

urls = ('/', 'index')


class index:
    def GET(self):
        return 'Hello world.'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
```

第一次知道了url里那个index是个类，globals()意思是全局变量空间。

这是按照上面的教程抄的代码。原以为每句话都理解了应该没问题了，不料产生错误：  

```
Traceback (most recent call last):
  File "main.py", line 17, in <module>
    app = web.application(urls, globals())
  File "/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/web/application.py", line 62, in __init__
    self.init_mapping(mapping)
  File "/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/web/application.py", line 130, in init_mapping
    self.mapping = list(utils.group(mapping, 2))
  File "/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/web/utils.py", line 531, in group
    x = list(take(seq, size))
RuntimeError: generator raised StopIteration
```

照样搜索了最后一句话，居然有个人跟我一模一样的遭遇，人家说因为运行了python3.7。确实如此啊！

[python - "RuntimeError: generator raised StopIteration" every time I try to run app - Stack Overflow](https://stackoverflow.com/questions/51700960/runtimeerror-generator-raised-stopiteration-every-time-i-try-to-run-app)

所以他们说了半天，意思就是不用python3.7？

理解力有点弱，[Python3.7运行web.py测试时出现RuntimeError: generator raised StopIteration异常 - 心有山海静而无边 - CSDN博客](https://blog.csdn.net/qq_38591756/article/details/84971485)这个人就是根据刚才的说法去改文件的。

又改了utils文件。

> Chances are they'll need to change:
> ```
yield next(seq)
```
> to:
> 
> ```
try:
    yield next(seq)
except StopIteration:
    return
```

改完后再运行，成功了。

这里增加了一个**新知**，可以在运行python文件时指定端口号：  

```
注意: 如果你不能或者不想使用默认端口，你可以使用这样的命令来指定端口号:
$ python code.py 1234

```

