#!/usr/bin/env python
# _*_coding:utf-8_*_

# from django.http import HttpResponse
from django.shortcuts import render
import os
import sqlite3
import datetime
import time
from BabyGrowModel.models import BabyInfo, NoteRecord


def index(request):
    filename = './babygrow.db'
    context = {}
    if os.path.exists(filename):
        context['tips'] = u"宝宝：%s" % (readBaby()['name'])
        return render(request, 'index.html', context)
    else:
        context['name'] = "未设置"
        context['gender'] = "未设置"
        context['birthtime'] = "未设置"
        context['momemail'] = "未设置"
        context['tips'] = "请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。"
        return render(request, 'baby.html', context)


def baby(request):
    context = {}
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        context['birthtime'] = str(datetime.date(
            int(request.POST.get('year')),
            int(request.POST.get('month')),
            int(request.POST.get('date'))))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = str(time.strftime("%Y/%m/%d %H:%M:%S"))
        context['tips'] = "宝宝：%s" % context['name']
        baby = BabyInfo(name=context['name'],
                        gender=context['gender'],
                        birthtime=context['birthtime'],
                        momemail=context['momemail'],
                        settingtime=context['settingtime'])
        baby.save()
        return render(request, 'baby.html', context)
    else:
        context['name'] = readBaby()['name']
        context['tips'] = u"宝宝：%s" % (readBaby()['name'])
        context['gender'] = readBaby()['gender']
        context['birthtime'] = readBaby()['birthtime']
        context['momemail'] = readBaby()['momemail']
        return render(request, 'baby.html', context)


def saveinfo(request):
    context = {}
    filename = './babygrow.db'
    context['tips'] = u"宝宝：%s" % (readBaby()['name'])
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            settingtime = time.strftime('%Y/%m/%d %H:%M:%S')
            age = readBaby()['age']
            record = request.POST.get('newline')
            note = NoteRecord(time=settingtime,
                              age=age,
                              record=record)
            note.save()
        cursor.execute('''select * from BabyGrowModel_noterecord''')
        context['historylabel'] = cursor.fetchall()
    return render(request, 'history.html', context)


def validateEmail(email):
    import re
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return 1
    return 0


def history(request):
    context = {}
    filename = './babygrow.db'
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        cursor.execute('''select * from BabyGrowModel_noterecord''')
        context['historylabel'] = cursor.fetchall()
        return render(request, 'history.html', context)


def email(request):
    context = {}
    context['momemail'] = readBaby()['momemail']
    return render(request, 'email.html', context)


def camera(request):
    context = {}
    context['photoid'] = '3'
    context['photoname'] = ['2013-11-13, 0岁.jpg', '2015-11-13, 2岁.jpg', '2016-11-13, 3岁.jpg']
    return render(request, 'camera.html', context)


def readBaby():
    filename = './babygrow.db'
    if os.path.exists(filename):
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            sql1 = '''
                    select name from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                  '''
            cursor.execute(sql1)
            name = str(cursor.fetchall())[3:-4]
            sql2 = '''
                    select gender from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                  '''
            cursor.execute(sql2)
            gender = str(cursor.fetchall())[3:-4]
            sql3 = '''
                    select birthtime from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                    '''
            cursor.execute(sql3)
            birthtime = str(cursor.fetchall())
            birthdate = datetime.datetime(int(birthtime[3:7]),
                                          int(birthtime[8:10]),
                                          int(birthtime[11:13]))
            age = (datetime.datetime.now() - birthdate).days
            birthtime = birthtime[3:-4]
            sql4 = '''
                    select momemail from BabyGrowModel_babyinfo
                    order by settingtime desc
                    limit 0,1
                    '''
            cursor.execute(sql4)
            momEmail = str(cursor.fetchall())[3:-4]
            babyDict = dict(zip(
                ['name', 'gender', 'birthtime', 'age', 'momemail'],
                [name, gender, birthtime, age, momEmail]))
            return babyDict
