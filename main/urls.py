from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^sitemap.xml', views.sitemap, name='sitemap'),
                  url(r'^robots.txt', views.robots, name="robots"),
                  url(r'^ads.txt', views.ads, name='ads'),
]
