看到了这篇教程。记录。 
[译27 个Jupyter Notebook的小提示与技巧 - Focus on ML & DM](http://liuchengxu.org/pelican-blog/jupyter-notebook-tips.html) 
[Jupyter Notebook的27个窍门，技巧和快捷键 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1135643)



## ## 1. 命令窗口  

> Cmd + Shift + P (  Linux 和 Windows下 Ctrl + Shift + P亦可)调出命令面板。这个对话框可以让你通过名称来运行任何命令——当你不知道某个操作的快捷键，或者那个操作没有快捷键的时候尤其有用。

## ## 2. 选择多个cell:   

> 
	▪	Shift + J 或 Shift + Down 选择下一个cell。
	▪	Shift + K 或 Shift + Up 选择上一个cell。
	▪	一旦选定cell，可以批量删除/拷贝/剪切/粘贴/运行。当你需要移动notebook的一部分时这个很有用。 
选择多个cell比较有用。整体移动方便。

## ## 3. 跨文本粘贴  

[python — 是否可以将单元格从一个Jupyter笔记本复制到另一个？](https://www.it-swarm.net/zh/python/%E6%98%AF%E5%90%A6%E5%8F%AF%E4%BB%A5%E5%B0%86%E5%8D%95%E5%85%83%E6%A0%BC%E4%BB%8E%E4%B8%80%E4%B8%AAjupyter%E7%AC%94%E8%AE%B0%E6%9C%AC%E5%A4%8D%E5%88%B6%E5%88%B0%E5%8F%A6%E4%B8%80%E4%B8%AA%EF%BC%9F/827511170/)

上面用命令的办法，只能在同一个book里批量移动代码块。如果想要把一批代码块都移到另一个book里，在mac下就使用command

> 为了跨选项卡执行此操作，您应该使用Ctrl-C和Ctrl-V（在Mac上为Cmd-C和Cmd-V）。

成功把自动化文本里的抓取部分都移到另一个文本里了。上面的命令是复制，复制完后删除了原文本中的代码块。

## ## 4. 合并单元格  

`shift + M`

## ## 5. 显示多个语句的运行结果

在代码最上方，先运行如下两句：  

```
# ipython输出各行结果
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
然后运行正常语句，可以出结果。如果放在一个单元格内一起运行，则不行。

## 6. 改变windows下默认路径

[总结：修改Anaconda中的Jupyter Notebook默认工作路径的三种方式_开发工具_u014552678的博客-CSDN博客](https://blog.csdn.net/u014552678/article/details/62046638)

这篇文章给出了三个方法，都不奏效。已经按照他说的把属性中的起始位置改成自己的路径，右键属性进入并修改起始位置的地址为自己的路径，然而不行。

然后看到了下面这个网址。

[修改Jupyter Notebook的默认工作目录_开发工具_戴翔的技术博客-CSDN博客](https://blog.csdn.net/yuanxiang01/article/details/79217469)

> 右击JupyterNotebook快捷方式，选择【属性】，删除【目标】属性中的【%USERPROFILE%】，点击【应用】–【确定】。

成功了。

