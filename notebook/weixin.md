# 微信后台开发笔记 

暂存一个聊天机器人：[项目简介 - itchat](https://itchat.readthedocs.io/zh/latest/)

## 1. 乱折腾——web.py抄录未遂 

有点病急乱投医，

第一版用了这里的代码：[使用python一步一步搭建微信公众平台（一） - kevin的个人页面 - OSCHINA](https://my.oschina.net/yangyanxing/blog/159215)

抄录情况如下：  

```
# weixinInterface.py

# _*_coding:utf-8_*_
import hashlib
import web
import os


class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        # 获取输入参数
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        # 自己的token
        token = "hello2019"  # 这里改写你在微信公众平台里输入的token
        # 字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        # sha1加密算法

        # 如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

```

main.py的修改如下：  

```
@route('/weixin')
def weixin():
    from weixinInterface import WeixinInterface
    return WeixinInterface
```
requirement的修改如下： 

```
bottle
kvdb
web.py==0.40.dev0
```
由于安装web.py还折腾了很久。但是对它一点不懂。所以main的修改毫无价值。记录在这里。现在专心于bottle。以及有个人说会写xml就行的。  

## 2. 用bottle

思考一下需要完成的功能：  

- 制造一个验证token
- 接收用户端输入  
- 让用户打印已输入内容

### 2.1 token验证

官方给出的
[Token验证的流程](http://mmbiz.qpic.cn/mmbiz_png/PiajxSqBRaEIQxibpLbyuSK9B2CRwJYwMRFbDwdwNicNwcwhWaTuibPIqUwocStP6VicjxyGc2S96XlaNiciagkc26eKg/0?wx_fmt=png)，意思是：一个消息从微信来时就已经用hash加密过了，如果用同样的过程加密，能得到同样的结果，就证明它是从微信来的。否则就是其他来路，因为加密过程不一样，导致加密结果不一样。

每一个接收到的消息都有这样几个部分可以分解出来：
  
- signature
- timestamp
- nonce
- echostr

其中signature就是那个加密结果。  

token+timestamp+nonce现加密，和signature进行比较。

[对这几个参数的说明：](https://apir8181.github.io/system/2013/04/10/wechat-min.html)

> 微信开放平台的api文档里面说，当用户访问你的公众平台帐号时，腾讯会发送GET请求到你的公众平台处理服务器，里面有signature等参数，而我们需要相应的是一个xml。  
> 微信开放平台GET参数: 
> 
> * signature: 微信加密签名 
> * timestamp: 时间戳 
> * nonce: 随机数 
> * echostr: 随机字符串

原来在bottle中，要获得输入，就是`request.GET`，用它可以获得上面四个参数：  

```
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
```
照猫画虎，

```
@route('/')
def verify():
    try:
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'hello2019'
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print('handle/GET func: %s, %s' % (hashcode, signature))
        if hashcode == signature:
            return echostr
        else:
            return ''
    except Exception, Argument:
        return Argument
```

这个传到sae后，服务无法启动。

以为是路径问题，把地址改成'/wx'，还是如此。想了想，应该去看看日志啊。结果看了日志才知道，那个莫名其妙的Argument是有问题的。

对照刚才那个例文，又发现，根本没有把新接收的字符串拿去加密。  

于是逐字逐句改成：  
```
route('/')
def verify():
    try:
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'hello2019'
        list = [token, timestamp, nonce].sort()
        hashcode = hashlib.sha1(''.join(list)).hexdigest()
        print('handle/GET func: %s, %s' % (hashcode, signature))
        if hashcode == signature:
            return echostr
        else:
            return ''
    except Exception:
        return 'Verify Error'

```
这回传上去，成功了。页面显示为'Verify Error'，填入微信后台，依旧token验证失败。这回可能轮到xml上场了。

引入xml，都写全了。

```
def parse():
    root = xml.etree.ElementTree.fromstring(request.body.read())
    message = {}
    for child in root:
        message[child.tag] = child.text
    return message


@post('/wx')
def handleUserInput():
    message = parse()
    s = '''
    <xml>
        <from>%s</from>
        <to>%s</to>
        <timestamp>%s</timestamp>
        <content>%s</content>
    </xml>
    ''' % (message['FromUserName'],
           message['ToUserName'], str(int(time())), message['Content'])
    return s
```

依然是token验证失败。不知道是不是5050和80端口的问题。

用try-except包裹起来真是傻啊，所以赶紧去掉。果然看见是list排序出了问题，里面数据类型不一致。

```
Traceback (most recent call last):
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 862, in _handle
    return route.call(**args)
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 1740, in wrapper
    rv = callback(*a, **ka)
  File "main.py", line 43, in verify
    list.sort()
TypeError: '<' not supported between instances of 'NoneType' and 'str'

```

对应的是这一段：  

```
    print(request.GET)
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    echostr = request.GET.get('echostr')
    token = 'hello2019'
    list = [token, timestamp, nonce]
    list.sort()
```
就是`list.sort()`出的问题。

突然惊觉，我居然用list做变量名！！！！疯掉了！！～！！！～～～这可真是个低级错误～～～

顺手把它们str了一下：  

```
def verify():
    print(request.GET)
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    echostr = request.GET.get('echostr')
    token = 'hello2019'
    list1 = [token, str(timestamp), str(nonce)]
    list1.sort()
```
现在换了个提示：  

```
 File "main.py", line 44, in verify
    hashcode = hashlib.sha1(''.join(list1)).hexdigest()
TypeError: Unicode-objects must be encoded before hashing

```
好，那就encoding。

```
def verify():
    print(request.GET)
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    echostr = request.GET.get('echostr')
    token = 'hello2019'
    list1 = [token, str(timestamp), str(nonce)]
    list1.sort()
    temp = (''.join(list1)).encode('utf-8')
    hashcode = hashlib.sha1(temp).hexdigest()
```
好，这次成功了。然后，token验证成功啦！🌹🌹🌹🌹🌹


### 2.2 接受用户输入  

不知道哪里来的小猪猪机器人。我现在输入了，就有小猪猪机器人回复我。

后台被关注回复写着这些：

> 你已授权给微商通、小猪cms、微盟、有赞、Hi现场帮助你运营公众号，点击管理已授权的第三方平台

以上全部取消授权后，关注就是纯关注了，不再有一大串自动回复。给它发消息，也不再有回复。

绕了一大圈，又去看服务器日志了，显示：  

```
10.39.123.35 - - [17/May/2019 16:47:40] "POST /wx?signature=25454995cc1b3d1f136cc441d9239ddd631d4729&timestamp=1558082859&nonce=2133759430&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM HTTP/1.1" 500 1646
AttributeError: module 'xml' has no attribute 'etree'
    root = xml.etree.ElementTree.fromstring(request.body.read())
  File "main.py", line 54, in parse_msg
    msg = parse_msg()
  File "main.py", line 63, in response_msg
    rv = callback(*a, **ka)
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 1740, in wrapper
    return route.call(**args)
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 862, in _handle
```
于是又去搜，这回又有个人跟我表现一样。

[Python import xml does not include xml.etree.ElementTree - Stack Overflow](https://stackoverflow.com/questions/40388061/python-import-xml-does-not-include-xml-etree-elementtree)

他说import不一定会把子模块也import进来。

改成了引用子模块。这次没有这个错误了，换了一个： 

```
KeyError: 'Content'
    if msg['Content'] != 'hi':
  File "main.py", line 72, in response_msg
    rv = callback(*a, **ka)
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 1740, in wrapper
    return route.call(**args)
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 862, in _handle
```
KeyError就是字典中没有content这个键。

比较了一下，发现这个键可能是xml中尖括号里的，于是赶紧改成一致的。然后发现其实是上面代码没盖好，变量名称message和msg前后不一致，所以msg是个空，当然什么键也没有了。这个错误也挺低挡的。刚才改变量名不应该手动改，应该用查找替换，就不会这样乌龙了。

现在没有错误了。不过表现还是如常。那就是没有及时回复的问题。可是到底怎么回复啊！

突然想起来程序中好几处print，我都不知道它们究竟是在哪里print的。发现是在正确日志里。小小增加了一个print，果然是这样。

那把验证时的各个字段都打出来吧。

```
@route('/wx')
def verify():
    print('ahcai')
    print('signature: ', request.GET.get('signature'))
    print('timestamp: ', request.GET.get('timestamp'))
    print('nonce: ', request.GET.get('nonce'))
    print('echostr: ', request.GET.get('echostr'))
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    echostr = request.GET.get('echostr')
    token = 'hello2019'
    list1 = [token, str(timestamp), str(nonce)]
    list1.sort()
    temp = (''.join(list1)).encode('utf-8')
    hashcode = hashlib.sha1(temp).hexdigest()
    print('handle/GET func: %s, %s' % (hashcode, signature))
    if hashcode == signature:
        return echostr
    else:
        return ''
```

发现正确日志是这样的：  

```
handle/GET func: 33363441261a8b01e5724ec27c8f732be6d9e72e, None
echostr:  None
nonce:  None
timestamp:  None
signature:  None
ahcai
```
好家伙！全是None。

以此类推，我也可以在msg那里设置print，看看会是什么。

看到了完整的msg。

```
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558086958', 'MsgType': 'text', 'Content': 'hi', 'MsgId': '22306442881577235'}
handle/GET func: 33363441261a8b01e5724ec27c8f732be6d9e72e, None
echostr:  None
nonce:  None
timestamp:  None
signature:  None
ahcai
```
再把echostr打印出来看看。

```
    </xml>
        <Content>Hi, I'm here.</Content>
        <timestamp>1558087285</timestamp>
        <ToUserName>gh_96828c21c75a</ToUserName>
        <FromUserName>oNUKYuMg4XfZueSsVOw74jh8zVVM</FromUserName>
    <xml>
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558087285', 'MsgType': 'text', 'Content': 'hi', 'MsgId': '22306448454771087'}
```

xml是echostr，字典是msg

可以看出来，echostr这里仍然是把公众号作为接收方、用户作为发送方的，其实应该反过来啊。
啊，会不会是应该把两个对调一下呀？

虽然没成功，但是看到了取消关注和关注的msg样子：  

```
    </xml>
        <Content>昨天</Content>
        <timestamp>1558088264</timestamp>
        <FromUserName>gh_96828c21c75a</FromUserName>
        <ToUserName>oNUKYuMg4XfZueSsVOw74jh8zVVM</ToUserName>
    <xml>
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558088264', 'MsgType': 'text', 'Content': '昨天', 'MsgId': '22306460488950562'}
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558088257', 'MsgType': 'event', 'Event': 'subscribe', 'EventKey': None}
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558088139', 'MsgType': 'event', 'Event': 'unsubscribe', 'EventKey': None}
```

回去看了一下例子，发现那个人也是双方对调的。


