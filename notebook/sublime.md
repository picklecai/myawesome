# 关于sublime使用的笔记  

好久不用sublime，也没有改造它。

## 1. 把默认的tab键变成4个空格  

[设置 sublime Text3 中的 Tab 键为 4 个空格 - Bingo - CSDN博客](https://blog.csdn.net/kl28978113/article/details/53066337)  

这次用的sublime是3.2.1，Build 3207

在最开始的Sublime Text菜单中，找到Preferences-> Settings，在弹出来的文本里，添加如下两行:

```
"tab_size": 4, "translate_tabs_to_spaces": true
```

左侧是这样：

```
{
    // Sets the colors used within the text area
    "color_scheme": "Monokai.sublime-color-scheme",

    // Note that the font_face and font_size are overridden in the platform
    // specific settings file, for example, "Preferences (Linux).sublime-settings".
    // Because of this, setting them here will have no effect: you must set them
    // in your User File Preferences.
    "font_face": "",
    "font_size": 10,
```

添加在右侧进行，效果是这样的：  

```
{
	"ignored_packages":
	[
		"Package Control",
		"Vintage"
	],
	"tab_size": 4,
   "translate_tabs_to_spaces": true,
}
```

## 2. 默认新标签打开文件，而不是新窗口

[sublime text 怎么在新标签中打开文件? - 知乎](https://www.zhihu.com/question/22325839)  

> 默认是在一个新窗口打开新文件，要想在新标签页打开文件，找到Preferences-> Settings，在弹出来的文本里，找到open_files_in_new_window并改为false。或者如果找不到就直接添加:`"open_files_in_new_window": false`

> 做完后重启，再打开新文件就会在新标签页了。




