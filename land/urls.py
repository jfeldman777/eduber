from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, views1, views2, views3, views0

urlpatterns = [

    path('adm/<int:user_id>/', views0.adm, name='adm'),
    path('show_users/',views0.show_users,name='show_users'),
    path('show_adr/',views0.show_adr,name='show_adr'),
    path('show_kids/',views0.show_kids,name='show_kids'),
    path('show_places/',views0.show_places,name='show_places'),
    path('show_claims/',views0.show_claims,name='show_claims'),
    path('show_prop/',views0.show_prop,name='show_prop'),
    path('show_courses/',views0.show_courses,name='show_courses'),
    path('show_subj/',views0.show_subj,name='show_subj'),

    path('course_cre/', views.course_cre, name='course_cre'),
    path('place_cre/', views.place_cre, name='place_cre'),
    path('kid_cre/', views.kid_cre, name='kid_cre'),
    path('claim_cre/', views1.claim_cre, name='claim_cre'),
    path('prop_cre/', views1.prop_cre, name='prop_cre'),

    path('face/<int:kid_id>/', views.face, name='face'),
    path('face31/<int:place_id>/', views.face31, name='face31'),
    path('face32/<int:place_id>/', views.face32, name='face32'),
    path('face33/<int:place_id>/', views.face33, name='face33'),

    path('course_show/<int:course_id>/', views2.course_show, name='course_show'),
    path('place_show/<int:place_id>/', views2.place_show, name='place_show'),
    path('kid_show/<int:kid_id>/', views2.kid_show, name='kid_show'),

    path('place_del/<int:place_id>/', views.place_del, name='place_del'),
    path('kid_del/<int:kid_id>/', views.kid_del, name='kid_del'),
    path('course_del/<int:course_id>/', views.course_del, name='course_del'),
    path('prop_del/<int:prop_id>/', views1.prop_del, name='prop_del'),
    path('claim_del/<int:claim_id>/', views1.claim_del, name='claim_del'),

    path('prop_ed/<int:prop_id>/', views1.prop_ed, name='prop_ed'),
    path('claim_ed/<int:claim_id>/', views1.claim_ed, name='claim_ed'),
    path('course_ed/<int:course_id>/', views.course_ed, name='course_ed'),
    path('kid_ed/<int:kid_id>/', views.kid_ed, name='kid_ed'),
    path('place_ed/<int:place_id>/', views.place_ed, name='place_ed'),

    path('viewcab/<uname>/', views.viewcab, name='viewcab'),
    path('viewref/<uname>/', views.viewref, name='viewref'),
    path('grant/<int:role>/<uname>/', views.grant, name='grant'),
    path('ask/<int:role>/', views.ask, name='ask'),

    path('q/', views.q, name='q'),
    path('in/', views.xin, name='in'),

    path('chat2me/', views3.chat2me, name='chat2me'),
    path('chat2see/<int:chat_id>/', views3.chat2see, name='chat2see'),
    path('reply/<int:chat_id>/', views3.reply, name='reply'),
    path('chat/<type>/<int:obj_id>/<int:holder_id>/', views3.chat, name='chat'),

    path('c2s/<int:course_id>/', views.c2s, name='c2s'),
    path('cp2s/<int:prop_id>/', views.cp2s, name='cp2s'),

    path('map112/<lat>/<lng>/', views3.map112, name='map112'),
    path('map11/', views3.map11, name='map11'),
    path('menu/', views3.menu, name='menu'),
    path('face2/', views.face2, name='face2'),

    path('search/', views3.search, name='search'),
    path('search_pref/', views3.search_pref, name='search_pref'),

    path('scan/', views2.scan, name='scan'),
    path('demo1/', views.demo1, name='demo1'),
    path('demo2/', views.demo2, name='demo2'),
    path('demo3/', views.demo3, name='demo3'),

    path('tst/', views1.tst, name='tst'),
    path('profile/', views1.profile, name='profile'),
    path('reference/<slug:uname>/', views1.reference, name='reference'),

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
