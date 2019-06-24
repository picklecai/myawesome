查看路径：命令行启动python，

```
import sys

print(sys.path)
```

在进入python3的情况下运行，输出为：  

```
['', '/Users/caimeijuan/anaconda/envs/python35/lib/python37.zip', '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7', '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/lib-dynload', '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages']
```

> 举例来说，假定你将 Python 路径设置为 ['','/usr/lib/python2.4/site- packages','/home/username/djcode/'] 。如果执行代码 from foo import bar ，Python 将会首先在 当前目录查找 foo.py 模块( Python 路径第一项的空字符串表示当前目录)。如果文件不存 在，Python将查找 /usr/lib/python2.4/site-packages/foo.py 文件。如果文件也不存在，它将尝 试 /home/username/djcode/foo.py 。最后，如果 这个 文件还不存在，它将引发 ImportError 异 常。 



