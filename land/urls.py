from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('demo_map/', views.demo_map, name='demo_map'),
    path('gps/', views.gps, name='gps'),
    path('demo/<str:lat>/<str:lng>/', views.demo, name='demo'),
    path('', views.index, name='index'),
]

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
