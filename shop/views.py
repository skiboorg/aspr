from django.shortcuts import render
from .models import Item
def index(request):
    shp = True
    page_title = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    page_description = 'АСПР Групп | Санкт-Петербург | Промышленная автоматизация'
    all_items = Item.objects.all()

    return render(request, 'pages/shop.html', locals())
