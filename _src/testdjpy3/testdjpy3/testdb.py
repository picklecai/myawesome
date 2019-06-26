#!/usr/bin/env python
# _*_coding:utf-8_*_

from django.http import HttpResponse
from TestModel.models import noterecord


def testdb(request):
    test1 = noterecord(time='2019-06-26', age='6', record='今天第一次')
    test1.save()
    return HttpResponse('<p>数据添加成功</p>')
