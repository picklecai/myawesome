# 微信后台开发笔记 

暂存一个聊天机器人：[项目简介 - itchat](https://itchat.readthedocs.io/zh/latest/)

暂存：[一堆微信开发相关的 python 库（不定期更新） - 后端 - 掘金](https://juejin.im/entry/58d7ac4d44d904006876039f)

**重点文档**：[微信公众平台](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1472017492_58YV5)——开发者指引，使用人话的开发文档

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

这里的错误在于没有用as：  

```
@post('/wx/index.html')
def response_msg():
    try:
        msg = parse_msg()
        print(msg)
        textTpl = '''
        <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]</MsgType>
            <Content><![CDATA[%s]]></Content>
        </xml>'''
        if msg['MsgType'] == 'event':
            if msg['Event'] == 'subscribe':
                echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                     str(int(time.time())), "Wait you.")
                print(echostr)
                # return template('wx', message=msg['Event'], echostr=echostr)
                return echostr
        elif msg['MsgType'] == 'text':
            if msg['Content'] == 'hi':
                echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                     str(int(time.time())), "Hi, I'm here.")
                print(echostr)
                # return template('wx', message=msg['Content'], echostr=echostr)
                return echostr
            else:
                echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                     str(int(time.time())), msg['Content'])
                # return 'success'
                return ''
    except Exception as Argument:
        print(Argument)
```

备注于此，其实由于上面的没有出错，下面的也就没用了。

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

#### 2.2.1 措施1:取消其他授权

不知道哪里来的小猪猪机器人。我现在输入了，就有小猪猪机器人回复我。

后台被关注回复写着这些：

> 你已授权给微商通、小猪cms、微盟、有赞、Hi现场帮助你运营公众号，点击管理已授权的第三方平台

以上全部取消授权后，关注就是纯关注了，不再有一大串自动回复。给它发消息，也不再有回复。

#### 2.2.2 措施2:对xml引入子模块

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

#### 2.2.3 措施3: 纠正字典里没有键‘Content’的问题：msg和message混用，xml书写不规范

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

比较了一下，发现这个键可能是xml中尖括号里的，于是赶紧改成一致的。然后发现其实是上面代码没改好，变量名称message和msg前后不一致，所以msg是个空，当然什么键也没有了。这个错误也挺低档的。刚才改变量名不应该手动改，应该用查找替换，就不会这样乌龙了。

现在没有错误了。不过表现还是如常。那就是没有及时回复的问题。可是到底怎么回复啊！

#### 2.2.4 发现1: 发现了main中的print是在服务器的正确日志里

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

#### 2.2.5 发现2: 完整的msg长啥样

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
#### 2.2.6 发现3:  xml格式里接收方和发送方写反了

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

#### 2.2.7 发现4: 取消关注和新关注的msg字段 

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

#### 2.2.8 措施4: 启用微信开发的报警群  

[用python快速实现微信公众号开发 - IT程序猿](https://www.itcodemonkey.com/article/4045.html)

框架不一样，不过他启用了报警群。我也用了，却没有收到消息。

#### 2.2.9 措施5: 在地址上新增了`/index.html`，以预防302重定向引发的接收不到  

["该公众号提供的服务出现故障，请稍后再试"，sh*t！ - 多重阅读 - CSDN博客](https://blog.csdn.net/henryhu712/article/details/84308570)

[Python进行微信公众号开发 - 知乎](https://zhuanlan.zhihu.com/p/37229184)

按照他说的，地址改成了加上/index.html的，刚刚改完时，日志出现这样的打印：  

```
handle/GET func: 6882dbd945a107bb12c78bc80d0f0dc5bb8e66dd, 6882dbd945a107bb12c78bc80d0f0dc5bb8e66dd
<bottle.FormsDict object at 0x7f469d647e80>
```
#### 2.2.10 发现5: 发现了只有更改了服务器配置时才进行token验证，和signature进行比较的值才不是none 

这是token验证比较，终于出现了不是none的，一度让我以为解决了。于是取关再关注，没想到还是老样子。

原来这个只有更改服务器配置时才会一样——因为只有这个时候会进行token验证。所以平常看到时none也是正常的，毕竟其他时候不做token验证。好吧，虽然问题如故，但是又理解了一个问题。

[解决：该公众号提供的服务出现故障，请稍后重试 - 分享传递价值 - CSDN博客](https://blog.csdn.net/fanrenxiang/article/details/80877600)

#### 2.2.11 措施6: 把xml中的timestamp字段也改成微信开发文档中规定的格式 

这里列了三种原因，不过我除了第二个已经改了之外，另外两种没有犯。不对，我还是把timestamp老老实实改成CreateTime看看吧。改完依旧。

[微信公众号提示错误:该公众号提供的服务出现故障,请稍后再试 - wqhjfree的专栏 - CSDN博客](https://blog.csdn.net/wqhjfree/article/details/80341001)

#### 2.2.12 措施7:  使用微信公众平台接口调试工具查看反馈结果

这个人提到的测试，我的结果也是200代码加connection close：

[微信公众平台接口调试工具](https://mp.weixin.qq.com/debug/cgi-bin/apiinfo?t=index&type=%E8%87%AA%E5%AE%9A%E4%B9%89%E8%8F%9C%E5%8D%95&form=%E8%87%AA%E5%AE%9A%E4%B9%89%E8%8F%9C%E5%8D%95%E5%88%9B%E5%BB%BA%E6%8E%A5%E5%8F%A3%20/menu/creat)

```
请求地址：
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxd8458c871909405b&secret=90de02dc19c040437deee9c16cd5d645
返回结果:
		200 OK
		Connection: close
		Date: Sat, 18-May-2019 17:05:19 GMT
		Content-Type: application/json; encoding=utf-8
		Content-Length: 46
		{
		    "errcode": -1000, 
		    "errmsg": "system error"
		}
		 
提示:
未知返回状态.

```

#### 2.2.13 措施8: 观察`list(request.forms.keys())[0]`和msg是否相同

在`print(msg)`时增加一个`print(list(request.forms.keys())[0])`，看看它们是否相同。来源仍然是[wechat_auto_reply · YixuanFranco/BookGiver Wiki](https://github.com/YixuanFranco/BookGiver/wiki/wechat_auto_reply)。

发现request这句，果然输出的是xml格式：  

```
</xml>
<MsgId>22309731789068337</MsgId>
<Content><![CDATA[hi]]></Content>
<MsgType><![CDATA[text]]></MsgType>
<CreateTime>1558316783</CreateTime>
<FromUserName><![CDATA[oNUKYuMg4XfZueSsVOw74jh8zVVM]]></FromUserName>
<xml><ToUserName><![CDATA[gh_96828c21c75a]]></ToUserName>
```
而msg则是字典样子： 
 
```
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558316783', 'MsgType': 'text', 'Content': 'hi', 'MsgId': '22309731789068337'}
```
#### 2.2.14 发现6: msg_parse是怎么提炼出msg各项参数的

想想把`request.body.read()`也打印出来看看，

```
b'<xml><ToUserName><![CDATA[gh_96828c21c75a]]></ToUserName>\n<FromUserName><![CDATA[oNUKYuMg4XfZueSsVOw74jh8zVVM]]></FromUserName>\n<CreateTime>1558318370</CreateTime>\n<MsgType><![CDATA[text]]></MsgType>\n<Content><![CDATA[hi]]></Content>\n<MsgId>22309756407214631</MsgId>\n</xml>'
```
和上面的区别是：它是二进制数据。其他都一样。怪不得回复数据要按照这个来写，原来确实是这样的。所以所谓接口数据，就是把内部的格式告诉开发者，让开发者不必去print就知道应该怎么写吧。

这样也就知道了函数parse_msg究竟做了什么，就是把这个二进制xml数据转换为字典数据。转换目的就是为了写回复信息时容易一些。

#### 2.2.15 发现7: 新关注时，后台也不打印echostr 

新关注时，不仅微信界面不会回复消息，程序也不打印echostr。虽然程序里写着如果msgtype是event的话就打印。这还不如用户发消息时——那会儿起码程序是打印echostr的。
```
def response_msg():
    msg = parse_msg()
    print(msg)
    textTpl = '''
    <xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[text]]</MsgType>
        <Content><![CDATA[%s]]></Content>
    </xml>
    '''
    if msg['MsgType'] == 'event':
        echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                             str(int(time.time())), "Wait you.")
    if msg['Content'] == 'hi':
        echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                             str(int(time.time())), "Hi, I'm here.")
    else:
        echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                             str(int(time.time())), msg['Content'])
    print(echostr)
    return template('wx', message=msg['Content'], echostr=echostr)
```

#### 2.2.16 措施9: return更改

想了想会不会是return的问题造成公众号不回复呢？于是把复杂的`return template('wx', message=msg['Content'], echostr=echostr)
`改成了简单一句`return echostr`。 

还是无法回复。上一条的问题依旧存在。三个if子句中，event那个就是不执行，其他两个都可以执行，后台都能打印出echostr来。

#### 2.2.17 措施10: 彻底解决content的keyerror和后台不打印echostr两个问题  

仔细研究关注时的msg突然发现，这时候msg是没有Content字段的，是否因为这个原因，所以时不时冒出Content的KeyError呢？于是把三个if语句改成这样：  

```
    if msg['MsgType'] == 'event' and msg['Event'] == 'subscribe':
        echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                             str(int(time.time())), "Wait you.")
        print(echostr)
        return template('wx', message=msg['Event'], echostr=echostr)
    else:
        if msg['Content'] == 'hi':
            echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 str(int(time.time())), "Hi, I'm here.")
        else:
            echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 str(int(time.time())), msg['Content'])
        print(echostr)
        return template('wx', message=msg['Content'], echostr=echostr)
```

结果发现2.2.15的问题被解决了，后台打印出了echostr的消息。  

但是content的KeyError并没有解决。突然想起来这个后台是倒过来打印的，调整一下顺序：

```
Traceback (most recent call last):

    if msg['Content'] == 'hi':
  File "main.py", line 81, in response_msg
    rv = callback(*a, **ka)
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 1740, in wrapper
    return route.call(**args)
  File "/app/.heroku/python/lib/python3.7/site-packages/bottle.py", line 862, in _handle
  
KeyError: 'Content'

10.39.123.35 - - [20/May/2019 11:04:51] "POST /wx/index.html?signature=7a9b2b555f5891765ad27ebcf2e4093ec6514121&timestamp=1558321490&nonce=1110266778&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM HTTP/1.1" 500 1471

172.16.100.22 - - [20/May/2019 11:04:59] "POST /wx/index.html?signature=ddf14f99d4b94ece244314238054bbf560f706c9&timestamp=1558321499&nonce=1284734740&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM HTTP/1.1" 200 438

10.39.123.35 - - [20/May/2019 11:05:05] "POST /wx/index.html?signature=4898a0086372bf46ec44da092a088da80809e3f7&timestamp=1558321505&nonce=1802548906&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM HTTP/1.1" 200 440

10.39.123.35 - - [20/May/2019 11:05:10] "POST /wx/index.html?signature=c4c51766f1b6a85be8343294ef7f4333c3c185da&timestamp=1558321510&nonce=427371664&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM HTTP/1.1" 200 432
```
对应4个动作：取消关注，关注，输入hi，输入其他消息。 

KeyError的消息，总是出现在取消关注时。可能是只交代了订阅时如何，没有交代取消订阅时如何，所以还会这样。继续改成这样：  

```
if msg['MsgType'] == 'event':
        echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                             str(int(time.time())), "Wait you.")
        print(echostr)
        return template('wx', message=msg['Event'], echostr=echostr)
elif msg['MsgType'] == 'text':
        if msg['Content'] == 'hi':
            echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 str(int(time.time())), "Hi, I'm here.")
        else:
            echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 str(int(time.time())), msg['Content'])
        print(echostr)
        return template('wx', message=msg['Content'], echostr=echostr)
```
显式地写出来究竟是event还是text。

果然取消订阅不再出现KeyError错误。

#### 2.2.18 发现8: token验证时的echostr长啥样

不知道为什么怀疑是消息没有加密，于是到后台去改成消息加密模式，没想到要先写加密解密代码才可以。于是放弃了。但是在这之前，想看看token验证时的echostr长啥样。于是打印了一下，果然看到了，是一串数字：  
```
handle/GET func: 33363441261a8b01e5724ec27c8f732be6d9e72e, None
None
handle/GET func: b76e1932949791b57f2a216bc27f64c5018bded3, b76e1932949791b57f2a216bc27f64c5018bded3
3095672099620486843
handle/GET func: 33363441261a8b01e5724ec27c8f732be6d9e72e, None
None
handle/GET func: 2c9e1b31cca444d9ee7899f57f10bdfc94143ba6, 2c9e1b31cca444d9ee7899f57f10bdfc94143ba6
6378132883159805415
handle/GET func: 404c8dac8845e416a04edc6e985b0b4f0b85e0ef, 404c8dac8845e416a04edc6e985b0b4f0b85e0ef
6988369138036505087
```

#### 2.2.19 发现9: 想自动回复消息必须消息加密

为什么觉得应该加密呢？

引用一下开发文档的这几个地方，看看是不是我理解问题：  

[微信公众平台](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140453)——接收普通消息

> 2、微信服务器在五秒内收不到响应会断掉连接，并且重新发起请求，总共重试三次。假如服务器无法保证在五秒内处理并回复，可以直接回复空串，微信服务器不会对此作任何处理，并且不会发起重试。详情请见“发送消息-被动回复消息”。  
> 3、如果**开发者需要对用户消息在5秒内立即做出回应**，即使用“发送消息-被动回复消息”接口向用户被动回复消息时，可以**在公众平台官网的开发者中心处设置消息加密**。开启加密后，用户发来的消息和开发者回复的消息都会被加密（但开发者通过客服接口等API调用形式向用户发送消息，则不受影响）。

[微信公众平台](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140543)——被动回复用户消息

> 如果开发者希望增强安全性，**可以**在开发者中心处开启消息加密，这样，用户发给公众号的消息以及公众号被动回复用户消息都会继续加密

[资源中心 - 微信开放平台](https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1419318479&token=&lang=zh_CN)——消息加解密接入指引

> 开发者在代替授权公众号接收和处理消息时，出于安全考虑，**必须**对消息收发的过程**进行必须的加解密**。  
> 首先请注意，开发者在接收消息和事件时，都需要进行消息加解密（某些事件可能需要回复，回复时也需要先进行加密）。但是，通过API主动调用接口（包括调用客服消息接口发消息）时，不需要进行加密。


[微信开放平台——消息加解密说明](https://mp.weixin.qq.com/wiki?action=doc&id=mp1434696670&t=0.569081929512322)

> 公众号消息加解密是公众平台为了进一步加强公众号安全保障，提供的新机制。开发者需注意，公众账号主动调用API的情况将不受影响。只有被动回复用户的消息时，才需要进行消息加解密。消息加解密的具体修改包括：  
> 
	> 1.新增消息体签名验证，用于公众平台和公众账号验证消息体的正确性   
	> 2.针对推送给微信公众账号的普通消息和事件消息，以及推送给设备公众账号的设备消息进行加密  
	> 3.公众账号对密文消息的回复也要求加密


#### 2.2.20 措施11:去掉函数response_msg的返回

想验证一下开发者指引中这段话：  

> 查询官方wiki 开头强调： 假如服务器无法保证在五秒内处理回复，则必须回复“success”或者“”（空串），否则微信后台会发起三次重试。  
> 解释一下为何有这么奇怪的规定。发起重试是微信后台为了尽可以保证粉丝发送的内容开发者均可以收到。如果开发者不进行回复，微信后台没办法确认开发者已收到消息，只好重试。  
> 真的是这样子吗？尝试一下收到消息后，不做任何回复。在日志中查看到微信后台发起了三次重试操作，  

于是去掉了return语句，只保留print语句。

然后，我再给公众号发消息，就没有‘该公众号暂时无法提供服务’这样的提示语了。随便我发什么，反正也不回应。上面这段话中的发起三次重试并没有看到。服务端日志并没有什么异样，让它打印的依旧打印。

#### 2.2.21 插曲：意外的token

刚才试图把后台设置为安全模式未遂后，一直到现在，改服务器设置都是token验证失败。试了好多次，放弃，还是把程序改为原来的地址和token吧。

#### 2.2.22 措施12: 回复success

按照开发者指引中的程序，硬性加上了`return 'success'`.

```
        if msg['Content'] == 'hi':
            echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 str(int(time.time())), "Hi, I'm here.")
            print(echostr)
            return template('wx', message=msg['Content'], echostr=echostr)
        else:
            echostr = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 str(int(time.time())), msg['Content'])
            return 'success'
```
现在，给公众号发送除了hi之外的消息，都能不出现‘该公众号暂时无法提供服务’了🌹🌹🌹。发送hi依旧如故。

后台日志还是老样子，只有我让它打印的那几个。网页上还是只有不验证token的那个none状态，没有其他消息。它根本没有像在网页上操作一样会自动跳转。如果刷新，那还是调用的get，不是post。

所以到目前为止，不出现‘该公众号暂时无法提供服务’有两种情况：  

- 不return
- `return 'success'`

这是说明在return的过程中丢了连接吗？

#### 2.2.23 措施13:重新写xml

怀疑是xml的书写出现问题，试了如下两种：  

```
    textTpl = '''<xml>
		<ToUserName><![CDATA[%s]]></ToUserName>
		<FromUserName><![CDATA[%s]]></FromUserName>
		<CreateTime>%s</CreateTime>
		<MsgType><![CDATA[text]]</MsgType>
		<Content><![CDATA[%s]]></Content>
	</xml>
'''
```
以及全部顶格：
```
    textTpl = '''<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]</MsgType>
<Content><![CDATA[%s]]></Content>
</xml>'''
```
这两种写法，都能通过python语法，但是无非是后台打印效果不一样，照旧‘该公众号暂时无法提供服务’

```
</xml>
<Content><![CDATA[Hi, I'm here.]]></Content>
<MsgType><![CDATA[text]]</MsgType>
<CreateTime>1558345296</CreateTime>
<FromUserName><![CDATA[gh_96828c21c75a]]></FromUserName>
<ToUserName><![CDATA[oNUKYuMg4XfZueSsVOw74jh8zVVM]]></ToUserName>
<xml>
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558345295', 'MsgType': 'text', 'Content': 'hi', 'MsgId': '22310141390324971'}
    </xml>
    <Content><![CDATA[Hi, I'm here.]]></Content>
    <MsgType><![CDATA[text]]</MsgType>
    <CreateTime>1558345101</CreateTime>
    <FromUserName><![CDATA[gh_96828c21c75a]]></FromUserName>
    <ToUserName><![CDATA[oNUKYuMg4XfZueSsVOw74jh8zVVM]]></ToUserName>
<xml>
```

别人写的，也没有全部顶格到最前面。所以可能问题不在这里。

#### 2.2.24 措施14: 改`return + 文本`

突然想知道如果直接 `return + 文本` 会怎么样。

于是把`return 'success'`直接简单粗暴地改成`return 'haole'`

这个还是有问题的。现在发送除了hi之外的其他消息也要‘不提供服务’了。

把success改成空字符就没事了。所以官方认定，除了success和空字符，其他一律妖艳贱货。。。。。

增加，到目前为止，不出现‘该公众号暂时无法提供服务’有两种情况：  

- 不return
- `return 'success'` or `return ''`

反正还是用了xml的就不行。

#### 2.2.25 发现10: 看到了平常发消息时的网页了

昏昏沉沉一上午，突然灵光一闪，错误信息里的网址大概是post后的吧。

于是弄来一个贴了看看，果然看到页面内容变了。

一般情况，网址为（https://pickle.applinzi.com/wx/index.html）,  
页面内容为：

```
receive: None.
Response: aha, no one.

```


抓了一个`return 'Hi, I'm here.'`的网址（时间和print消息对上号），贴过来一看，response为None。

网址为（https://pickle.applinzi.com/wx/index.html?signature=2cf4c3891de3325fc75da964c10960424ce4fff0&timestamp=1558406632&nonce=283907092&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM）,  
页面内容为：

```
receive: None.
Response: None

```

想起来这是template还被关在注释里呢，赶紧把它放出来。

现在网址为（https://pickle.applinzi.com/wx/index.html?signature=b08cad722cab4d138450123d922b009a8bd2b777&timestamp=1558407220&nonce=150393399&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM），  
页面内容仍然是：  

```
receive: None.
Response: None

```
好像不应该返回页面，还是应该返回echostr。把包括验证在内的所有返回都改成了echostr，再打开发送hi之后的网址（https://pickle.applinzi.com/wx/index.html?signature=0a8b5c2da18608eee0f353653465b1c41cd2959f&timestamp=1558407837&nonce=1432694926&openid=oNUKYuMg4XfZueSsVOw74jh8zVVM），  

页面内容为空。什么都没有。这正是None的含义。

echostr在后台是打印得出来的，却不能返回给网页/用户。


#### 2.2.26 发现11: 报警群的消息  

报警群两天来发了4次消息，有一次是服务关闭。那是因为我在升级的过程中去发送消息了。还有的连尖括号都是其他符号。现在仔细核对了一下，发现每次消息都是一样的内容：  

> 内容： 微信服务器向公众号推送消息或事件后得到的回应不合法
> 次数：5分钟3次（或2次）
> 错误样例：……

错误样例每每不同。但是上面的汉字内容都是一样。这说明问题还是出在回复消息的写法上？

这里[微信公众平台](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747358)有报警指引。

> 5.回应失败  
> 开发者没有按照wiki中的回复消息格式进行回复消息，或者发生网络错误，会报警回应失败，报警消息会提供第一次出现请求回应失败的时间，开发者的IP，消息类型以及回应的消息内容，请开发者确认：  
> 
	> a）该IP是否有误
	> b）该IP是否发生网络错误
	> c）该业务处理逻辑是否没有按照wiki规范回复消息，或是进入了异常逻辑。

#### 2.2.27 发现12: hashcode&signature突然一致了

这几次发送消息仍然没有回复，但是突然发现正确日志里，hashcode和signature居然一致了。为什么不再none了呢？是每次通信都验证token了吗？

```
    </xml>
        <Content><![CDATA[Hi, I'm here.]]></Content>
        <MsgType><![CDATA[text]]</MsgType>
        <CreateTime>1558416778</CreateTime>
        <FromUserName><![CDATA[gh_96828c21c75a]]></FromUserName>
        <ToUserName><![CDATA[oNUKYuMg4XfZueSsVOw74jh8zVVM]]></ToUserName>
    <xml>
{'ToUserName': 'gh_96828c21c75a', 'FromUserName': 'oNUKYuMg4XfZueSsVOw74jh8zVVM', 'CreateTime': '1558416777', 'MsgType': 'text', 'Content': 'hi', 'MsgId': '22311164414801853'}
handle/GET func: 756d02281d5ce539efe146a7fe2f7de1655e877f, 756d02281d5ce539efe146a7fe2f7de1655e877f
```

明白了，只是因为我把post后的地址拿出来直接访问了。这个地址是发送消息的过程中产生的，那会儿发生了交互。如果不做这个动作，就不会打印这句了。空欢喜一场。

#### 2.2.28 措施15: createtime改成整型

突然发现接收消息里，CreateTime写着整形，赶紧改成整型。

```
    textTpl = '''
    <xml>
      <ToUserName><![CDATA[%s]]></ToUserName>
      <FromUserName><![CDATA[%s]]></FromUserName>
      <CreateTime>%d</CreateTime>
      <MsgType><![CDATA[text]]</MsgType>
      <Content><![CDATA[%s]]></Content>
    </xml>'''
    if msg['MsgType'] == 'event':
        if msg['Event'] == 'subscribe':
            res_str = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 int(time.time()), "Wait you.")
            print(res_str)
            # return template('wx', message=msg['Event'], echostr=echostr)
            return res_str
    elif msg['MsgType'] == 'text':
        if msg['Content'] == 'hi':
            res_str = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 int(time.time()), "Hi, I'm here.")
            print(res_str)
            # return template('wx', message=msg['Content'], echostr=echostr)
            return res_str
```
结果还是不行，而且报警群又报警了。
```
Appid: wxd8458c871909405b
昵称: 玩爆网站
时间: 2019-05-21 14:22:19
内容: 微信服务器向公众号推送消息或事件后，得到的回应不合法
次数: 5分钟 2次
错误样例: [OpenID=oNUKYuMg4XfZueSsVOw74jh8zVVM][Stamp=1558419739][3rdUrl=http://pickle.applinzi.com/wx/index.html][Msg=Text][ip=220.181.136.186][response_length=285][response_content=<xml>
      <ToUserName><![CDATA[oNUKYuMg4XfZueSsVOw74jh8zVVM]]></ToUserName>
      <FromUserName><![CDATA[gh_96828c21c75a]]></FromUserName>
      <CreateTime>1558419739</CreateTime>
      <MsgType><![CDATA[text]]</MsgType>
      <Content><![CDATA[Hi, I'm here.]]></Content>
    </xml>]
报警排查指引，请见: http://url.cn/ab0jnP
```

#### 2.2.29 发现13: 为什么要写CDATA  

[微信公众平台编程](http://www.dwenzhao.cn/profession/netbuild/weixin.html)

> 4）文本内容规则：  
> 
> 在XML中，一些字符拥有特殊含义，如“<”和“>”，如果在XML文档的文本内容中用到就会发生错误，这时需要使用转义字符，“<”使用“<”，“>”使用“>”，其他还有“&”使用“&”，单引号使用“'”，双引号使用“"”。转义字符都为小写字符。   
>     但某些文本中会包含大量特殊字符，逐个转义比较麻烦，这时可以定义为CDATA区段。CDATA区段中的所有内容都会被XML解析器忽略，区段由“<![CDATA[”开始，由“]]>”结束。当然，CDATA部分的内容不能包含字符串“]]>”。


#### 2.2.30 发现14: text后面少了右尖括号  

故意连续输了6次hi，指望触发警报。过了几分钟，果然收到警报了。和刚才那个页面的逐字逐句比较，发现MsgType的text]]后面少了‘>’，赶紧补上。。。。。

哭了，果然是这个错误。现在试了，成功了！！！！！🌹🌹🌹🌹🌹🌹🌹


