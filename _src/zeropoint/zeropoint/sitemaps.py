from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['index', 'product', 'about']

    def location(self, item):
        return reverse(item)
