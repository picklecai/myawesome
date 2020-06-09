"""zeropoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import view


urlpatterns = [
    path('admin/', admin.site.urls), path('news', include('news.urls')),
    url(r'^$', view.index), url(r'^product$', view.product),
    url(r'^solution$', view.solution), url(r'^case$', view.case),
    url(r'^about$', view.about),
    url(r'^map.html$', view.map),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/images/favicon.ico')),
]
