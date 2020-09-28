from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='shop_index'),
    # path('/<name_slug>', views.item, name='shop_item'),



]
