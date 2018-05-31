from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('gps/', views.gps, name='gps'),
    path('demo/<str:lat>/<str:lng>/', views.demo, name='demo'),
    path('', views.index, name='index'),
]
