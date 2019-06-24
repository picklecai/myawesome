#!/usr/bin/env python
# _*_coding:utf-8_*_

from django.http import HttpResponse
from django.shortcuts import render
import time
import datetime


def clock(request):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    # now = datetime.datetime.now()
    html = '<html><body>It is now: %s.</body></html>' % now
    return HttpResponse(html)


def timeAhead(request, offset):
    offset = int(offset)
    # time.strftime('%Y-%m-%d %H:%M:%S')
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %d hours, it\'ll be : %s.</body></html>' % (offset, dt)
    # assert False
    return HttpResponse(html)


def hello(request):
    context = {}
    context['hello'] = 'Hi everyone, this is Peter Two.'
    return render(request, 'hello.html', context)
