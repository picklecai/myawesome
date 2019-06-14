#!/usr/bin/env python
# _*_coding:utf-8_*_

# from django.http import HttpResponse
from django.shortcuts import render
import os
import sqlite3
import datetime
import time


def hello(request):
    context = {}
    context['hello'] = '这是一个Django网站!'
    # return HttpResponse('Hello world!')
    return render(request, 'hello.html', context)


def index(request):
    filename = './babyinfo.db'
    context = {}
    if os.path.exists(filename):
        conn = sqlite3.connect('./babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select name from babyinfo order by settingtime desc limit 0,1')
        n = str(cursor.fetchall())
        name = n[4:-4].decode('unicode_escape')
        context['tips'] = u"宝宝：%s" % name
        return render(request, 'index.html', context)
    else:
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)


def savebaby(request):
    context = {}
    context['name'] = request.forms.get('name')
    context['gender'] = request.forms.get('gender')
    context['birthtime'] = datetime.date(int(request.forms.get('year')), int(request.forms.get('month')), int(request.forms.get('date')))
    context['momemail'] = request.forms.get('email')
    context['settingtime'] = time.strftime("%d/%m/%Y %H:%M:%S")
    if context['name']|context['gender']|context['birthtime']|context['momemail'] is None or validateEmail(momemail) == 0:
        context['name'] = "重新设置"
        context['gender'] = "重新设置"
        context['birthtime'] = "重新设置"
        context['momemail'] = "重新设置"
        context['tips'] = "请重新设置宝宝信息及妈妈邮箱。"
    else:
        data = context['name'].decode('utf-8'), context['gender'].decode('utf-8'), context['birthtime'], context['momemail'], context['settingtime']
        context['tips'] = "宝宝：%s" % name
        createbaby(data)
        readbaby()
    return render(request, 'baby.html', context)


def createbaby(data):
    conn = sqlite3.connect('./babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, momemail text, settingtime text)')
    cursor.execute('insert into babyinfo (name, gender, birthtime, momemail, settingtime) values (?,?,?,?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()


def readbaby():
    conn = sqlite3.connect('./babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, momemail text, settingtime text)')
    cursor.execute('select * from babyinfo')
    babyinfolist = cursor.fetchall()
    return babyinfolist


def validateEmail(email):
    import re
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return 1
    return 0


def history(request):
    context = {}
    context['tips'] = '大猫'
    context['historylabel'] = ['2019-06-02, 青蛙和小鱼', '2019-05-08, 最喜欢乌鸦喝水了', '2019-04-15, 今天5:40就醒啦']
    return render(request, 'history.html', context)


def baby(request):
    context = {}
    context['tips'] = readbaby['name']
    context['name'] = '大猫'
    context['gender'] = '男'
    context['birthtime'] = '2013-11-13'
    context['momemail'] = 'pickle.ahcai@163.com'
    return render(request, 'baby.html', context)




def email(request):
    context = {}
    context['momemail'] = 'pickle.ahcai@163.com'
    return render(request, 'email.html', context)


def camera(request):
    context = {}
    context['photoid'] = '3'
    context['photoname'] = ['2013-11-13, 0岁.jpg', '2015-11-13, 2岁.jpg', '2016-11-13, 3岁.jpg']
    return render(request, 'camera.html', context)
