from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, views1, views2

urlpatterns = [

    path('face/<int:kid_id>/', views.face, name='face'),
    path('face31/<int:place_id>/', views.face31, name='face31'),
    path('face32/<int:place_id>/', views.face32, name='face32'),
    path('face33/<int:place_id>/', views.face33, name='face33'),

    path('course9/<int:course_id>/', views2.course9, name='course9'),
    path('course3/<int:course_id>/', views2.course3, name='course3'),
    path('ed_course/<int:course_id>/', views.ed_course, name='ed_course'),

    path('place9/<int:place_id>/', views2.place9, name='place9'),
    path('place3/<int:place_id>/', views2.place3, name='place3'),
    path('ed_place/<int:place_id>/', views.ed_place, name='ed_place'),

    path('del_place/<int:place_id>/', views.del_place, name='del_place'),
    path('del_kid/<int:kid_id>/', views.del_kid, name='del_kid'),
    path('del_course/<int:course_id>/', views.del_course, name='del_course'),

    path('ed_kid/<int:kid_id>/', views.ed_kid, name='ed_kid'),
    path('kid3/<int:kid_id>/', views2.kid3, name='kid3'),
    path('kid9/<int:kid_id>/', views2.kid9, name='kid9'),

    path('viewcab/<uname>/', views.viewcab, name='viewcab'),
    path('viewref/<uname>/', views.viewref, name='viewref'),
    path('grant/<int:role>/<uname>/', views.grant, name='grant'),
    path('ask/<int:role>/', views.ask, name='ask'),

    path('q/', views.q, name='q'),
    path('in/', views.xin, name='in'),
    path('chat2me/', views2.chat2me, name='chat2me'),

    path('c2s/<int:course_id>/', views.c2s, name='c2s'),

    path('map112/<lat>/<lng>/', views2.map112, name='map112'),
    path('map11/', views2.map11, name='map11'),
    path('menu/', views2.menu, name='menu'),
    path('face2/', views.face2, name='face2'),

    path('search/', views2.search, name='search'),
    path('scan/', views2.scan, name='scan'),
    path('course/', views.course, name='course'),
    path('place/', views.place, name='place'),
    path('kid/', views.kid, name='kid'),


    path('demo1/', views.demo1, name='demo1'),
    path('demo2/', views.demo2, name='demo2'),
    path('demo3/', views.demo3, name='demo3'),
    path('look3/', views2.look3, name='look3'),
    path('look2/', views2.look2, name='look2'),
    path('look/', views2.look, name='look'),

    path('profile/', views1.profile, name='profile'),
    path('reference/', views1.reference, name='reference'),

    path('del_addr/<int:location_id>/', views.del_addr, name='del_addr'),
    path('map2/<int:location_id>/', views.map2, name='map2'),
    path('map/', views.map, name='map'),

    path('obj12/', views1.obj12, name='obj12'),
    path('obj/', views1.obj, name='obj'),

    path('about/', views.about, name='about'),
    path('good/', views2.good, name='good'),
    path('', views.index, name='index'),
]

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
