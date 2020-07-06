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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
# from django.contrib.sitemaps import GenericSitemap
from . import view


sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include(('news.urls', 'news'), namespace='news')),
    path('case', include(('case.urls', 'case'), namespace='case')),
    path('solution', include(('solution.urls', 'solution'), namespace='solution')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', view.index, name='index'),
    url(r'^product$', view.product, name='product'),
    url(r'^about$', view.about, name='about'),
    url(r'^map.html$', view.map),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^favicon.ico$',
        RedirectView.as_view(url=r'static/images/favicon.ico')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
