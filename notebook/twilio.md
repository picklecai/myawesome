# 发送短信的模块——Twilio

官网地址：[Twilio - Communication APIs for SMS, Voice, Video and Authentication](https://www.twilio.com/)  

简单注册了一下，和这位兄弟[使用 twilio + python 给你的手机发短信 - fengfengdiandia的专栏 - CSDN博客](https://blog.csdn.net/fengfengdiandia/article/details/52719214)提的情况不同，没看到free api。  

注册后得到了三个值：ACCOUNT SID, AUTH TOKEN, TRIAL NUMBER

注册时一直惴惴不安，不知道是否支持中国手机。看到刚才那兄弟是中国手机，放心了一半。后来又一直担心是否能免费。因为一直看到$符号。现在明白了，这是试用版账户余额。我刚才给自己发了一条短信后，余额就少了。

抄代码时，一开始和作者以及刚才那人一样，用了`from twilio.rest import TwilioRestClient`。但是提示：  

```
ObsoleteException: TwilioRestClient has been removed from this version of the library. Please refer to current documentation for guidance.
```

在这里[python - TwilioRestClient removed - Stack Overflow](https://stackoverflow.com/questions/51878976/twiliorestclient-removed?noredirect=1&lq=1)，发现这个模块改名字了。

于是新的模块是Client。

又试了一下中文，也可以。


