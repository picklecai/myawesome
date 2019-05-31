# 日志  

[日志 HOWTO — Python 3.7.3 文档](https://docs.python.org/zh-cn/3/howto/logging.html)

照书抄：  

```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
```

期间发现了一个错误，message写错了，少写了一个s。  

不过在ipython，怎么也不工作，只输出0。  

想着那就存个文件吧，存了个logging.py的文件。一运行：  
```
Traceback (most recent call last):
  File "logging.py", line 2, in <module>
    import logging
  File "/Users/caimeijuan/github/myawesome/_src/logging.py", line 3, in <module>
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
AttributeError: module 'logging' has no attribute 'basicConfig'
```
擦擦眼睛仔细看看，没抄错啊。于是搜索，得到这个页面：[python - 'module' object has no attribute 'basicConfig' - Stack Overflow](https://stackoverflow.com/questions/4482587/module-object-has-no-attribute-basicconfig)  

这还是个2011年就犯的错误。多老啊！赶紧把文件名随便改一个，运行了一下，终端果然能出现正确的日志了。


```
 2019-05-30 17:15:00,669 - DEBUG - Start of program
 2019-05-30 17:15:00,669 - DEBUG - Start of factorial(5%)
 2019-05-30 17:15:00,669 - DEBUG - i is 1, total is 1
 2019-05-30 17:15:00,669 - DEBUG - i is 2, total is 2
 2019-05-30 17:15:00,670 - DEBUG - i is 3, total is 6
 2019-05-30 17:15:00,670 - DEBUG - i is 4, total is 24
 2019-05-30 17:15:00,670 - DEBUG - i is 5, total is 120
 2019-05-30 17:15:00,670 - DEBUG - End of factorial(5%)
120
```
这和用print有什么区别呢？

作者说：  

> 只要加入一次`logging.disable(logging.CRITICAL)`调用，就可以紧致日志。

日志文件是追加式的，即‘a'模式，只要文件不删除，每次运行就会往里面加一点。


