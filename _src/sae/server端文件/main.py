# _*_coding:utf-8_*_
import time
import os
from bottle import run, route, post, template, request
import hashlib
import xml.etree.ElementTree


@route('/')
def index():
    return template('index', savetxt=False)


@post('/', method='POST')
def save():
    newline = request.forms.decode('utf-8').get('record')
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()
    return template('index', savetxt=True)


@route('/history')
def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
    else:
        notelist = []
    return template('history', history=notelist)


@route('/wx/index.html')
def verify():
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
    if hashcode != signature:
        return 'aha, no one.'
    else:
        return echostr
    # return template('wx', message='None.', echostr=echostr)


def parse_msg():
    root = xml.etree.ElementTree.fromstring(request.body.read())
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg


@post('/wx/index.html')
def response_msg():
    msg = parse_msg()
    subscribe = u'Hello，欢迎来到玩爆网站！我们想跟你聊聊网站的那点事儿。<a href="https://mp.weixin.qq.com/s/-CIzaHiD_1duR_Djf-qnwg">营销网站</a>'
    hi_msg = '你好！我在这里等你哦'
    copy_msg = '我会重复你的话： '
    textTpl = '''
    <xml>
      <ToUserName><![CDATA[%s]]></ToUserName>
      <FromUserName><![CDATA[%s]]></FromUserName>
      <CreateTime>%d</CreateTime>
      <MsgType><![CDATA[text]]></MsgType>
      <Content><![CDATA[%s]]></Content>
    </xml>'''
    if msg['MsgType'] == 'event':
        if msg['Event'] == 'subscribe':
            res_str = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 int(time.time()), subscribe)
            # return template('wx', message=msg['Event'], echostr=echostr)
            return res_str
    elif msg['MsgType'] == 'text':
        if msg['Content'] == 'hi':
            res_str = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 int(time.time()), hi_msg)
            # return template('wx', message=msg['Content'], echostr=echostr)
        else:
            res_str = textTpl % (msg['FromUserName'], msg['ToUserName'],
                                 int(time.time()), copy_msg + msg['Content'])
            # return 'success'  # return ''
        return res_str

if __name__ == '__main__':
    global HOST, PORT
    HOST = '0.0.0.0'
    PORT = 5050
    run(host=HOST, port=PORT, debug=True, reloader=True)
