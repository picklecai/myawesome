#!/usr/bin/env python
# _*_coding:utf-8_*_

# from django.http import HttpResponse
from django.shortcuts import render
import os
import sqlite3
import datetime
import time


def index(request):
    # filename = './babyinfo.db'
    filename = './babyinfo.txt'
    context = {}
    if os.path.exists(filename):
        '''
        conn = sqlite3.connect('./babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select name from babyinfo order by settingtime desc limit 0,1')
        n = str(cursor.fetchall())
        name = n[4:-4].decode('unicode_escape')'''
        name = open(filename).readlines()[0]
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
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        context['birthtime'] = str(datetime.date(int(request.POST.get('year')), int(request.POST.get('month')), int(request.POST.get('date'))))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = time.strftime("%d/%m/%Y %H:%M:%S")
        context['tips'] = "宝宝：%s" % context['name']
    '''
    if (context['name'] or context['gender'] or context['birthtime'] or context['momemail']) is None or validateEmail('momemail') == 0:
        context['name'] = "重新设置"
        context['gender'] = "重新设置"
        context['birthtime'] = "重新设置"
        context['momemail'] = "重新设置"
        context['tips'] = "请重新设置宝宝信息及妈妈邮箱。"

    else:'''
    # data = context['name'].decode('utf-8'), context['gender'].decode('utf-8'), context['birthtime'], context['momemail'], context['settingtime']

    '''
    createbaby(data)
    readbaby()'''
    file = open('./babyinfo.txt', 'w')
    file.write(context['name'] + '\n')
    file.write(context['gender'] + '\n')
    file.write(context['birthtime'] + '\n')
    file.write(context['momemail'] + '\n')
    file.write(context['settingtime'] + '\n')
    file.close()
    return render(request, 'baby.html', context)


def saveinfo(request):
    context = {}
    name = open('./babyinfo.txt').readlines()[0]
    context['tips'] = u"宝宝：%s" % name
    with open('./babynote.txt', 'a') as file:
        if request.method == 'POST':
            content = request.POST.get('newline')
            settingtime = time.strftime("%d/%m/%Y %H:%M:%S")
            file.write(settingtime + '\n')
            file.write(content + '\n\n')
    if os.path.exists('babynote.txt'):
        with open('./babynote.txt', 'r') as file:
            context['historylabel'] = file.readlines()
            return render(request, 'history.html', context)
    else:
        if os.path.exists('babyinfo.txt'):
            context['historylabel'] = ['尚无宝宝记录，先去添加吧。']
            return render(request, 'history.html', context)
        else:
            context['name'] = "未设置"
            context['gender'] = "未设置"
            context['birthtime'] = "未设置"
            context['momemail'] = "未设置"
            context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
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
    if os.path.exists('babynote.txt'):
        with open('./babynote.txt', 'r') as file:
            context['historylabel'] = file.readlines()
            return render(request, 'history.html', context)
    else:
        if os.path.exists('babyinfo.txt'):
            context['historylabel'] = ['尚无宝宝记录，先去添加吧。']
            return render(request, 'history.html', context)
        else:
            context['name'] = "未设置"
            context['gender'] = "未设置"
            context['birthtime'] = "未设置"
            context['momemail'] = "未设置"
            context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
            return render(request, 'baby.html', context)


def baby(request):
    context = {}
    filename = './babyinfo.txt'
    if os.path.exists(filename):
        data = open(filename, 'r').readlines()
        context['tips'] = data[0]
        context['name'] = context['tips']
        context['gender'] = data[1]
        context['birthtime'] = data[2]
        context['momemail'] = data[3]
    else:
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
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
