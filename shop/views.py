from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def shop_item(request,item_slug):
    shp = True
    all_cats = Category.objects.all()
    item = Item.objects.get(name_slug=item_slug)
    return render(request, 'pages/item.html', locals())
def shop_cat(request,cat_slug):
    page = request.GET.get('page')
    all_cats = Category.objects.all()
    shp = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'

    category = Category.objects.get(name_slug=cat_slug)
    items = Item.objects.filter(category=category)
    items_paginator = Paginator(items, 12)
    try:
        all_items = items_paginator.get_page(page)
    except PageNotAnInteger:
        all_items = items_paginator.page(1)
    except EmptyPage:
        all_items = items_paginator.page(items_paginator.num_pages)
    return render(request, 'pages/shop.html', locals())

def shop_subcat(request,cat_slug,subcat_slug):
    page = request.GET.get('page')
    all_cats = Category.objects.all()
    shp = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    subcategory = SubCategory.objects.get(name_slug=subcat_slug)
    category = Category.objects.get(name_slug=cat_slug)
    items = Item.objects.filter(subcategory=subcategory)
    items_paginator = Paginator(items, 12)
    try:
        all_items = items_paginator.get_page(page)
    except PageNotAnInteger:
        all_items = items_paginator.page(1)
    except EmptyPage:
        all_items = items_paginator.page(items_paginator.num_pages)
    return render(request, 'pages/shop.html', locals())
