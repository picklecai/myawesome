# Tkinter  

教程：[Tkinter GUI 教程系列 | 莫烦Python](https://morvanzhou.github.io/tutorials/python-basic/tkinter/)

## 1. 基本过程  

```
import tkinter

windows = tkinter.Tk()
windows.title('Title')
windows.getmetry('640x480')
windows.mainloop()
```
这个过程基本上是每个使用了tkinter的程序都必须有的，以至于我昨天一直Ctrl+C以及Ctrl+V。  

需要注意的是：  

- import的tkinter，到了python3里，需要全部小写。以前是T大写。  
- title()是函数，不是属性，如果不是这样设置，那么窗口就会给自己一个自动命名的title。 
- getmetry()的参数是字符串，乘号✖️要用小写字母x，一不小心写成‘*’那就等着出错吧。  
- mainloop()似乎是放在哪里都可以，不一定要放到程序末尾。  
- 但是涉及到定义函数，就不能像普通python一样碰到了函数就去找函数了，得在使用之前先定义好。

## 2. 基本元素  

	1.	Label & Button 标签和按钮
	2.	Entry & Text 输入, 文本框
	3.	Listbox 列表部件
	4.	Radiobutton 选择按钮
	5.	Scale 尺度
	6.	Checkbutton 勾选项
	7.	Canvas 画布
	8.	Menubar 菜单
	9.	Frame 框架
	10.messagebox 弹窗

对它们的操作基本上是放在参数里的，常用参数有parent(这个如果省略了就是定义成tkinter.Tk()的那一个，不需要写出parent，只需要写parent的名称)，text，bg，width和height。有按钮功能的会有command。

### 2.1 设置文本  

- 在定义时设置：  
固定文本用`text=`，不固定文本用`textvariable=`  

- 在定义之后设置：  
`widgetname.config(text=)`

适用于Label。button一般设置固定值就够了。  

listbox，虽然设置后不会改变单项，但是需要一串值一起赋，所以也借助变量。先定义一个列表list，再把列表的值赋给它的参数listvariable  

```
var2 = tkinter.Variable()
month_list = ['May', 'June', 'July', 'August', 'September']
var2.set(['Janary','Februry','March','April'])

ls = tkinter.Listbox(root, listvariable=var2, width=15)
```
菜单menubar，它的参数不是text，是label：  

```
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
```

总之，需要经常更换文本的，就只有Label了。注意，不要写成lable  

### 2.2 文本的传递  

Label的动态赋值过程是这样的：  

```
var = tkinter.StringVar()
tkinter.Label(textvariable=var).pack()
var.set('xxxxxxxx.')
```
效果和上面说的config一样：  

```
`widgetname.config(text=)`
```

但是似乎不能在同一段里同时用这两种？  

```
var = tkinter.StringVar()
l = tkinter.Label(root, width=20, textvariable=var, bg='#7DECF5')
l.pack()

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()

def print_selection():
    var.set('')
    if var1.get()==1 and var2.get()==0:
        var.set('I love only Python')
    elif var1.get()==0 and var2.get()==1:
        var.set('I love only C语言')
    elif var1.get()==1 and var2.get()==1:
        var.set('I love both')
    else:
        var.set('I dont love either')
```
这样有效！ 

```
l = tkinter.Label(root, width=20, text=' ', bg='#7DECF5')
l.pack()

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()

def print_selection():
    if var1.get()==1 and var2.get()==0:
        l.config(text='I love only Python')
    elif var1.get()==0 and var2.get()==1:
        l.config(text='I love only C语言')
    elif var1.get()==1 and var2.get()==1:
        l.config(text='I love both')
    else:
        l.config(text='I dont love either')
``` 

这样也有效！！！

```
var = tkinter.StringVar()
l = tkinter.Label(root, width=20, textvariable=var, bg='#7DECF5')
l.pack()

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()

def print_selection():
    var.set('')
    if var1.get()==1 and var2.get()==0:
        var.set('I love only Python')
    elif var1.get()==0 and var2.get()==1:
        var.set('I love only C语言')
    elif var1.get()==1 and var2.get()==1:
        l.config(text='I love both')
    else:
        l.config(text='I dont love either')
```
这样无效！！！原因是Label定义里少了参数text，就没法对text进行config了。  

要想获取某Label的值，用`cget('text')`

```
for grid in grid_list:
        alltext = alltext + grid.cget('text')
```
grid_list是个Label的list，所以其中每个元素都是一个Label。对它们进行cget('text')的操作就能得到text，如果参数是其他也可以，例如`xxname.cget('command')`。

### 2.3 Button的state  

Button有个state参数，可以冻结按钮，它一共有三个值：active, disabled, normal  
也是用在config里：  

```
btn.config(state='disabled')
```

### 2.4 是否需要全局  

注意，command的函数，一定要先定义好，才能在command中使用，否则出错。  
这里出现了btn和command互相调用的情况，就把btn设置为全局了。  

```
def chess_in():    
    …………
    if len(alltext)==9:
        user_label.config(text='Game over!')
        btn.config(state='disabled') # 游戏结束后不能再玩。

global btn
btn = tkinter.Button(root, text='Submit', command=chess_in)
btn.grid(row=7, column=1)
```

经过反复测试，发现不把btn设置为全局也没关系。但如果先定义btn，再定义chess_in，就一定会出问题。  

### 2.5 insert  

`xxname.insert('',var)`

第一个参数，字符串形式有两个：'end', 'insert'。另外还有int形式，就是指在列表中的位置，以listbox为代表。  

```
def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    t.insert('end', var)
```

Listbox中的用法： 
 
```
ls = tkinter.Listbox(root, listvariable=var2, width=15) #不赋初值也没关系
for month in month_list:
    ls.insert('end', month)
ls.insert(9, 'Octorber')
```

## 3. 放置位置  

分三种：  

```
pack()
grid()
place()
```

如下：  

似乎是同一个窗口内的元素只能选择同一种放置方式。不能上面的grid，下面的pack。


### 3.1 pack:  

```
import tkinter

root = tkinter.Tk()
root.title('Pack Grid Place')
root.geometry('640x480')

tkinter.Label(text='top', bg='pink').pack(side='top')
tkinter.Label(text='bottom', bg='pink').pack(side='bottom')
tkinter.Label(text='left', bg='pink').pack(side='left')
tkinter.Label(text='right', bg='pink').pack(side='right')'''

root.mainloop()
```
### 3.2 grid  

```
import tkinter

root = tkinter.Tk()
root.title('Pack Grid Place')
root.geometry('640x480')

for i in range(3):
    for j in range(3):
        tkinter.Label(root, text='null', bg='pink',borderwidth=2, relief="groove", width=10, height=5).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
root.mainloop()
```
### 3.3 place  

```
import tkinter

root = tkinter.Tk()
root.title('Pack Grid Place')
root.geometry('640x480')

tkinter.Label(text=' ', bg='pink', padx=10, pady=10).place(x=100, y=100, anchor='se')
tkinter.Label(text=' ', bg='yellow', padx=10, pady=10).place(x=100, y=100, anchor='nw')
tkinter.Label(text=' ', bg='red', padx=10, pady=10).place(x=100, y=100, anchor='sw')
tkinter.Label(text=' ', bg='blue', padx=10, pady=10).place(x=100, y=100, anchor='ne')

root.mainloop()
```

### 3.4 两个例外  


菜单menubar是个例外，定义好了之后不能用pack类方法放到窗口中去，必须要用下面这个：  

```
window.config(menu=menubar)
```

messagebox是另一个例外，它总是按钮触发出来的，所以永远活在command的函数内部，无须放置具体位置。  

```
def hit_me():
    tkinter.messagebox.showinfo(title='Information', message='This is a normal information.')
    
b = tkinter.Button(root, text='hit me', command=hit_me)
```

