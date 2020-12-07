from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def shop_item(request,item_slug):
    shp = True
    all_cats = Category.objects.all()

    item = get_object_or_404(Item, name_slug=item_slug)
    add_info = ''
    if item.subcategory.category_id == 1:
        add_info = item.article
    page_title = f'{item.name} {add_info}. Производство в Санкт-Петербурге по выгодным ценам'
    page_description = f'Купить {item.name} {add_info} по выгодным ценам в интернет-магазине АСПР Групп. Большой каталог. Гарантия на всю продукцию. Доставка по Санкт-Петербургу и всей России. Звоните: ☎ +7 (812) 920-81-62'

    canonical_url = f'/catalog/{item_slug}'
    return render(request, 'pages/item.html', locals())

def shop_cat(request,cat_slug):
    page = request.GET.get('page')
    all_cats = Category.objects.all()
    shp = True
    category = get_object_or_404(Category, name_slug=cat_slug)
    page_title = f'{category.name}. Производство в Санкт-Петербурге по выгодным ценам'
    page_description = f'Проектирование и производство {category.name} в компании АСПР Групп. Большой опыт, гарантия на всю продукцию, современное оборудование. Звоните: ☎ +7 (812) 920-81-62'
    canonical_url = f'/catalog/{cat_slug}'

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
    category = get_object_or_404(Category, name_slug=cat_slug)
    subcategory = get_object_or_404(SubCategory, name_slug=subcat_slug)
    shp = True
    page_title = f'{subcategory.name}. Производство в Санкт-Петербурге по выгодным ценам'
    page_description = f'Проектирование и производство {subcategory.name} в компании АСПР Групп. Большой опыт, гарантия на всю продукцию, современное оборудование. Звоните: ☎ +7 (812) 920-81-62'
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
