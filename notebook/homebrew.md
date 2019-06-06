# hombbrew


想用homebrew来装一个egrep，发现装不了，顺便发现brew自己需要update，没想到update后，是这样：  
```
Error: /usr/local must be writable!
```
[brew安装错误brew Error: /usr/local must be writable! - 个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000017917621)

> 大家解决方法为执行下面赋予权限预句sudo chown -R $(whoami) /usr/local，执行过后发现控制台报操作不允许，google发现macOS，现在版本不让修改了。。。（apple 搞事情啊）

这兄弟说麻利地，卸掉重装吧。这才发现，之前都没有写过一篇brew笔记。  

## 卸载和重装 

卸载：  

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)" 
```

重装： 
 
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

中途拿着手机走了，忘记了在安装，结果不就断网了吗？它还不表示，到最后才表示失败。没有卸载，直接重装，等了半天又失败。好在及时回头，赶紧卸载再重装，等了很久，终于装好了。

## 基本命令  

[MAC上Homebrew常用命令 - 简书](https://www.jianshu.com/p/c60789934af1)

- 查看帮助信息
	
`brew help`

- 查看版本
	
`brew -v`

现在的版本2.1.4

- 更新Homebrew自己
	
`brew update`

- 安装软件包
	
`brew install [包名]`
```
//安装git
brew install git

//安装git-lfs
brew install git-lfs

//安装wget
brew install wget

//安装openssl
brew install openssl
```

- 查询可更新的包
	
`brew outdated`
  




