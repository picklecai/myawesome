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

