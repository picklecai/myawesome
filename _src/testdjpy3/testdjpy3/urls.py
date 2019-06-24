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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
# from django.urls import path


urlpatterns = [url(r'^$', view.index),
               url(r'^history.html/$', view.saveinfo, name='info'),
               url(r'^email.html/$', view.email),
               url(r'^camera.html/$', view.camera),
               url(r'^baby.html/$', view.baby, name='check'),
               url(r'^baby2.html/$', view.savebaby, name='check'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''urlpatterns = [path('', view.index), path('history.html', view.saveinfo, name='info'),
               path('email.html', view.email), path('baby.html', view.baby, name='check'),
               path('camera.html', view.camera), path('baby2.html', view.savebaby, name='check')
               ]'''
# path('/static/main.css', serve, {'document_root':settings.STATIC_ROOT})
