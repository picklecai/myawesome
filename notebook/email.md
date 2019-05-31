# 邮件  

本来不太想玩邮件，想想试试吧。

没想到一试就出来问题了  

```
import smtplib

smtpObj = smtplib.SMTP('mail.163.com', 25)
smtpObj.ehlo()
```

错误提示是：  

```
ConnectionRefusedError: [Errno 61] Connection refused

```
[Python3实现163邮箱SMTP发送邮件 - weixin_40475396的博客 - CSDN博客](https://blog.csdn.net/weixin_40475396/article/details/78693408)提到有邮箱授权的问题。  

第二天想起来，这个服务器填错了，应该是smtp

```
import smtplib

smtpObj = smtplib.SMTP('smtp.163.com', 25)
smtpObj.ehlo()
```

这就对了，有正常输出了。 

### 登录  

如果使用密码登录，则会输出：  
```
SMTPAuthenticationError: (535, b'Error: authentication failed')

```
使用授权码登录则正常：  

```
(235, b'Authentication successful')

```

### 发邮件 

无论是给qq邮箱还是gmail邮箱发送，都失败。错误信息为：  

```
SMTPDataError: (554, b'DT:SPM 163 smtp10,DsCowADXwbimJ+9cbRZ+Ig--.17524S3 1559177175,please see http://mail.163.com/help/help_spam_16.htm?ip=117.60.179.70&hostid=smtp10&time=1559177175')

```

[企业退信的常见问题？-163邮箱常见问题](http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html)

> •554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；

有人说因为没有写header，没有subject和内容分开……

[554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件； - Katios - CSDN博客](https://blog.csdn.net/sinat_21302587/article/details/69388526)

于是改成这样：  

```
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'pickle.ahcai@163.com'
receiver = input()
content = 'Dear Cai, thanks for all fish.'
title = 'So long'

message = MIMEMultipart()
#   # 内容, 格式, 编码
message['From'] = "{}".format(sender)
message['To'] = receiver
message['Subject'] = Header(title, 'utf-8').encode()
message.attach(MIMEText(content, 'plain', 'utf-8'))


smtpObj.sendmail(sender, receiver, message.as_string)
smtpObj.quit()
```

现在变成了：  
```
TypeError: expected string or bytes-like object

```

也没有什么好主意，想想把type类型打印出来看看吧。

于是增加了一句`print(type(message.as_string))`，出来的怎么是`class:method`？我忘了写括号了？？？？  

增加了括号，马上好了。。。。。🤦‍♀️🤦‍♀️

查看邮箱，也收到了。

gmail和qq的都收得到。用逗号隔开，可以一起发送。也可以添加抄送人。正文用回车符\n也可以隔开。


