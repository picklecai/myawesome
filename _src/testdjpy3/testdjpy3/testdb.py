#!/usr/bin/env python
# _*_coding:utf-8_*_

from django.http import HttpResponse
from TestModel.models import BabyInfo  # NoteRecord,


def testdb(request):
    # test1 = NoteRecord(time='2019-06-26', age='6', record='今天第一次')
    test2 = BabyInfo(name='damao', gender='男', birthtime='2013-11-13')
    # momemail='pickle.ahcai@163.com', settingtime='2019-06-27')
    # test1.save()
    test2.save()
    return HttpResponse('<p>数据添加成功</p>')
