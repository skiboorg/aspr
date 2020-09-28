from django.contrib import admin
from .models import *


class Block1ItemInline(admin.TabularInline):
    model = Block1Item
    extra = 0

class ManufactoryInline(admin.TabularInline):
    model = Manufactory
    extra = 0

class PartnerInline(admin.TabularInline):
    model = Partner
    extra = 0

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 0
class HomePageAdmin(admin.ModelAdmin):
    inlines = [Block1ItemInline,ManufactoryInline,PartnerInline,FeatureInline]
    class Meta:
        model = HomePage


class WorkTypeInline(admin.TabularInline):
    model = WorkType
    extra = 0

class WorkTypePageAdmin(admin.ModelAdmin):
    inlines = [WorkTypeInline]
    class Meta:
        model = WorkTypePage

admin.site.register(HomePage,HomePageAdmin)
admin.site.register(AvtomatizaciyaPage)
admin.site.register(ProizvodsvoPage)
admin.site.register(AboutPage)
admin.site.register(Project)
admin.site.register(WorkTypePage,WorkTypePageAdmin)
