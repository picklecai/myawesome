#!/usr/bin/env python
# _*_coding:utf-8_*_

from django.shortcuts import render
import os
import sqlite3
from datetime import date
import time
# from BabyGrowModel.models import BabyInfo, NoteRecord

FILE_NAME = './babygrow.db'
UPLOAD_TIPS = '请上传您宝宝的基本信息，否则系统无法计算宝宝年龄。'


def index(request):
    context = {}
    if not os.path.exists(FILE_NAME) or readBaby()['name'] == '':
        context = initBaby()
        return render(request, 'baby.html', context)
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
        return render(request, 'index.html', context)


def baby(request):
    context = {}
    if not os.path.exists(FILE_NAME) or readBaby()['name'] == '':
        context['tips'] = UPLOAD_TIPS
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
    if request.method == 'POST':
        context['name'] = request.POST.get('name')
        context['gender'] = request.POST.get('gender')
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        day = int(request.POST.get('day'))
        context['birthtime'] = str(date(year, month, day))
        context['momemail'] = request.POST.get('email')
        context['settingtime'] = str(time.strftime("%Y/%m/%d %H:%M:%S"))
        ID = readBaby()['ID'] + 1
        data = (ID, context['name'], context['gender'], context['birthtime'],
                context['momemail'], context['settingtime'])
        createBaby(data)
        age = (date.today() - date(year, month, day)).days
        context['tips'] = '%s，今天%s天' % (context['name'], age)
        '''baby = BabyInfo(
            name=context['name'], gender=context['gender'],
            birthtime=context['birthtime'], momemail=context['momemail'],
            settingtime=context['settingtime'])
        baby.save()'''
        return render(request, 'baby.html', context)
    else:
        if not os.path.exists(FILE_NAME) or readBaby()['name'] == '':
            context = initBaby()
        else:
            context['name'] = readBaby()['name']
            context['tips'] = '%s，今天%s天' % (context['name'], readBaby()['age'])
            context['gender'] = readBaby()['gender']
            context['birthtime'] = readBaby()['birthtime']
            context['momemail'] = readBaby()['momemail']
        return render(request, 'baby.html', context)


def saveRecord(request):
    context = {}
    if not os.path.exists(FILE_NAME) or readBaby()['name'] == '':
        context = initBaby()
        return render(request, 'baby.html', context)
    else:
        if request.method == 'POST':
            if readRecord() != []:
                ID = readRecord()[0][0] + 1
            else:
                ID = 1
            settingtime = time.strftime('%Y/%m/%d %H:%M:%S')
            age = readBaby()['age']
            record = request.POST.get('newline')
            data = (ID, settingtime, age, record)
            createRecord(data)
            '''note = NoteRecord(time=settingtime, age=age, record=record)
            note.save()'''
            context['tips'] = '%s，今天%s天' % (readBaby()['name'], age)
            context['historylabel'] = readRecord()
            return render(request, 'history.html', context)
        elif not os.path.exists(FILE_NAME) or readRecord() == []:
            context['tips'] = '%s，今天%s天 \n尚无记录，赶快添加吧！' % (
                readBaby()['name'], readBaby()['age'])
            return render(request, 'index.html', context)
        else:
            context['tips'] = '%s，今天%s天' % (
                readBaby()['name'], readBaby()['age'])
            context['historylabel'] = readRecord()
            return render(request, 'history.html', context)


def validateEmail(email):
    import re
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return 1
    return 0


def email(request):
    context = {}
    if not os.path.exists(FILE_NAME) or readBaby()['name'] == '':
        context = initBaby()
        return render(request, 'baby.html', context)
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
        context['momemail'] = readBaby()['momemail']
        return render(request, 'email.html', context)


def camera(request):
    context = {}
    if not os.path.exists(FILE_NAME) or readBaby()['name'] == '':
        context = initBaby()
        return render(request, 'baby.html', context)
    else:
        context['tips'] = '%s，今天%s天' % (readBaby()['name'], readBaby()['age'])
        context['photoid'] = len(readRecord())
        context['photoname'] = readBaby()
        return render(request, 'camera.html', context)


def createBaby(data):
    with sqlite3.connect(FILE_NAME) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists babyinfo (
        ID num, name text, gender text,
        birthtime text, momemail text,
        settingtime text
        )'''
        cursor.execute(sql1)
        sql2 = '''
        insert into babyinfo (
        ID, name, gender, birthtime, momemail, settingtime)
        values (?,?,?,?,?,?) '''
        cursor.execute(sql2, data)


def createRecord(data):
    with sqlite3.connect(FILE_NAME) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists noterecord (
        ID num, time text, age text, record text
        )'''
        cursor.execute(sql1)
        sql2 = '''
        insert into noterecord (
        ID, time, age, record)
        values (?,?,?,?) '''
        cursor.execute(sql2, data)


def readBaby():
    with sqlite3.connect(FILE_NAME) as conn:
        cursor = conn.cursor()
        sql1 = '''
        create table if not exists babyinfo (
        ID num, name text, gender text, birthtime text, momemail text,
        settingtime text)'''
        cursor.execute(sql1)
        sql = '''select * from babyinfo order by settingtime desc'''
        cursor.execute(sql)
        babyList = cursor.fetchall()
        if babyList != []:
            ID, name = babyList[0][0], str(babyList[0][1])
            gender, birthtime = str(babyList[0][2]), str(babyList[0][3])
            birthdate = date(
                int(birthtime[0:4]), int(birthtime[5:7]), int(birthtime[8:10]))
            age = (date.today() - birthdate).days
            momEmail = str(babyList[0][4])
        else:
            ID = 0
            name = gender = birthtime = age = momEmail = ''
        babyDict = dict(zip(
            ['ID', 'name', 'gender', 'birthtime', 'age', 'momemail'],
            [ID, name, gender, birthtime, age, momEmail]))
        return babyDict


def readRecord():
    with sqlite3.connect(FILE_NAME) as conn:
        cursor = conn.cursor()
        sql1 = '''create table if not exists noterecord (ID num, time text,
        age text, record text)'''
        cursor.execute(sql1)
        sql = '''select * from noterecord order by time desc'''
        cursor.execute(sql)
        historylabel = cursor.fetchall()
        return historylabel


def initBaby():
    context = {}
    context['name'] = context['gender'] = "未设置"
    context['birthtime'] = context['momemail'] = "未设置"
    context['tips'] = UPLOAD_TIPS
    return context
