# python challenge的有趣笔记

## 1. 字符替代——翻译

像早期密码一样，以字母表向右错位两位为例。
给定一个密文，给定一个替代规则，要求翻译出明文。  

### 1.1 常规做法
  
密文字符串，密钥字符串，都转为列表。对密文中每一个字符，都到密钥中去查找，一旦查到，就用替代字符串中对应的来替换。最后把列表再转成字符串，输出。  

由于替代规则中“向右错位两位”会产生列表溢出的问题，干脆把替代字符串明确写出来。例如：  
```
alpha = 'abcdefghijklmnopqrstuvwxyz'
beta  = 'cdefghijklmnopqrstuvwxyzab'  
```
程序中使用了嵌套循环。因此运算量比较大。  

### 1.2 maketrans方法  

str有个maketrans方法，专门用来解决密钥翻译为明文的问题。分两步：  
第一步：  
把替代规则装进一个字典中，  `str.maketrans(alpha, beta)`所返回的是一个dict类型数据。  
第二步：  
用这个字典去翻译密文，`msg.translate(刚才这个dict)`，translate方法返回的是字符串类型sr。 

把`str.maketrans(alpha, beta)`打印出来可以看到，这个字典的键就是alpha字符串对应的ascii码，值就是beta字符串对应的ascii码。

可以根据字典的思路，再写一个。要注意，**判断字符是否在字典中，这个还是不能少**，因为有空格等非字母字符，它们不在字典中，会引发字典的keyError错误。这种错误主要是字典中不存在对应的键造成的。   

### 1.3 善用ASCII码  

有一对方法，`chr()`和`ord()`，前者把ASCII码数值转换为字符，后者把字符转换为ASCII码数值。用在这个规则“向右错位两位”正好。如果规则不是这样错位的，就不能用了。  

好处就是少用了一层循环。

#### 附： `''.join(list)`  

除了现成的方法外，其他借助于列表完成的方法，都多亏了这一句**快速列表转字符串**。

## 2. 字符串中的字符计数  

### 2.1 字典的setdefault  

用字典来存放计数结果，形式为`{'某字符':countnum，……}`  

为了计数方便，就用了字典的设置默认值方法：  

`dictionary.setdefault(character, 0)`  

第一个参数是要检查的键，第二个参数是如果这个键不存在时，要设置的值。如果存在，就返回它的值。

一般用这个方法是增加键，在这个例子中，是用来辅助新键加入以方便计数。

### 2.2 字典的get

看了答案，发现作者用的是字典的get方法。比较起来，由两句变为一句： 
用 setdefault：  

```
count = {}
for character in msg:
	count.setdefault(character,0)
	count[character] +=1
```
用 get:  
```
count = {}
for character in msg:
	count[character] = count.get(character,0) +1
```

原因是get直接返回键的值，在这个例子中就可以直接+1：  
> Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
> 
> get()方法语法：
`dict.get(key, default=None)`

从视觉上来说，setdefault会更容易懂一些：先赋值，再计数➕1。

### 2.3 字典的排序  

这里说的不是普通的按键或按值排序，而是这个：  
`collections.OrderedDict()`  

其中collections.是要import的。排序依据是放入先后。如果顺序不同，字典就不等值。（普通的字典只要键值一致，无论顺序如何，都是等值的）

### 2.4 filter和string

更牛叉的来了。鉴于题库给的字符串里非字母太多。作者提供了一个投机方法：把直接字母挑出来。  

用了string.ascii_letters和filter函数。  

