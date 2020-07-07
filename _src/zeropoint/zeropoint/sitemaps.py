from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from news.models import *
from solution.models import SoluArcs
from case.models import AnliArcs


class IndexSitemap(Sitemap):
    priority = 0.5
    changefreq = 'yearly'

    def items(self):
        return ['index', 'product', 'solution', 'case', 'news', 'about']

    def location(self, item):
        return '/' + item


class SoluSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return SoluArcs.objects.all()

    def location(sef, item):
        return '/solution-detail/' + str(item.id)


class CaseSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return AnliArcs.objects.all()

    def location(sef, item):
        return '/case-detail/' + str(item.id)


class CateSitemap(Sitemap):
    priority = 0.6
    changefreq = 'never'

    def items(self):
        return Category.objects.all()

    def location(sef, item):
        return '/category/' + str(item.id)


class PostSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(sef, item):
        return '/article-detail/' + str(item.id)


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['map']

    def location(self, item):
        return reverse(item)
