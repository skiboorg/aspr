from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from staticPages.views import customhandler404
from staticPages.sitemaps import *
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
     'ProizvodstvoSitemap': ProizvodstvoSitemap,
     'ItemsSitemap': ItemsSitemap,
}

admin.site.site_header = "Aдминистрирование"
admin.site.site_title = "Aдминистрирование"
admin.site.index_title = "Aдминистрирование"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staticPages.urls')),
    path('catalog/', include('shop.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = customhandler404