[Python3 filter() 函数 | 菜鸟教程](http://www.runoob.com/python3/python3-func-filter.html)

filter函数，两个参数中，第一个是函数，第二个是待检查的字符串。在python3中，它的返回值是个filter对象，不是直接的字符串。

```
import string

''.join(list(filter(lambda x:x in string.ascii_letters, msg)))
```  
第一个参数为：
`lambda x:x in string.ascii_letters`  
这个函数的作用就是过滤器。再看这个例子：  

```
def is_odd(n):
    return n % 2 == 1
 
tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)
```
这里用来做参数的is_odd就是过滤是否是奇数的。上面那个就是过滤是否是字母的。  

所以这个过滤器函数的返回值应该是True 或 False。  

把第二个参数（是个字符串）中符合过滤器要求的留下来，重新组成字符串。在python2中，它直接返回字符串。在python3中，它返回的是过滤数据类型，不过可以很方便地转换成列表再到字符串。

### 2.5 查看是否字母

```
print(''.join([character for character in msg if character.isalpha()]))
```

和filter以及string的思路一样  

这个思路下还可以走正则，毕竟正则写字母还是比较容易的。  

```
import re

print re.findall(r'[a-z]', msg)

```

### 2.6 字符串直接计数  

任何字符串都有count方法，参数是待计算字符，返回是这个字符的出现次数。  

```
for i in msg:
    l = msg.count(i)
    if l<20:
        print('%s : %d'%(i,l))
```
这个方法效率不高，运行时看得到卡顿过程。不像上面其他方法一样秒出结果。因为它针对每一个字符都去计数了。而待查字符串中重复甚多。

### 2.7 用maketrans，只删除不翻译  

类似上面那个挑出字母来的做法。

```
translator = str.maketrans('', '', "[]{}()#$%^@+!*&_")
msg.translate(translator).replace('\n','')
```
相当于把要删除的那些替换（翻译）为None  

### 2.8 不计频，只看有没有出现过  

```
tab = []
for i in msg:
    if tab.count(i)==0:
        tab.append(i)
print(''.join(tab))
```
原来列表是可以直接对其中的元素进行计数的。本质上来说，**列表的count和字符串的count**是一回事。  

### 2.9 用集合  

```
checklist = set(msg)
for i in checklist:
    print('%s: %d'%(i, msg.count(i)))
```
这个方法的缺点和pprint一样，顺序没有了。要猜英文单词。  

## 3. 寻找被三个连续大写字母包围的小写字母  

### 3.1 9字符串

用一个9字符组成的字符串，判断是否符合‘aAAAaAAAa’的规律，如果符合，就把中间的a保存起来。 
9个字符，每次都删除第一个，最后一个append下一个字符。估计比较费时，但有效。 

### 3.2 正则re模块  

新增两点认识：  
1. 使用分组，就可以不用考虑怎么提取中间小写字母的问题，只会输出分组。  
2. 原来`re.compile(r'Regex').finall(string)`相当于`re.findall(r'Regex', string)` 

比较：  

```
r'[a-z]+[A-Z]{3}[a-z][A-Z]{3}[a-z]+'
```
和

```
r'[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+'
```
前者把符合条件的整串字符串都输出，后者只输出括号（分组）中的  

```
re.findall(参数1Regex，参数2string)
```
相当于先`re.compile`再`.findall(string)`  

现在只需要一行代码就完成任务了：  

```
print(''.join(re.findall(r'[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+', msg)))
```

## 4. 解链锁  

怎么从网页上读取并解析内容。上次用的是urllib，好多人反应这个模块不好用。于是今天试了一下requests。和网络环境很有关系，很容易timeout。两种方法都是。  

试了好几次，终于成功了。

```
import re, requests

digital = '12345'
i = 1
while True:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php' + '?nothing=' + digital
    i+=1
    p = requests.get(url, verify=False, timeout=None)
    if 'Divide' in p.text:
        digital = str(int(digital)/2)
    else:
        digital = ''.join(re.findall(r'nothing is (\d+)', p.text))
    if p.text.find('html')!=-1:
        break
print(i, p.text)
```
requests方法明确多了。但是对于超时是否要等，这句话我还不怎么有数。

`if 'Divide' in p.text`这一句，避免了16044/2的莫名其妙。  

`''.join(re.findall(r'nothing is (\d+)', p.text))`这一句可能避免了两个数字那个的坑。  

## 5. pickle  

### 5.1 不用文件，直接用pickle读取  

可以不必先保存，直接用pickle，但是不用load，用loads。

```
import requests, pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
a = pickle.loads(requests.get(url).content)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j][0]*int(a[i][j][1]),end='')
    print('\n')
```

`requests.get(url)`，如果`.content`，则结果是二进制形式，如果`.text`，则结果是str。  

### 5.2 善用列表推导式  

上面的画法，改用列表推导式：  

```
for line in a:
	print(''.join([ch*count for ch, count in line]))
```

合并列表推导式：  

```
print('\n'.join([''.join([ch*count for ch, count in line]) for line in a]))
```
里面一层的推导式结果list需要先join起来，作为字符串，再给外面一层的推导式用。

