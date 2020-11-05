from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('avtomatizaciya', views.avtomatizaciya, name='avtomatizaciya'),
    path('proizvodstvo', views.proizvodstvo, name='proizvodstvo'),
    path('proizvodstvo/<name_slug>', views.proizvodstvo_item, name='proizvodstvo_item'),
    path('projects', views.projects, name='projects'),
    path('napravleniya', views.napravleniya, name='napravleniya'),
    path('about', views.about, name='about'),
    path('create_item', views.create_item, name='create_item'),

    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
    # path('robots.txt', views.robots, name='robots'),


]
