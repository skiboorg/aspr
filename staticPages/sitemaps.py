from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *
from shop.models import Item

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['index','avtomatizaciya','proizvodstvo','projects','napravleniya','about']

    def location(self, item):
        return reverse(item)


class ProizvodstvoSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return Manufactory.objects.all()


class ItemsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return Item.objects.all()

    def lastmod(self, obj):
        return obj.created_at

