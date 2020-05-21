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



## 3.  3211破解

[SublimeText-3211-License-Key-/Key at master · AchrafIdir/SublimeText-3211-License-Key-](https://github.com/AchrafIdir/SublimeText-3211-License-Key-/blob/master/Key)

```
----- BEGIN LICENSE -----
Member J2TeaM
Single User License
EA7E-1011316
D7DA350E 1B8B0760 972F8B60 F3E64036
B9B4E234 F356F38F 0AD1E3B7 0E9C5FAD
FA0A2ABE 25F65BD8 D51458E5 3923CE80
87428428 79079A01 AA69F319 A1AF29A4
A684C2DC 0B1583D4 19CBD290 217618CD
5653E0A0 BACE3948 BB2EE45E 422D2C87
DD9AF44B 99C49590 D2DBDEE1 75860FD2
8C8BB2AD B2ECE5A4 EFC08AF2 25A9B864
------ END LICENSE ------
```

## 4. 安装Package Control

CTRL+` (ese按键下)，打开sublime命令输入框，将下述代码粘贴到命令行中，直接Enter执行：

**sublime text 3** ：

```
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp  = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try           manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```