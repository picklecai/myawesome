"""testdjpy3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import view
# from django.conf.urls import url
from django.urls import path

'''urlpatterns = [url(r'^$', view.hello), url(r'^index/$', view.hello),
               url(r'^hi/$', view.hello), ]'''
urlpatterns = [path('', view.index), path('history.html', view.history),
               path('email.html', view.email), path('baby.html', view.baby, name='check'),
               path('camera.html', view.camera), path('baby2.html', view.savebaby) ]
