```
import docx, os

path = r'G:\删除1\应用程序\msword\15360.doc
doc = docx.Document(path)
```

简单运行一下，发现错误：

```
PackageNotFoundError: Package not found at 'G:\删除1\应用程序\msword\15360.doc'
```

以为是docx没有安装好，不过那样不应该在import上出错吗？后来发现原来docx只能处理docx，不能处理doc。真是凄惨。

[Python：读取 .doc、.docx 两种 Word 文件简述及“Word 未能引发事件”错误 - 简书](https://www.jianshu.com/p/9a10410e25d5)

*Python* 中可以读取 *word* 文件的库有 *python-docx* 和 *pywin32*。

下表比较了各自的优缺点。

|             | 优点              | 缺点                                  |
| ----------- | ----------------- | ------------------------------------- |
| python-docx | 跨平台            | 只能处理 .docx 格式，不能处理.doc格式 |
| pywin32     | 仅限 windows 平台 | .doc 和 .docx 都能处理                |

然而对pywin32的介绍是：

> 这个库很强大，不仅仅可以读取 *word*，本文仅介绍其读取 *word* 功能。网上介绍用 *pywin32* 读取 *.doc* 的文章真不多，因为，**真心不好用**。



神奇的是，它似乎无须安装。因为我运行`pip install pywin32`时，windows给出的提示是：`Requirement already satisfied: pywin32 in c:\programdata\anaconda3\lib\site-packages (227)`

它的引用是这样的：

```
from win32com.client import Dispatch
```