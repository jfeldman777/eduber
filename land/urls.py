from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('viewcab/<uname>/', views.viewcab, name='viewcab'),
    path('viewref/<uname>/', views.viewref, name='viewref'),
    path('grant/<int:role>/<uname>/', views.grant, name='grant'),
    path('ask/<int:role>/', views.ask, name='ask'),
    path('q/', views.q, name='q'),
    path('reference/', views.reference, name='reference'),
    path('in/', views.xin, name='in'),
    path('obj/', views.obj, name='obj'),
    path('map/', views.map, name='map'),
    path('map2/<slug:name>/', views.map2, name='map2'),
    path('del_addr/<slug:name>/', views.del_addr, name='del_addr'),
    path('ed_addr/<slug:name>/', views.ed_addr, name='ed_addr'),

    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('demo1/', views.demo1, name='demo1'),
    path('demo2/', views.demo2, name='demo2'),
    path('demo3/', views.demo3, name='demo3'),
    path('', views.index, name='index'),
]

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
