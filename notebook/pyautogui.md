# python要控制键盘鼠标啦  

做实验的在线画板：[Sumopaint 2.0](https://sumo.app/paint/ch)

## 初级  

```
pyautogui.size()
```
这个结果的类型是pyautogui.Size，并不是元组。不过它可以当作元组来用，直接赋值给宽高没问题。  

```
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
```
这一段运行之前，mac要求授权给终端来控制。授权后，就看着鼠标🖱️自己在那里表演，哈哈哈哈～～～

## 鼠标在哪里  

这一段程序，一开始就写了一句话：  
```
print(pyautogui.position())
```
然而发现这句话的问题是程序一直在不停地向下刷，根本就看不清现在在哪里。  

怎么才能让程序觉得只有鼠标动了才打印结果呢？显然很难控制。

作者的方法是：打印出当前内容后，仍然在当前行打印退格键，就OK了。  

```
#!/usr/bin/env python
# _*_coding:utf-8_*_

import pyautogui


def cursor():
    print('Press Ctrl - C to quit.')
    try:
        while True:
            # print(pyautogui.position())
            x, y = pyautogui.position()
            positionStr = ('X: %s; Y: %s') % (str(x).rjust(4), str(y).rjust(4))
            print(positionStr, end='')  # 这一行忘记写end=‘’
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\nDone.')


def main():
    cursor()

if __name__ == '__main__':
    main()

```
print的flush，是自动刷新缓冲区的。改成False之后，问题就是光标会在两端闪动，看着很不舒服。  

另外sublime的pep8检查不知道怎么回事，坚持觉得第一次出现的`end=''`是语法错误。

### 自动填表单  

程序是照抄的，其他都好，就是下拉框不行，我在down前后都分别加了enter也不行。但是如果充满旧数据，偶尔能成功一次，然后就自我放飞。很纳闷。

```
        if person['source'] == 'wand':
            pyautogui.typewrite(['enter', 'down', 'enter', '\t'])
        elif person['source'] == 'amulet':
            pyautogui.typewrite(['enter', 'down', 'down', 'enter', '\t'])
        elif person['source'] == 'crystal ball':
            pyautogui.typewrite(['enter', 'down', 'down', 'down', 'enter', '\t'])
        elif person['source'] == 'money':
            pyautogui.typewrite(['enter', 'down', 'down', 'down', 'down', 'enter', '\t'])

```
还有个问题是：mac里的sublime怎么这么慢呢？  


