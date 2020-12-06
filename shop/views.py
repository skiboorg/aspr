from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def shop_item(request,item_slug):
    shp = True
    all_cats = Category.objects.all()

    item = get_object_or_404(Item, name_slug=item_slug)
    canonical_url = f'/catalog/{item_slug}'
    return render(request, 'pages/item.html', locals())

def shop_cat(request,cat_slug):
    page = request.GET.get('page')
    all_cats = Category.objects.all()
    shp = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    canonical_url = f'/catalog/{cat_slug}'
    category = get_object_or_404(Category, name_slug=cat_slug)
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
    canonical_url = f'/catalog/{cat_slug}/{subcat_slug}'
    shp = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    category = get_object_or_404(Category, name_slug=cat_slug)
    subcategory = get_object_or_404(SubCategory, name_slug=subcat_slug)
    items = Item.objects.filter(subcategory=subcategory)
    items_paginator = Paginator(items, 12)
    try:
        all_items = items_paginator.get_page(page)
    except PageNotAnInteger:
        all_items = items_paginator.page(1)
    except EmptyPage:
        all_items = items_paginator.page(items_paginator.num_pages)
    return render(request, 'pages/shop.html', locals())
