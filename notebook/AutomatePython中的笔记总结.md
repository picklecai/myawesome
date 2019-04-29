# 一些常规做法  

## 1. 路径转换  

`os.path.dirname('路径')`，得到最后一个斜杠之前的内容。  
`os.path.basename('路径')`，得到最后一个斜杠之后的内容。  

结合`os.chdir()`，可以把路径转到和当前目录平行的其他目录中，或者转到父级目录。  

## 2. 隐式输入密码  

用了一个库：getpass  

这个库一共两个方法，一个是getpass，使输入的密码隐形。一个是getuser，知道当前用户是谁。  
getpass方法中有个stream参数，不是我以为的设置星星符号的。  

## 3. continue  

使用了循环语句中的continue，可以让循环语句段在执行第一个需要反复的语句后继续向后执行，而不必跳出循环。  

原来的写法：  
```
while typedPassword!=secretPassword :
    print('Access denied! Please enter again.')
    typedPassword = input("Enter your password again:")
    if typedPassword == secretPassword:
        break    

if typedPassword == '123456':
    print('This is not a good password.')    
    print('Access granted.')
else:
    print('Access granted. Your password has %d characters.' % len(typedPassword)) 
```

在看到密码验证通过后，跳出来输入反馈信息。

新的写法：  

```
# _*_coding:utf-8_*_
import os, getpass

os.chdir(os.path.dirname(os.getcwd()) + '/files/') # 转到父级文件目录
passWord = open(os.getcwd() + '/password.txt').read()
while True:
    guessWord = getpass.getpass('Enter your password:')
    if guessWord!=passWord:
        continue
    else:
        if guessWord == '123456':
            print('Access granted.','This is not a good password.', sep='\n')
        else:
            print('Access granted.','Your password has %d characters.' %len(guessWord), sep='\n')
        break
```

用`continue`不必跳出，等全部执行完毕再跳出。  

这种做法，如果有两个需要反复验证的，第二次的通不过会让第一次的再执行。  

书上这个例子就是这样：  

```
while True:
    name = input('Who are you?')
    if name!='Joe':
        continue
    password = input('Hello, Joe. What is the password?(It\'s a fish.)')
    if password == 'swordfish':
        break
print('Access granted.')
```   

回答joe通过用户名后，如果密码不对，又退回去问用户名了。

## 4. 快速给字典赋值  

`dict(zip(list1,list2))`  

zip的参数，只能是list，不能是range  

```
def getAnswer(answerNumber):
    dictMonths = dict(zip(list(range(1,13)),['January','February','March','April','May','June','July','August', 'September','October','November','December' ]))
    if answerNumber in dictMonths:
        return 'AnswerNumber is %d . This is in '%answerNumber + dictMonths[answerNumber]
    else:
        return 'AnswerNumber is %d . This is not in any month of the year.'%answerNumber 
```

## 5. try-except  

**执行跳到except代码块，就不会回到try代码块。**  

比较这两段：  

```
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Error:Invalid argument.")    
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(6))
```

第二段：  
```
def spam(number):
    return 42/number
   
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(6))
except ZeroDivisionError:
    print("Error:Invalid argument.")
```
第二段就不会执行`print(spam(6))`。

## 6. python的容错  

while子句不小心多缩进了4格，居然也运行正确。number变量拼写错误，导致次次死循环崩溃。

死循环：  
```
def collatz(number):   
    if number%2==0:
        number = number//2
    else:
        number = number*3+1  
    print(number)         
    return number
number = int(input('Enter an integer:'))
while True:
    if number!=1:
        nubmer = collatz(number)
    else:
        break
```

多缩进：  

```
def collatz(number):   
    if number%2==0:
        number = number//2
    else:
        number = number*3+1  
    print(number)         
    return number
number = int(input('Enter an integer:'))
while number!=1:
        nubmer = collatz(number)
```

## 7. global  

```
def collatz(number):   
    if number%2==0:
        number = number//2
    else:
        number = number*3+1  
    collatzList.append(number)        
    while number!=1:
        number = collatz(number)
    return number
number = int(input('Enter an integer:'))
collatzList = [number]
collatz(number)
print('The sequence collatz(%d) is: '%number, collatzList)
```
这段程序运行没问题。列表collatzList先赋值第一个number，然后在调用collatz的过程中逐渐增加。

当把调用执行过程如下一样包装进另一个函数时，列表collatzList在调用collatz的过程中不再新增，因为它是局部变量。这时必须增加**global**
```
def collatz(number):   
    if number%2==0:
        number = number//2
    else:
        number = number*3+1  
    collatzList.append(number)        
    while number!=1:
        number = collatz(number)
    return number
def caculateCollatz(number):
    global collatzList
    collatzList = [number]
    collatz(number)
    print('The sequence collatz(%d) is: '%number, collatzList)

number = int(input('Enter an integer:'))
caculateCollatz(number)
```

## 8. pprint

打印字典或嵌套字典，键值排序  

`pprint.pprint`和`pprint.pformat`的区别是，后者是得到字符串，而不是None。所以：  

```
pprint.pprint(sth)  
print(pprint.pformat(sth))
```
二者等价。  

如果字典包含嵌套的列表或字典，pprint就更有用。  

## 9. 判断是否汉字  


不用正则：  
```
def is_chinese(uchar):
    '''
    判断一个unicode是否是汉字
    '''
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
```

用正则：  
```
u"[\u4e00-\u9fa5]+"
```

## 10. 字典排序  

### 10.1 按放入顺序排序  

```
import collections
count =  collections.OrderedDict()
```
### 10.2 按键排序 

```
dict(sorted(dictionary_name.items(), key=lambda item:item[0], reverse=True))
```
 测试一下：  
 
 ```
 dictionary = {
    'Pickle':32,
    'Cindy':21,
    'Alice':19,
    'Coco':35,
    'Mia':18
}

sorted(dictionary.items(), key=lambda item:item[0], reverse=True)
 ```
输出结果为：  
`[('Pickle', 32), ('Mia', 18), ('Coco', 35), ('Cindy', 21), ('Alice', 19)]`

确实按名字倒序了。

测试有效。  

### 10.3 按值排序  

```
dict(sorted(dictionary_name.items(), key=lambda item:item[1], reverse=True))
```
用reverse调节升序还是降序。True代表降序。  

sorted结果是list，加上dict就能变回字典了。


## 11. 棋盘对弈切换双方  

想了半天，用了键为1和-1的字典，每次完了就让键乘以-1。
```
chess = {1:'X', (-1):'O'}
turn = 1
if inputN in listNumber:
    …… 
    turn = turn *(-1)
```

但是书上是这样处理的：  

```
turn = 'X'  

if ......:
    if turn=='X':
        turn = ‘O’
    else:
        turn = 'X'
```
貌似用字典比它的简洁？  

## 12. 下过棋的位置不许再下  

我用了一个列表来表示位置，每下一个位置，就把这个位置从列表中删除（不能用pop，必须用remove）  

```
listNumber = [1,2,3,4,5,6,7,8,9]
while listNumber!=[]:    
    inputN = int(input('%s turn. Where\'ll put?'%chess[turn]))
    if inputN in listNumber:
        ……
        listNumber.remove(inputN)
        ……
```
这样谁都不能在已经下过的位置再下棋了。


