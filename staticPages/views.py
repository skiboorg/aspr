from django.shortcuts import render,get_object_or_404
from .models import *

def avtomatizaciya(request):
    page_title = 'АСПР Групп | Автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_content = HomePage.objects.all().first()
    content = AvtomatizaciyaPage.objects.all().first()
    avt = True
    return render(request, 'pages/page.html', locals())

def proizvodstvo_item(request,name_slug):
    page_title = 'АСПР Групп | Производство'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    content = get_object_or_404(Manufactory,name_slug=name_slug)
    page_content = HomePage.objects.all().first()
    pr = True
    return render(request, 'pages/page.html', locals())
def proizvodstvo(request):
    showitems = True
    page_title = 'АСПР Групп | Производство'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_content = HomePage.objects.all().first()
    content = ProizvodsvoPage.objects.all().first()
    pr = True
    return render(request, 'pages/page.html', locals())

def projects(request):
    prj = True
    page_title = 'АСПР Групп | Проекты'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    all_projects = Project.objects.all()
    return render(request, 'pages/projects.html', locals())


def napravleniya(request):
    nap = True
    page_title = 'АСПР Групп | Направления'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    content = WorkTypePage.objects.all().first()
    return render(request, 'pages/worktype.html', locals())

def about(request):
    ab = True
    page_title = 'АСПР Групп | О нас'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    content = AboutPage.objects.all().first()
    return render(request, 'pages/about.html', locals())

def index(request):
    ind = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_content = HomePage.objects.all().first()

    return render(request, 'pages/index.html', locals())
