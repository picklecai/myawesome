# 关于GitHub提交错误的问题  

[git - OS X上的GitHub客户端提交失败（“无法添加文件...”） - Stack Overflow](https://stackoverflow.com/questions/23304734/github-client-on-os-x-commit-fail-failed-to-add-file)

`Failed to add file xxx  `  

> 我有同样的问题。在.git我想要创建新存储库的位置有一个现有的存储库。我删除了它并创建了一个新的。
如果您不确定.git存储库的目标位置是否存在，请执行此操作（在Unix计算机上）：
```
$> cd <path>
$> ls -aef 
```

> 这应该显示隐藏文件（如.git）。现在您有两个选择：

> 删除.git目录：
`$> sudo rm -R .git`

> 或更改所有者权利。


