from django.shortcuts import render,get_object_or_404
from .models import *
# from openpyxl import load_workbook
# import urllib
# from urllib.parse import urlparse
# import requests
# from django.core.files.base import ContentFile
from shop.models import *

def avtomatizaciya(request):
    all_cats = Category.objects.all()
    page_title = 'АСПР Групп | Автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_content = HomePage.objects.all().first()
    content = AvtomatizaciyaPage.objects.all().first()
    avt = True
    return render(request, 'pages/page.html', locals())

def proizvodstvo_item(request,name_slug):
    all_cats = Category.objects.all()
    page_title = 'АСПР Групп | Производство'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    content = get_object_or_404(Manufactory,name_slug=name_slug)
    page_content = HomePage.objects.all().first()
    pr = True
    return render(request, 'pages/page.html', locals())
def proizvodstvo(request):
    showitems = True
    all_cats = Category.objects.all()
    page_title = 'АСПР Групп | Производство'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_content = HomePage.objects.all().first()
    content = ProizvodsvoPage.objects.all().first()
    pr = True
    return render(request, 'pages/page.html', locals())

def projects(request):
    prj = True
    all_cats = Category.objects.all()
    page_title = 'АСПР Групп | Проекты'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    all_projects = Project.objects.all()
    return render(request, 'pages/projects.html', locals())


def napravleniya(request):
    all_cats = Category.objects.all()
    nap = True
    page_title = 'АСПР Групп | Направления'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    content = WorkTypePage.objects.all().first()
    return render(request, 'pages/worktype.html', locals())

def create_item(request):
    all_items = Item.objects.all()
    for i in all_items:
        i.save()
#     url = '/home/xxx/SEO aspr.tech/shud/'
#     wb = load_workbook(filename=f'{url}items.xlsx')
#     sheet = wb.active
#     max_row = sheet.max_row
#     max_column = sheet.max_column
#
#
#
#
#     for i in range(363, max_row + 1):
#         article = sheet.cell(row=i, column=1).value
#
#         if not article:
#             break
#         engine_count = sheet.cell(row=i, column=2).value
#         engine_power = sheet.cell(row=i, column=3).value
#         engine_start = sheet.cell(row=i, column=4).value
#         manufactor = sheet.cell(row=i, column=5).value
#
#         defence = sheet.cell(row=i, column=6).value
#         price = sheet.cell(row=i, column=7).value
#         size_shelter = sheet.cell(row=i, column=8).value
#         setup_type = sheet.cell(row=i, column=9).value
#         warranty = sheet.cell(row=i, column=10).value
#         life_time = sheet.cell(row=i, column=11).value
#         work_temperature = sheet.cell(row=i, column=12).value
#         kabel_input = sheet.cell(row=i, column=13).value
#
#
#         print(price)
#
#
#
#         try:
#             manufactor = Manufactor.objects.get(name=manufactor)
#         except:
#             manufactor = Manufactor.objects.create(name=manufactor)
#
#         full_d="""
# <p align="justify"><font color="#000000"><font size="5"><b>Описание ШУД (шкаф управления двигателем)</b></font></font></p>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">используется для запуска электродвигателей методами прямого пуска, плавным пуском или преобразователем частоты. Может быть применен как в объектах коммунального хозяйства (насосные станции водоканала, тэц и т.д.), так и на промышленных объектах (включение конвейера, мельницы и т.д.). В зависимости от технологического процесса инженер выбирает наиболее оптимальный метод включения электродвигателя. </font></font></font></font></p>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#000000"><font size="5"><b>Функционал, который обеспечивает шкаф ШУД.</b></font></font></font></font></p>
#
# <ul>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Защита от перегрузок и коротких замыканий</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Включение электродвигателя устройством плавного пуска</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Включение электродвигателя преобразователем частоты</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Включение электродвигателя прямым пуском</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Защита от недопустимых перенапряжения, перекоса и обрыва фаз</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Защита по датчикам температуры, уровня масла и т.д. электродвигателя</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Защита токоведущих частей</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">При необходимости можно добавить второй ввод и возможность подключения системы АВР</font></font></font></font></p>
# 	</li>
# </ul>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#000000"><font size="5"><b>Основные комплектующие шкафа управления двигателем</b></font></font></font></font></p>
#
# <ol>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">На выбор предоставлены 3 варианта комплектации оборудования: </font></font></font></font></p>
# 	</li>
# </ol>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">- корейский производитель </font></font><font color="#363c46"><font size="2">Hyundai</font></font></font></font></p>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">- </font></font><font color="#363c46"><font size="2">Schneider Electric</font></font></font></font></p>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">- ABB</font></font></font></font></p>
#
# <ol start="2">
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Несколько вариантов защиты корпуса: </font></font><font color="#363c46"><font size="2">IP</font></font><font color="#363c46"><font size="2">31, </font></font><font color="#363c46"><font size="2">IP</font></font><font color="#363c46"><font size="2">54, </font></font><font color="#363c46"><font size="2">IP</font></font><font color="#363c46"><font size="2">65</font></font></font></font></p>
# 	</li>
# 	<li>
# 	<p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Доп. оборудование в зависимости от номинального тока шкафа</font></font></font></font></p>
# 	</li>
# </ol>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#000000"><font size="5"><b>Что сделать для заказа шкафа управления двигателем?</b></font></font></font></font></p>
#
# <p align="justify"><font color="#000000"><font size="5"><font color="#363c46"><font size="2">Вы можете прислать Ваше задание на сборку ШУД (однолинейная схема, описание или любое другое). Наш инженер проработает спецификацию и внешний вид шкафа перед заказом. В случае отсутствия задания Вы можете выбрать из готовых решений на нашем сайте</font></font></font></font></p>
#
#         """
#
#         new_item = Item.objects.create(
#             name='Шкаф управления двигателем ШУД (ШПЧ, ШУПП)',
#             subcategory_id=4,
#
#             price=int(price),
#             article=article,
#             engine_count=engine_count,
#             engine_power=engine_power,
#             engine_start=engine_start,
#
#             # is_avr = True if is_avr == 'Да' else False,
#             # is_counters = True if is_counters == 'Да' else False,
#             manufactor=manufactor,
#             # power=power,
#             # tok_str=tok_str,
#             # number_faz=number_faz,
#             # napryag=napryag
#              defence=defence,
#             # number_zadvigek=number_zadvigek,
#             # engine_tok=engine_tok,
#              setup_type=setup_type,
#              size_shelter=size_shelter,
#              warranty=warranty,
#              life_time=life_time,
#
#              work_temperature=work_temperature,
#              kabel_input=kabel_input,
#
#              full_description=full_d,
#             image='items/shud.jpg'
#             )
#



    return render(request, 'page/about.html', locals())
def about(request):
    ab = True
    all_cats = Category.objects.all()
    page_title = 'АСПР Групп | О нас'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    content = AboutPage.objects.all().first()
    return render(request, 'pages/about.html', locals())

def index(request):
    ind = True
    all_cats = Category.objects.all()
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_content = HomePage.objects.all().first()

    return render(request, 'pages/index.html', locals())
