# SAE笔记  

[免运维的云计算服务 - 新浪云](https://www.sinacloud.com/)

玩了半天，不要关机了连地址都没记住。写在这里吧。

## 1. 创建新应用  

控制台，点击创建新应用。原本担心只支持python2.7，发现如果选择独享环境就能自定义。代码管理方式也可以选择git。二级域名选择了pickle。


## 2. 代码管理  

在菜单 运行环境管理——代码管理中，可以看到git仓库。

进入代码所在目录，  
```
git clone https://git.sinacloud.com/pickle
```
后面要求输入安全邮箱和密码。安全邮箱就在这个页面上写着。  

成功后，由于第一次运行，啥也没有，所以终端提示说：  
```
warning: You appear to have cloned an empty repository.
```
然后进入这个文件夹：`cd pickle`

编辑代码并部署代码

```
#添加本地的文件改动
git add .
```

把四个代码文件都拖入新文件夹中， 然后运行下面的：  

```
#添加本地修改的备注信息
git commit -m 'Init my first app'

#将改动推送到远程仓库
git push origin master
```

commit这句成功了，但是push这句给出了提示： 

```
error: failed to push some refs to 'https://git.sinacloud.com/pickle'
```

全部提示是：

```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.07 KiB | 1.04 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote: 导出 Git 代码中...
remote: 构建程序中...
remote: Save files ok
-----> Unable to select a buildpack
remote: {"Code":1,"Error":"build image failed: exit status 1."}
remote: 错误：构建镜像失败
remote: error: hook declined to update refs/heads/master
To https://git.sinacloud.com/pickle
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to 'https://git.sinacloud.com/pickle'
```

#### 措施1:  

不知道从哪里知道的（[新浪云](https://www.sinacloud.com/doc/sae/docker/python-getting-started.html)）要加runtime来说明python版本。

#### 措施2:  

安装sae了。虽然不知道有啥用。

结果错误提示变成：  

```
Compressing objects: 100% (11/11), done.
Writing objects: 100% (14/14), 2.77 KiB | 1.39 MiB/s, done.
Total 14 (delta 2), reused 0 (delta 0)
remote: 导出 Git 代码中...
remote: 构建程序中...
remote: Save files ok
-----> Python app detected
-----> Network Connection Success
       !     Requested runtime ($ cat runtime.txt
       python-3.7.2) is not available for this stack (cedar-14).
       !     Aborting.  More info: https://devcenter.heroku.com/articles/python-support
remote: {"Code":1,"Error":"build image failed: exit status 1."}
remote: 错误：构建镜像失败
remote: error: hook declined to update refs/heads/master
To https://git.sinacloud.com/pickle
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to 'https://git.sinacloud.com/pickle'
```

又把这个文件删了。从`git add .` 开始，重新再来一遍。  现在的提示：  

```

remote: 部署程序中 .............
To https://git.sinacloud.com/pickle
 * [new branch]      master -> master
 
```

至少不出错了吧。但是启动失败。

又把那个文件runtime扒拉出来，先把python版本改成3.6.8，依然如故。然后把第一句去掉，只留下版本号这一句，貌似成功。

```
remote: 部署程序中 ....
To https://git.sinacloud.com/pickle
   0544d08..0339720  master -> master
```

但是启动依旧错误。

突然发现config.yaml、index.wsgi这两个文件是共享环境需要的，现在我这个独立环境不需要了。删了吧。创建app的任务，转到主程序上。



