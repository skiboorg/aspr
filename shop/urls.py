from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('items/<item_slug>/', views.shop_item, name='shop_item'),
    path('<cat_slug>/', views.shop_cat, name='shop_cat'),
    path('<cat_slug>/<subcat_slug>/', views.shop_subcat, name='shop_subcat'),

    # path('/<name_slug>', views.item, name='shop_item'),



]
