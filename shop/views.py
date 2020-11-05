from django.shortcuts import render
from .models import *
def shop_item(request,item_slug):
    shp = True
    all_cats = Category.objects.all()
    item = Item.objects.get(name_slug=item_slug)
    return render(request, 'pages/item.html', locals())
def shop_cat(request,cat_slug):
    all_cats = Category.objects.all()
    shp = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'

    category = Category.objects.get(name_slug=cat_slug)
    all_items = Item.objects.filter(category=category)

    return render(request, 'pages/shop.html', locals())
def shop_subcat(request,cat_slug,subcat_slug):
    all_cats = Category.objects.all()
    shp = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    subcategory = SubCategory.objects.get(name_slug=subcat_slug)
    category = Category.objects.get(name_slug=cat_slug)
    all_items = Item.objects.filter(subcategory=subcategory)

    return render(request, 'pages/shop.html', locals())
