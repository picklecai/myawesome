# kivy

2015年12月29日，在river的帮助下，用qpython打的包，已经没法在现在的安卓系统上运行了。所以想重新打个包。搜索了一下，kivy出现的频率比较高。

[利用python开发app实战 | nMask's Blog](https://thief.one/2018/05/08/1/)

推荐kivy。想到我上次安装未遂。

## 1. 安装kivy（上次的安装过程，中途夭折）

[mac系统中kivy打包为apk安装包步骤](http://www.360doc.com/content/16/0331/16/13647213_546844872.shtml)

基本按照这里的指导做的。 

### 1.1 安装Bulldozer

'
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
'

建了个文件夹zhangda，初始化为buildozer项目：

`
mkdir zhangda
cd zhangda
buildozer init
`
生成了配置文件buildozer.spec

抄了他的helloworld程序。 


### 1.2 安装kivy  

[kivy 在mac上安装笔记 - 简书](https://www.jianshu.com/p/27278af8a92e)

step1:

`brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer`

成功

step2:

`pip install Cython==0.26.1 `  

提示说本机已有Cython，但是版本是0.23.4，那就改为升级吧。

`python -m pip install --upgrade Cython`

还是提示本机已有Cython 0.23.4

step3:

`pip install kivy`

没想到这一个成功了，其他的方法倒是没成。
`Successfully built Kivy-Garden
Installing collected packages: Kivy-Garden, kivy
Successfully installed Kivy-Garden-0.1.4 kivy-1.10.1`

### 1.3 安装Java

执行`buildozer -v android debug`，错误提示是：  

`No Java runtime present, requesting install.`  

对话框提示是“您需要安装JDK才能使用‘Java’命令行工具。” 提示了一个网址如下。
从[Download Java for Mac OS X](https://www.java.com/en/download/mac_download.jsp)下载了安装。

安装完毕，重新执行buil这句，照旧。  

页面有一句提示：  

> When your Java installation completes, you may need to reload (Command+R) or quit(Command+Q) your browser in order to enable Java in your browser.

重启并没有用。  

[[Java] Mac安装JDK - 简书](https://www.jianshu.com/p/0036a344509e)  
按照这里的，下载了jdk12,安装成功。
在命令行中输入echo $SHELL ，输出/bin/bash则为bash  

用`open ~/.bash_profile`打开文件改写：export JAVA_HOME=$(/usr/libexec/java_home)

`source .bash_profile`  

最后用`java -version`出现了版本信息：  
`java version "12" 2019-03-19
Java(TM) SE Runtime Environment (build 12+33)
Java HotSpot(TM) 64-Bit Server VM (build 12+33, mixed mode, sharing)`  

再执行`buildozer -v android debug`，错误提示是：

`No buildozer.spec found in the current directory. Abandon.` 

这是目录不对。回到zhangda目录中去。  
安装java的错误已经没有了。终于回到正途上。  

### 1.4 解决。。。  

正途上的问题是什么呢？  

```
# Command failed: /Users/caimeijuan/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager tools platform-tools
# ENVIRONMENT:
#     LANG = 'zh_CN.UTF-8'
#     TERM = 'xterm-256color'
#     Apple_PubSub_Socket_Render = '/private/tmp/com.apple.launchd.nEAsgn7OwM/Render'
#     SHLVL = '1'
#     OLDPWD = '/Users/caimeijuan/buildozer'
#     SSH_AUTH_SOCK = '/private/tmp/com.apple.launchd.2Knxb5wLi2/Listeners'
#     SECURITYSESSIONID = '186a9'
#     TERM_SESSION_ID = 'C7F8B4C8-997E-422D-A429-C61810C90FC5'
#     TERM_PROGRAM_VERSION = '421.1'
#     PWD = '/Users/caimeijuan/buildozer/zhangda'
#     SHELL = '/bin/bash'
#     LOGNAME = 'caimeijuan'
#     USER = 'caimeijuan'
#     XPC_SERVICE_NAME = '0'
#     HOME = '/Users/caimeijuan'
#     PATH = '/Users/caimeijuan/.buildozer/android/platform/apache-ant-1.9.4/bin:/Users/caimeijuan/anaconda/bin:/Users/caimeijuan/anaconda/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
#     XPC_FLAGS = '0x0'
#     JAVA_HOME = ''
#     _ = '/Users/caimeijuan/anaconda/bin/buildozer'
#     TMPDIR = '/var/folders/ll/hf0rtrgx4qb0vffp086qfkx80000gn/T/'
#     TERM_PROGRAM = 'Apple_Terminal'
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2`  

```

未遂

## 2. 第二次安装  

按照这个[利用python开发app实战](https://thief.one/2018/05/08/1/)来：  

### 2.1 安装一些依赖包  

`brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer`  

python3和2下都操作了一遍，结果是这样：  

```
Warning: pkg-config-0.29.1 already installed
Warning: sdl2-2.0.4 already installed
Warning: sdl2_image-2.0.1_1 already installed
Warning: sdl2_ttf-2.0.13 already installed
Warning: sdl2_mixer-2.0.1 already installed
Warning: gstreamer-1.8.0 already installed
Warning: You are using OS X 10.14.
We do not provide support for this pre-release version.
You may encounter build failures or other breakages.
```

这些都安装成功了。但是可能会不支持我当前的系统。  

向后走走看。

### 2.2 安装cython以及kivy  

进入python3（`source activate python35`）

```
pip3 install cython
pip3 install kivy

```
cython直接安装了0.29.7

又回到python2下，正常用pip，问题和上面一样，改用了pip3安装，就也是0.29.7了。

kivy也很顺利：  

```
Successfully built Kivy-Garden
Installing collected packages: docutils, Kivy-Garden, kivy
Successfully installed Kivy-Garden-0.1.4 docutils-0.14 kivy-1.10.1
```
### 2.3 测试  

安装好后，在python3的条件下，命令行端直接进入python，`import kivy`，出现这样的警告：  
```
>>> import kivy
[WARNING] [Config      ] Older configuration version detected (0 instead of 20)
[WARNING] [Config      ] Upgrading configuration in progress.
Purge log fired. Analysing...
Purge finished!
[INFO   ] [Logger      ] Record log in /Users/caimeijuan/.kivy/logs/kivy_19-05-22_0.txt
[INFO   ] [Kivy        ] v1.10.1
[INFO   ] [Python      ] v3.7.2 (default, Dec 29 2018, 00:00:04) 
[Clang 4.0.1 (tags/RELEASE_401/final)]
```
发现这里有个人装8的时候同样的经历：[[Solved] Error Upgrading to Kivy 1.8.0](https://techamad.blogspot.com/2014/07/error-upgrading-to-kivy-180.html)

[kivy.config — Kivy 1.10.1 documentation](https://kivy.org/doc/stable/_modules/kivy/config.html)这样说：   

```
# Upgrade default configuration until we have the current version
    need_save = False
    if version != KIVY_CONFIG_VERSION and 'KIVY_NO_CONFIG' not in environ:
        Logger.warning('Config: Older configuration version detected'
                       ' ({0} instead of {1})'.format(
                           version, KIVY_CONFIG_VERSION))
        Logger.warning('Config: Upgrading configuration in progress.')
        need_save = True

```

可能还是python2下的旧版本在某个地方“作祟”吧。  

或者在python2下，使用pip3再来一遍。

然后python2和python3的环境下进入python， import的结果都是下面这样，warning消失了：  

```
Python 2.7.15 |Anaconda custom (64-bit)| (default, Dec 14 2018, 13:10:39) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import kivy
[INFO   ] [Logger      ] Record log in /Users/caimeijuan/.kivy/logs/kivy_19-05-22_1.txt
[INFO   ] [Kivy        ] v1.10.1
[INFO   ] [Python      ] v2.7.15 |Anaconda custom (64-bit)| (default, Dec 14 2018, 13:10:39) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]
```

### 2.4 安装buildozer工具

`pip3 install buildozer`

在python3的环境下运行这个，很快就装好了。

```
Successfully built buildozer
Installing collected packages: virtualenv, sh, buildozer
Successfully installed buildozer-0.39 sh-1.12.14 virtualenv-16.6.0
```
python2的环境下，也运行的是pip3，

```
Successfully built buildozer
Installing collected packages: ptyprocess, pexpect, virtualenv, sh, buildozer
Successfully installed buildozer-0.39 pexpect-4.7.0 ptyprocess-0.6.0 sh-1.12.14 virtualenv-16.6.0
```

成功，可以用了。


### 2.5 打包apk

有很多依赖，所以记在这里。  

在项目目录下运行：  

```
buildozer init
```
创建一个配置文件buildozer.spec，可以通过修改配置文件更改app的名称等。

改完后下一句：  

```
buildozer android debug deploy run
```
运行了几次都是直接卡在第一个install就不动了：  

```
# Check configuration tokens
# Ensure build layout
# Check configuration tokens
# Preparing build
# Check requirements for android
# Install platform

```
有人[Kivy+Buildozer 折腾踩坑记录 - 知乎](https://zhuanlan.zhihu.com/p/33990951)建议把buildozer.spec文件内的log_level修改为2，这样可以更清楚地观察每步输出。

哇哦，效果明显，一下子就知道卡着的时候是在干啥了。

目前是在做这个：`Cloning into 'python-for-android'...`

[kivy - Is there a way to stop buildozer from cloning python-for-android? - Stack Overflow](https://stackoverflow.com/questions/47383413/is-there-a-way-to-stop-buildozer-from-cloning-python-for-android)建议可以在别的地方做好这个。

> 	1.	Clone python-for-android somewhere manually  	
> 	2.	Install dependencies your cloned version would need (can be done just installing python-for-android with pip)  	
> 	3.	Change your buildozer.spec file adding option p4a.source_dir pointing to cloned directory (for example p4a.source_dir =/home/ken/python-for-android) 

新开了一个终端装python-for-android

```
pip install python-for-android
```

安装的版本是：0.7.0

```
Successfully built python-for-android
Installing collected packages: python-for-android
Successfully installed python-for-android-0.7.0
```

python3环境下运行pip3,同样顺利完成：  

```
Successfully built python-for-android
Installing collected packages: appdirs, colorama, MarkupSafe, jinja2, python-for-android
Successfully installed MarkupSafe-1.1.1 appdirs-1.4.3 colorama-0.4.1 jinja2-2.10.1 python-for-android-0.7.0

```

无助于解决。

[Buildozer Documentation](https://buildmedia.readthedocs.org/media/pdf/buildozer/latest/buildozer.pdf)

> To test your own recipe via Buildozer, you need to:   
> 1. Fork Python for Android, and clone your own version (this will allow easy contribution later): git clone http://github.com/YOURNAME/python-for-android   
> 2. Change your buildozer.spec to reference your version: p4a.source_dir = /path/to/your/python-for-android   
> 3. Copy your recipe into python-for-android/recipes/YOURLIB/recipe.sh   
> 4. Rebuild.

于是在项目文件夹下运行`git clone http://github.com/picklecai/python-for-android `

### 2.6 虚拟机路线  

不知道这里[The Kivy Android Virtual Machine — Kivy 1.10.1 documentation](https://kivy.org/doc/stable/guide/packaging-android-vm.html)有虚拟机如何安装使用的说明。只是下了虚拟机，然后使用vmware打开，结果说需要操作系统，又费了几天劲下载了一个win7系统。但是运行不起来。



