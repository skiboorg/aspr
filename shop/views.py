from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def shop_item(request,item_slug):
    shp = True
    all_cats = Category.objects.all()

    item = get_object_or_404(Item, name_slug=item_slug)
    add_info = ''
    try:
        if item.subcategory.category_id == 1:
            add_info = item.article
    except:
        pass
    try:
        if item.category_id == 1:
            add_info = item.article
    except:
        pass
    if add_info !='':
        page_title = f'{item.name} - купить в СПб | Артикул: {add_info}'
        page_description = f'Купить {item.name} {add_info} в интернет-магазине АСПР Групп. Купить с доставкой по Санкт-Петербургу и России. ☎ Звоните: +7 (812) 920-81-62 '

    else:
        page_title = f'{item.name}  – купить в СПб | Цена в магазине АСПР Групп'
        page_description = f'{item.name} в магазине АСПР Групп. Купить с доставкой по Санкт-Петербургу и России. ☎Звоните: +7 (812) 920-81-62'

    canonical_url = f'/catalog/items/{item_slug}'
    return render(request, 'pages/item.html', locals())

def shop_cat(request,cat_slug):
    page = request.GET.get('page', '1')

    all_cats = Category.objects.all()
    shp = True
    category = get_object_or_404(Category, name_slug=cat_slug)
    canonical_url = f'/catalog/{cat_slug}'
    if page == '0' or page == '1':
        h1 = f'{category.name}– купить в Санкт-Петербурге, цена в магазине АСПР Групп'
        page_title = f'{category.name} купить в Санкт-Петербурге, цена в магазине АСПР Групп'
        page_description = f'Купить {category.name} по выгодным ценам в интернет-магазине АСПР Групп. Большой каталог. Гарантия на всю продукцию. Доставка по Санкт-Петербургу и всей России. Звоните: ☎ +7 (812) 920-81-62'
    else:
        page_description = False
        h1 = f'Каталог товаров - страница {page}'
        page_title = f'{category.name}, страница {page}'
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

    page = request.GET.get('page', '1')

    all_cats = Category.objects.all()
    canonical_url = f'/catalog/{cat_slug}/{subcat_slug}'
    category = get_object_or_404(Category, name_slug=cat_slug)
    subcategory = get_object_or_404(SubCategory, name_slug=subcat_slug)
    shp = True
    if page == '0' or page == '1':
        h1 = f'{subcategory.name}– купить в Санкт-Петербурге, цена в магазине АСПР Групп'
        page_title = f'{subcategory.name} купить в Санкт-Петербурге, цена в магазине АСПР Групп'
        page_description = f'Купить {subcategory.name} по выгодным ценам в интернет-магазине АСПР Групп. Большой каталог. Гарантия на всю продукцию. Доставка по Санкт-Петербургу и всей России. Звоните: ☎ +7 (812) 920-81-62'
    else:
        page_description = False
        h1 = f'Каталог товаров - страница {page}'
        page_title = f'{subcategory.name}, страница {page}'
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
