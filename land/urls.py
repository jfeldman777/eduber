from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, views2

urlpatterns = [
    path('viewcab/<uname>/', views.viewcab, name='viewcab'),
    path('viewref/<uname>/', views.viewref, name='viewref'),
    path('grant/<int:role>/<uname>/', views.grant, name='grant'),
    path('ask/<int:role>/', views.ask, name='ask'),
    path('q/', views.q, name='q'),
    path('reference/', views.reference, name='reference'),
    path('in/', views.xin, name='in'),
    path('obj/', views.obj, name='obj'),
    path('obj12/', views.obj12, name='obj12'),

    path('map/', views.map, name='map'),

    path('kid9/<slug:user>/<slug:code>/', views2.kid9, name='kid9'),
    path('place9/<slug:user>/<slug:code>/', views2.place9, name='place9'),
    path('course9/<slug:user>/<slug:code>/', views2.course9, name='course9'),

    path('map112/<lat>/<lng>/', views2.map112, name='map112'),
    path('map11/', views2.map11, name='map11'),
    path('menu/', views2.menu, name='menu'),

    path('map2/<slug:name>/', views.map2, name='map2'),
    path('del_addr/<slug:name>/', views.del_addr, name='del_addr'),
    path('ed_addr/<slug:name>/', views.ed_addr, name='ed_addr'),
    path('ed_kid/<slug:name>/', views.ed_kid, name='ed_kid'),
    path('del_kid/<slug:name>/', views.del_kid, name='del_kid'),
    path('face/<slug:name>/', views.face, name='face'),
    path('face2/', views.face2, name='face2'),

    path('face31/<slug:code>/', views.face31, name='face31'),
    path('face32/<slug:code>/', views.face32, name='face32'),
    path('face33/<slug:code>/', views.face33, name='face33'),

    path('c2s/<slug:code>/', views.c2s, name='c2s'),

    path('ed_place/<slug:code>/', views.ed_place, name='ed_place'),
    path('del_place/<slug:code>/', views.del_place, name='del_place'),

    path('course3/<slug:uname>/<slug:code>/', views2.course3, name='course3'),
    path('ed_course/<slug:code>/', views.ed_course, name='ed_course'),
    path('del_course/<slug:code>/', views.del_course, name='del_course'),

    path('good/', views2.good, name='good'),
    path('search/', views2.search, name='search'),
    path('scan/', views2.scan, name='scan'),
    path('course/', views.course, name='course'),
    path('place/', views.place, name='place'),
    path('place3/<slug:uname>/<slug:code>/', views2.place3, name='place3'),

    path('kid3/<slug:parent>/<slug:uname>/', views2.kid3, name='kid3'),
    path('kid/', views.kid, name='kid'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('demo1/', views.demo1, name='demo1'),
    path('demo2/', views.demo2, name='demo2'),
    path('demo3/', views.demo3, name='demo3'),

    path('look3/', views2.look3, name='look3'),
    path('look2/', views2.look2, name='look2'),
    path('look/', views2.look, name='look'),
    path('', views.index, name='index'),
]

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
