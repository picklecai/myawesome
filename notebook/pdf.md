# pdf文档处理

## 问题1:  

找了十几个pdf文件，运行一遍后出现这样的警告：  

```
Pdf Read Warning: Xref table not zero-indexed. ID numbers for objects will be corrected.
```

[PyPDF2不打印文本中的任何输出 - VoidCC](http://cn.voidcc.com/question/p-makfhcrm-sk.html)  

这个人也得到这种警告，但是他要解决的问题和我不同。貌似他的解决方法是encode

[PyPDF2 warning in PyPDF2 1.19 · Issue #36 · mstamy2/PyPDF2](https://github.com/mstamy2/PyPDF2/issues/36)  

这个没有看明白。

想想，我把那些报纸一样的文件去掉吧。只保留报告类的。

## 问题2:  

无论十几个还是几个，运行出来都是得到空文件。上面的警告在只剩下几个报告类文件后，没有了。但是出来的结果仍然是空文件，只不过以前是104页，现在是72页。  

我从网上下这些文件时，都费了一番时间。但是运行程序时，几乎是秒结束。

把with都改回来。加上file。close

用作者的文档试，也是空。

file.close去掉。

最常出现的错误是编码错误，非utf-8

现在换作者的文档试，可以了。

想想是不是因为我找的文档都是中文，无论繁简。于是找了几个英文的（主题是vipkid）。成功合并了。

