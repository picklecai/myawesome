# app开发  


[利用python开发app实战 | nMask's Blog](https://thief.one/2018/05/08/1/)

[如何Python写一个安卓APP-又耳笔记-51CTO博客](https://blog.51cto.com/youerning/1733534)

## 1. 第一个kivy应用  

两个文件：一个是python，一个是kivy

```
# main.py

!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App


class HelloApp(App):
    pass

if __name__ == '__main__':
    HelloApp().run()

```
kivy的文件：  

```
# hello.kv

Label:
    text:'Hello, World! I am ahcai.'
```

需要注意的是**kivy文件的命名规则**，就是把python函数里那个run的主体（自己定义的类）拿出来，去掉app，全小写。

运行时，只要运行`python main.py`即可蹦出一个图形界面，上面内容就是kivy文件中规定的文本内容。太 帅了😄😄😄

## 2. 打包apk

未遂待续

## 3. 第二个应用

参考：[kivy学习笔记－基础篇 - cloveses的专栏 - CSDN博客](https://blog.csdn.net/cloveses/article/details/80369764)

### 3.1 一个根部件

因为kv文件里只能有一个根部件，所以就需要使用form里。

上一个界面，直接添加一个按钮的报错如下：  

```
     'Only one root object is allowed by .kv')
 kivy.lang.parser.ParserException: Parser: File "/Users/caimeijuan/github/myawesome/_src/kivy/note.kv", line 3:
 ...
       1:Label:
       2:    text:'Hello, World! I am ahcai.'
 >>    3:Button:
       4:    text:'click me.'

```
添加了一个form后，需要在py文件中添加它的类，它是继承自kivy自己的BoxLayout的。（看起来kv文件的命名习惯就是首字母大写）

```
# main.py

#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyForm(BoxLayout):
    pass


class NoteApp(App):
    pass

if __name__ == '__main__':
    NoteApp().run()

```

kv文件已改名。  

```
# note.kv

MyForm:
<MyForm>:
    Label:
        text:'Hello, World! I am ahcai.'
    Button:
        text:'click me.'
```
### 3.2 界面布局

由于没有对Form做任何规定，所以实际界面就是左一半是标签，右一半是按钮。

[4.9KV语言 · Kivy官方文档中文翻译（基于Kivy1.9.1） · 看云](https://www.kancloud.cn/gthank/kivydoc/127817)

> 注意，当属性名以小写字母开头时，部件名首字母应当大写。遵循PEP8 Naming Conventions是被鼓励的。

所以才都是首字母大写，因为都是部件。

BoxLayout就是盒子布局，我觉得相当于HTML的div。

label的文本水平垂直对齐：  

```
        Label:
            size_hint:1,1
            text:root.label_text
            text_size:self.size
            halign:'center'
            valign:'middle'
```
找到布局水平和垂直不起作用的原因了，没写到BoxLayout中，写到myform中了。

正确的写法是这样：  

```
MyForm:
<MyForm>:

    padding:20
    spacing:10
    text_input: text_box

    BoxLayout:
        orientation: 'vertical'

        TextInput:
            id:text_box

```

备份一下Box布局：  

```
# note.kv

MyForm:
<MyForm>:
    text_input: text_box

    BoxLayout:
        orientation: 'vertical'
        padding:20
        spacing:10
        Label:
            text:'INPUT:'
            text_size:self.size
            bold:True
            font_size:18
            size_hint:1,.05
            color:1,1,1,1
            canvas.before:
                Color:
                    rgba:0,0,0,1
                Rectangle:
                    pos:self.pos
                    size:self.size
            halign:'left'
            valign:'middle'
            font_name:'STHeiti Medium.ttc'

        TextInput:
            id:text_box
            font_name:'STHeiti Medium.ttc'
            size_hint:1,.2

        Button:
            text:'Save It'
            size_hint:1,.1
            background_normal:''
            background_color:0,0,1,1
            on_press:root.save()

        Label:
            size_hint:1,.05

        Label:
            text:'HISTORY:'
            text_size:self.size
            bold:True
            font_size:18
            size_hint:1,.05
            color:1,1,1,1
            canvas.before:
                Color:
                    rgba:0,0,0,1
                Rectangle:
                    pos:self.pos
                    size:self.size
            halign:'left'
            valign:'middle'
            font_name:'STHeiti Medium.ttc'

        Button:
            text:'Print History'
            size_hint:1,.1
            on_press:root.print_history()

        Button:
            text:'Clear'
            size_hint:1,.1
            on_press:root.clear() 

        Label:
            text:root.label_text
            text_size:self.size
            color:1,0,0,1
            canvas.before:
                Color:
                    rgba:1,1,0,1
                Rectangle:
                    pos:self.pos
                    size:self.size
            halign:'left'
            valign:'top'
            font_name:'STHeiti Medium.ttc'            
```

### 3.3 动作设置在哪个类里？  

```
# main.py

#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MyForm(BoxLayout):
    pass


class NoteApp(App):
    text_input = ObjectProperty()

    def buttona_act(self):
        print(self.text_input.text)

if __name__ == '__main__':
    NoteApp().run()

```

当main写成这样时，你觉得界面上的button该听谁的呢？

```
# note.kv

MyForm:
<MyForm>:
    orientation:'vertical'
    text_input:text_box

    BoxLayout:
        height:'40dp'
        size_hint_y:None

        TextInput:
            id:text_box
            size_int_x:20

        Button:
            text:'Button A'
            size_hint_x:20
            on_press:root.buttona_act()

        Button:
            text:'Button B'
            size_hint_x:20
```

如此运行的结果就是：

```
 File "kivy/weakproxy.pyx", line 30, in kivy.weakproxy.WeakProxy.__getattr__
 AttributeError: 'MyForm' object has no attribute 'buttona_act'

```
百思不得其解。 看了几个，也没有人犯这样的错。直到看到这个：  
[用户对问题“如何在Kivy中通过函数实现向新屏幕的转换？”的回答 - 问答 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/ask/149465/answer/260085)

> 你的问题之所以发生是因为ScreenFrame是BoxLayout(根据您的kv文件)，而不是Screen。因此，root(在这种情况下)，ScreenFrame)没有manager与此相关。

恍然，回去main一看，果然动作没写在myform下。岂止动作没写？全部都没有写。看界面看不出区别，动作一来就原形毕露了。赶紧改回来。 

```
# main.py

#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MyForm(BoxLayout):
    text_input = ObjectProperty()

    def buttona_act(self):
        print(self.text_input.text)


class NoteApp(App):
    pass

if __name__ == '__main__':
    NoteApp().run()
```

所以，现在也知道了，那些我看不懂的程序里，有很多类只是定义一下，然后就pass的，不一定是为了后面留接口。很可能删了就启动不起来了。

### 3.4 动作改进，让text文本显示在标签里

从这里[如何使用python更改kivy语言中的标签文本 - VoidCC](http://cn.voidcc.com/question/p-tkrerfal-gb.html)学习的更改label文本，没想到居然成功了。

```
# main.py 

from kivy.properties import ObjectProperty, StringProperty

class MyForm(BoxLayout):
    text_input = ObjectProperty()
    label_text = StringProperty() # 这是个文本属性

    def buttona_act(self):
        print(self.text_input.text)
        self.label_text = self.text_input.text # self是指root

```

```
# note.kv

    text_input:text_box
    label_text:label1.text (这一句可以去掉)

    BoxLayout:
        Label:
            id:label1 (这一句也可以去掉)
            size_hint:1,0.2
            text:root.label_text （这一句万万不能去掉）

        TextInput:
            id:text_box
            size_hint:1,0.2
```

只展示了这个label对应部分，其他略。

在python文件中，为root增加了一个文本属性，并给它赋值文本框的输入。  
在kv文件中，把这个文本属性和标签文本挂钩起来。

在size_hint中，0可以去掉，小数点不能去吧？


### 3.5 中文显示的问题  

[Kivy显示中文 - Leon's Blog——Study Notes - CSDN博客](https://blog.csdn.net/leon_founder/article/details/78572387)

这里的方法最简单，只要在相应部件中加上字体就可以了。

```
        Label:
            size_hint:1,1
            text:root.label_text
            text_size:self.size
            halign:'center'
            valign:'middle'
            font_name:'STHeiti Medium.ttc'
```

复杂的方法是这个[kivy中文的支持 - xia872409653的专栏 - CSDN博客](https://blog.csdn.net/xia872409653/article/details/81076131)，没试。

### 3.6 倒计时 

不成功的代码暂存：  

```
    def buttonb_act(self):
        def count_it(num):
            if num >= 0:
                self.label_text2 = str(num - 1)
            else:
                return
            self.label_text2 = str(num)
            Clock.schedule_once(lambda x: count_it(num), 1)
        Clock.schedule_interval(lambda x: count_it(5), 0)

```
运行正确的(来自：[[Python Programming for Android/IOS] Kivy简明教程,Python交流,技术交流区,鱼C论坛 - Powered by Discuz!](https://fishc.com.cn/thread-105901-1-1.html))：

```

class MyForm(BoxLayout):

    def buttonb_act(self):
        global stime, dtime
        stime = time.time()
        dtime = self.ids['time_slider'].value
        self.on_update()

    def callback(self, *argv):
        global stime, dtime
        if stime + dtime < time.time():
            self.ids['time_slider'].value = 0
            self.ids['time_counter'].text = '00:00:00'
            Clock.unschedule(self.callback)
            return False
        self.ids['time_slider'].value = dtime + stime - time.time()
        self.on_update()

    def on_update(self):
        Clock.schedule_once(self.callback, 0.2)

```
[4.5事件和属性 · Kivy官方文档中文翻译（基于Kivy1.9.1） · 看云](https://www.kancloud.cn/gthank/kivydoc/127813)


### 3.7 窗口尺寸

想把窗口设置成手机大小。没成功，不过其中全屏成功了：  

```

#!/usr/bin/env python
# _*_coding:utf-8_*_

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window


class MyForm(BoxLayout):
    text_input = ObjectProperty()
    label_text = StringProperty()

    def buttona_act(self):
        print(self.text_input.text)
        self.label_text = self.text_input.text


class TextApp(App):

    def build(self):
        Window.fullscreen = 'auto'
        Window.size = (750, 1206)
        self.title = 'Text Output'
        return MyForm()

if __name__ == '__main__':
    TextApp().run()
```
试了几次，明白了。是750*1206这一对数字中，1206超出了我的电脑的高度尺寸。设置小尺寸就可以了。

### 3.8 颜色

颜色的事情总算搞明白了，原来1等于255:  

```
        Label:
            text:root.label_text
            text_size:self.size
            color:0,0,1,1
            canvas.before:
                Color:
                    rgba:1,0,0,1
                Rectangle:
                    pos:self.pos
                    size:self.size
            halign:'left'
            valign:'top'
            font_name:'STHeiti Medium.ttc'
```

无论是rgb还是color，0就是0，而1就是255，所以只能表达6种纯色，表达不了其他颜色。

在上面的代码中，canvas代表标签背景色（蒙上了一层彩色布），color那里代表了字体颜色。

以上是标签的颜色，以下是按钮的颜色：  

```
        Button:
            text:'Save It'
            size_hint:1,.1
            background_color:0,0,1,1
            on_press:root.save()

```

如果也用canvas，before只能留一条边，after则会覆盖整个按钮，让它无法工作。所以要用background_color。

以上代码存在这样的问题：

[在Kivy中更改Button的背景颜色 | landcareweb.com](http://landcareweb.com/questions/39055/zai-kivyzhong-geng-gai-buttonde-bei-jing-yan-se)

> 啊，这是一个常见的混乱。问题是 Button.background_color 真的是作为一种 着色，而不仅仅是块颜色。由于默认背景是灰色图像（如果你制作一个没有样式的按钮，你通常会看到的图像），你最终看到的是那个灰色图像的红色 - 它是你观察到的暗红色。

更改：  

```
        Button:
            text:'Save It'
            size_hint:1,.1
            background_normal:''
            background_color:0,0,1,1
            on_press:root.save()
```
现在可以得到鲜蓝色了。


### 3.9 背景图像  

在时钟中，想给时间区域加个背景图像，发现只要在rectangle中加入source就可以了。不过在原来的canvas下加，背景颜色就没有了。解决办法是新增一个rectangle，不需要其他gridLayout，在新增中加source。

```
            canvas.before:
                Color:
                    rgba:1,1,0,1
                Rectangle:
                    pos:self.pos
                    size:self.size           
                Rectangle:
                    pos:self.pos
                    size:self.size
                    source:'wheel.gif'
```
觉得比例不对，但是rectangle不支持size_hint，于是把size写死，写成（300，300）

下一步是觉得字覆盖在图片上不好看。于是调整为字体靠上，但是有padding。padding只能是元组或list，不是4个，是两个。

```
            halign:'center'
            valign:'top'
            padding:(10,100)
```
现在界面就很和谐了。

### 3.10 动画

但是，原本是个gif的图片，到这里也不动了。想必要让gif动起来，不能让它做背景图片。

查到了`anim_delay `是控制动画播放速度的，它是Image的属性。于是直接在rectangle后加了个image，错误提示：  

```
You can add only graphics Instruction in canvas.
```
于是把它挪出了canvas，马上就动起来了。太帅了，虽然‘偏安于一隅’。

```
            canvas.before:
                Color:
                    rgba:1,1,0,1
                Rectangle:
                    pos:self.pos
                    size:self.size           
                Rectangle:
                    pos:self.pos
                    size:300,300
                    source:'wheel.gif'
            Image:
                pos:self.pos
                size:self.size
                source:'wheel.gif'
                anim_delay:1/20
```
接下来就只是布局问题了。改成这样就行了：  

```
            canvas.before:
                Color:
                    rgba:1,1,0,1
                Rectangle:
                    pos:self.pos
                    size:self.size
            Image:
                pos:self.pos
                size:300,300
                source:'wheel.gif'
                anim_delay:1/20
```

过了一天，对动画又有了新的想法。能不能让它只有在倒计时的时候才动呢？昨天想的是这个动画本身，只要载入了就会一直运动，无法控制的。今天想，在初始时载入静态，start后载入动态，stop后仍然改为静态，不就可以解决问题了？  

顺着这个想法，本来打算是不是要在python文件中去导入Image，导入什么样的image？灵感突来，不是应该使用id吗？  

这才理解到：self.ids['']，意思就是所有的id都在一个列表中。引用出来后，它的属性随便改。

那就这样了：  

```
# kv文件

            Image:
                id:bg_image
                pos:self.pos
                size:300,300
                source:'giphy.png'
                anim_delay:0.001
```

```
# py文件  

class MyForm(BoxLayout):
    def start(self):
        global stime, dtime
        stime = time.time()
        dtime = self.ids['time_slider'].value
        self.ids['bg_image'].source = 'giphy.gif'
        Clock.schedule_interval(self.callback, 0.1)

    def callback(self, *argv):
        global stime, dtime
        if stime + dtime < time.time():
            self.ids['time_slider'].value = 0
            self.ids['time_counter'].text = '00:00.00'
            return False
        self.ids['time_slider'].value = dtime + stime - time.time()

    def stop(self):
        self.ids['time_slider'].value = 0
        self.ids['time_counter'].text = '00:00.00'
        self.ids['bg_image'].source = 'giphy.png'
        Clock.unschedule(self.callback)

```
分别在start中和stop中更改source就行了。  

至于png文件从哪儿来，只要使用图像编辑软件把gif另存为png就万事大吉了。（一开始我强改扩展名，无效，🤦‍♀️）


### 3.11 倒计时  

#### 问题1: 不停止循环

```
class MyForm(BoxLayout):
    label_text = StringProperty()
    global num
    num = 10

    def countback(self, *argv):
        global num
        self.label_text = str(num)
        num = num - 1
        self.update()
        if num <= 0:
            print('Byebye.')
            # Clock.unschedule(self.countback)
            return False

    def update(self):
        Clock.schedule_interval(self.countback, 1)
```

退出循环，如果只依靠`return False`，则不会停止，会一直执行这个print。加上注释的这句`Clock.unschedule`，马上就好了，会停在1。

#### 问题2: 不是依次递减1

以上代码，在运行时，不依次递减。但是循环停止了后，如果继续按按钮，则会递减1。

按照时钟那个程序的样式，不用schedule_interval，还用schedule_once，是可以实现的：  

```
class MyForm(BoxLayout):
    label_text = StringProperty()
    global num   # 如果没有这个，countback中的num就没有初始值
    num = 10

    def countback(self):
        global num
        self.update()

    def update(self):
        Clock.schedule_once(self.callback, 1)

    def callback(self, *argv):
        global num
        self.label_text = str(num)
        num = num - 1
        self.update()
        if num < 0:
            print('Byebye.')
            Clock.unschedule(self.callback)
            return False
```

用schedule_interval，先打印在命令行，也是可以的：  

```
    def countback(dt):
        global num
        print(num)
        num = num - 1
        if num < 0:
            print('Byebye')
            return False

    Clock.schedule_interval(countback, 1)
```

转为界面上：  

```
    def countback(self):
        global num
        Clock.schedule_interval(self.callback, 1)

    def callback(self, *argv):
        global num
        self.label_text = str(num)
        num = num - 1
        if num < 0:
            # print('Byebye')
            return False
```

由于在两个函数之前已经写了一遍：
```
global num
num = 10
```
所以感觉countback中的global num好像没有什么用。忽然意识到，这个定义全局并赋初值的过程应该在countback中进行。这样无论什么时候按这个按钮，都是从10开始倒数的。否则运行完第一遍，再按按钮，就是从-1往下数了。

所以应该是这样的：  
```
class MyForm(BoxLayout):
    label_text = StringProperty()
    # global num  # 如果没有这个，countback中的num就没有初始值
    # num = 10

    def countback(self):
        global num
        num = 10
        Clock.schedule_interval(self.callback, 1)

    def callback(self, *argv):
        global num
        # print(num)
        self.label_text = str(num)
        num = num - 1
        if num < 0:
            print('Byebye')
            # self.label_text = 'Byebye'
            return False
```
countback的作用就是通过按钮提供入口，定义初始全局变量，不停地调用callback。  
callback的作用就是接收全局变量的初始值，并对它进行计算且输出计算结果，规定停止运行的条件。  

分工明确，简洁明了。

对于schedule_once那一段同理，根本不需要预先规定num数值，而是应该放在countback中。这样就总是会从10往下倒数。
改进后的schedule_once:  
```
class MyForm(BoxLayout):
    label_text = StringProperty()
    # global num  # 如果没有这个，countback中的num就没有初始值
    # num = 10

    def countback(self):
        global num
        num = 10
        Clock.schedule_once(self.callback, 1)

    def callback(self, *argv):
        global num
        # print(num)
        self.label_text = str(num)
        num = num - 1
        Clock.schedule_once(self.callback, 1)
        if num < 0:
            print('Byebye.')
            Clock.unschedule(self.callback)
            return False
```

同样，countback的作用是定义全局变量并赋初值，但是只调用了一次callback。   
那么，为什么也能实现连续倒数的效果呢？原因是callback内部，在接收全局变量并计算输出后，它自己又调用了一次自己。由于递归作用，就导致进入了循环。

在once中，无法使用`return False`停止运行。只能通过unschedule实现。这就是之前无法停止运行的原因。为什么呢？**还不理解**  

#### callback中的秒数

> callback()函数将会在1秒后执行。1秒参数是在执行该程序前等待的时间，以秒为单位。但是你可以使用特殊的值作为时间参数得到一切其它结果：   
	•	如果X > 0，则回调函数会在X秒后执行。   
	•	如果X = 0, 则回调函数会在下一帧执行。   
	•	如果x = -1，则回调函数在在下一帧之前执行。   
其中 x = -1最为常用。   

在上面的代码中试了一下，唯一的感觉就是快。


