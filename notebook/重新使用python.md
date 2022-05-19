两年过去了，突然发现直接在终端输入python不管用了，这就导致Django网站支棱不起来了。

一个一个来。



## 0. 环境变量

在powershell里输入python，就会跳出windows应用商店。查了，说是环境变量中，winapp顺序在先。

于是按照这个途径，`我的电脑→属性→高级系统设置→环境变量`，进入环境变量，点击path。

果然winapp在先不假。但是，把它放到后面，或者干脆删了。都没起作用，输入python或者python3就是会跳出windows应用商店。

然后发现path中只有anaconda，没有标准python。难道是没有安装？

试了python3或者pip3，都说没有这个命令。

## 1. 升级pip

在powershell中检查pip版本：

`pip show pip`

可以工作。

然后试图升级：

`pip install --upgrade pip`

```
ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 拒绝访问。: 'c:\\programdata\\anaconda3\\lib\\site-packages\\pip\\_internal\\build_env.py'
Consider using the `--user` option or check the permissions.

```

不能卸载旧版本。

这时用了另一句：

`python -m pip install --upgrade pip`

照旧。

别人说是windows的权限问题。需要换到system32下。

`cd c:\windows\system32`

照旧。

又有一个人说在命令行后面加上`--user`

`python -m pip install --upgrade pip --user`

成功升级到pip22.1了。

## 2. 查看python路径

按照原先的记录查看python的路径。因为powershell里直接输入python是不管用的，但是输入ipython可以。于是从ipython进入python运行界面：

```
import sys

print(sys.path)
```

输出为：

```
[
'C:\\ProgramData\\Anaconda3\\Scripts', 
'C:\\ProgramData\\Anaconda3\\python37.zip', 
'C:\\ProgramData\\Anaconda3\\DLLs', 
'C:\\ProgramData\\Anaconda3\\lib', 
'C:\\ProgramData\\Anaconda3', '', 'C:\\Users\\asus\\AppData\\Roaming\\Python\\Python37\\site-packages', 
'C:\\ProgramData\\Anaconda3\\lib\\site-packages', 
'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32', 
'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib', 
'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin', 
'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\IPython\\extensions', 
'C:\\Users\\asus\\.ipython'
]
```

这个路径里有直接的python37。

## 3. 突然能进python了

又试图输入python，突然发现能打开。

版本是20年时更新的：`Python 3.7.6 (default, Jan  8 2020, 20:23:39)`

看了一下，路径是上上步骤留下来的`c:\windows\system32`。

换成c盘根目录，也是可以的。但是python3并没有。

## 4. 更新python版本

按照以前写的`conda update python`更新python。但是又提示没有管理员权限。这回在后面加一个`--uers`没有用了。搜了后发现，windows下的anaconda，是可以直接在开始菜单里看到的，找到后，anaconda navigator直接右击选择“以管理员身份运行”，它就会自己另外开一个命令行窗口，在其中输入更新语句，就可以了。不过更新内容是其他，如conda等，不是python本身，它还是那个20年的版本。

## 5. 运行Django网站

应该是从python命令能用开始，那个Django网站就能打开了。现在进入网站目录，运行`python manage.py runserver`，果然有了本地地址。



一个上午没有白费。但并不知道到底哪一步解决了问题。



## 附录：所得新知

1. 环境变量中的winapp，最好位于其他变量之后，甚至删掉也没事。在最前面就是惹事儿。
2. windows环境下，动不动给你来个没有管理员权限，很是麻烦。不同情况下的解决方案还不同。
3. 之前不能运行Django网站，原因不在Django命令，而在python。所以重新看Django笔记没有解决问题。这个问题也好判断，输入python语句后，什么反应也没有，下次就知道是系统没把"python"当成命令，才会没有反应。





