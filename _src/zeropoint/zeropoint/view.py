import time
import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    context['hello'] = 'Hello world!'
    # return HttpResponse("Hello world!")
    return render(request, 'index.html', context)


def clock(request):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    html = '<html><body>It is now: %s. </body></html>' % now
    return HttpResponse(html)


def timeAhead(request, offset):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    dt = dt.strftime('%Y-%m-%d %H:%M:%S')
    html = '''<html><body>
    It is now:</br> %s.</br></br>
    In <strong>%d</strong> hours, it\'ll be:</br> %s.
    </body></html>
    ''' % (now, offset, dt)
    return HttpResponse(html)
