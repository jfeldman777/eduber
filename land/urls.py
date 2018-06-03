from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('in/', views.xin, name='in'),
    path('about/', views.about, name='about'),
    #path('map/', views.map, name='map'),
    #path('demo_map/', views.demo_map, name='demo_map'),
    #path('gps/', views.gps, name='gps'),
    #path('demo/<str:lat>/<str:lng>/', views.demo, name='demo'),
    path('demo1/', views.demo1, name='demo1'),
    path('demo2/', views.demo2, name='demo2'),
    path('demo3/', views.demo3, name='demo3'),
    path('', views.index, name='index'),
]

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
