from django.urls import path
from django.utils.translation import gettext as _
from django.conf import settings
from django.conf.urls.static import static
from . import views, views1, views2, views3, v_cde, v_face, v_map, v_show

urlpatterns = [
    path('face/<int:kid_id>/', v_face.face, name='face'),
    path('face2/', v_face.face2, name='face2'),
    path('face31/<int:place_id>/', v_face.face31, name='face31'),
    path('face32/<int:place_id>/', v_face.face32, name='face32'),
    path('face33/<int:place_id>/', v_face.face33, name='face33'),

    path('map112/<lat>/<lng>/', v_map.map112, name='map112'),
    path('map11/', v_map.map11, name='map11'),
    path('map2/<int:location_id>/', v_map.map2, name='map2'),
    path('map20/<int:location_id>/', v_map.map20, name='map20'),
    path('map/', v_map.map, name='map'),

    path('fill_page1/<int:event_id>/', v_show.fill_page1, name='fill_page1'),

    path('opt_del/<int:opt_id>/', v_cde.opt_del, name='opt_del'),
    path('opt_ed/<int:opt_id>/', v_cde.opt_ed, name='opt_ed'),
    path('opt_cre/<int:qline_id>/', v_cde.opt_cre, name='opt_cre'),

    path('qline_img_ed/<int:qline_id>/', v_cde.qline_img_ed, name='qline_img_ed'),
    path('qline_del/<int:qline_id>/', v_cde.qline_del, name='qline_del'),
    path('qline_ed/<int:qline_id>/', v_cde.qline_ed, name='qline_ed'),
    path('qline_cre/<int:qpage_id>/', v_cde.qline_cre, name='qline_cre'),

    path('qpage_qline/<int:qpage_id>/', v_cde.qpage_qline, name='qpage_qline'),
    path('qpage_cre/', v_cde.qpage_cre, name='qpage_cre'),
    path('qpage_del/<int:qpage_id>/', v_cde.qpage_del, name='qpage_del'),
    path('qpage_ed/<int:qpage_id>/', v_cde.qpage_ed, name='qpage_ed'),
    path('qpage_img_ed/<int:qpage_id>/', v_cde.qpage_img_ed, name='qpage_img_ed'),

    path('event_cre/', v_cde.event_cre, name='event_cre'),
    path('course_cre/', v_cde.course_cre, name='course_cre'),
    path('place_cre/', v_cde.place_cre, name='place_cre'),
    path('kid_cre/', v_cde.kid_cre, name='kid_cre'),
    path('claim_cre/', v_cde.claim_cre, name='claim_cre'),
    path('prop_cre/', v_cde.prop_cre, name='prop_cre'),
    path('invite_cre/<int:event_id>/', v_cde.invite_cre, name='invite_cre'),

    path('place_del/<int:place_id>/', v_cde.place_del, name='place_del'),
    path('kid_del/<int:kid_id>/', v_cde.kid_del, name='kid_del'),
    path('course_del/<int:course_id>/', v_cde.course_del, name='course_del'),
    path('event_del/<int:event_id>/', v_cde.event_del, name='event_del'),
    path('prop_del/<int:prop_id>/', v_cde.prop_del, name='prop_del'),
    path('claim_del/<int:claim_id>/', v_cde.claim_del, name='claim_del'),
    path('invite_del/<int:invite_id>/', v_cde.invite_del, name='invite_del'),

    path('del_addr/<int:location_id>/', v_cde.del_addr, name='del_addr'),

    path('invite_ed/<int:invite_id>/', v_cde.invite_ed, name='invite_ed'),
    path('prop_ed/<int:prop_id>/', v_cde.prop_ed, name='prop_ed'),
    path('claim_ed/<int:claim_id>/', v_cde.claim_ed, name='claim_ed'),
    path('course_ed/<int:course_id>/', v_cde.course_ed, name='course_ed'),
    path('event_ed/<int:event_id>/', v_cde.event_ed, name='event_ed'),

    path('kid_ed/<int:kid_id>/', v_cde.kid_ed, name='kid_ed'),
    path('place_ed/<int:place_id>/', v_cde.place_ed, name='place_ed'),

    path('c2s/<int:course_id>/', v_cde.c2s, name='c2s'),
    path('cp2s/<int:prop_id>/', v_cde.cp2s, name='cp2s'),
###########################################################################################
    path('event_show/<int:event_id>/', v_show.event_show, name='event_show'),
    path('course_show/<int:course_id>/', v_show.course_show, name='course_show'),
    path('place_show/<int:place_id>/', v_show.place_show, name='place_show'),
    path('kid_show/<int:kid_id>/', v_show.kid_show, name='kid_show'),
    path('prop_show/<int:prop_id>/', v_show.prop_show, name='prop_show'),
    path('claim_show/<int:claim_id>/', v_show.claim_show, name='claim_show'),

    path('show_pages/<int:event_id>/', v_show.show_pages, name='show_pages'),
    path('show_events/',v_show.show_events,name='show_events'),
    path('show_users/',v_show.show_users,name='show_users'),
    path('show_adr/',v_show.show_adr,name='show_adr'),
    path('show_kids/',v_show.show_kids,name='show_kids'),
    path('show_places/',v_show.show_places,name='show_places'),
    path('show_claims/',v_show.show_claims,name='show_claims'),
    path('show_prop/',v_show.show_prop,name='show_prop'),
    path('show_courses/',v_show.show_courses,name='show_courses'),
    path('show_subj/',v_show.show_subj,name='show_subj'),

    path('chat2me/', views3.chat2me, name='chat2me'),
    path('chat2see/<int:chat_id>/', views3.chat2see, name='chat2see'),
    path('reply/<int:chat_id>/', views3.reply, name='reply'),
    path('chat/<type>/<int:obj_id>/<int:holder_id>/', views3.chat, name='chat'),
    path('chat2user/<slug:uname>/', views3.chat2user, name='chat2user'),

    path('search/', views3.search, name='search'),
    path('search_pref/', views3.search_pref, name='search_pref'),

    path('good/', views2.good, name='good'),
    path('scan/', views2.scan, name='scan'),
    path('myletter/',views2.myletter,name='myletter'),
    path('friend_down/<int:user_id>/', views2.friend_down, name='friend_down'),
    path('friend_up/<int:user_id>/', views2.friend_up, name='friend_up'),
    path('adm/<int:user_id>/', views2.adm, name='adm'),

    path('profile/', views1.profile, name='profile'),
    path('reference/<slug:uname>/', views1.reference, name='reference'),
    path('obj22/<slug:uname>/', views1.obj22, name='obj22'),
    path('obj12/', views1.obj12, name='obj12'),
    path('obj/', views3.obj, name='obj'),

    path('viewcab/<uname>/', views.viewcab, name='viewcab'),
    path('viewref/<uname>/', views.viewref, name='viewref'),
    path('grant/<int:role>/<uname>/', views.grant, name='grant'),
    path('ask/<int:role>/', views.ask, name='ask'),
    path('q/', views.q, name='q'),
    path('in/', views.xin, name='in'),
    path('about/', views.about, name='about'),
    path('allabout/', views.allabout, name='allabout'),
    path('', views.index, name='index'),
]

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
