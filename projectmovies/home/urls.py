from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('thriller', views.thriller,name='thriller'),
    path('horror', views.horror,name='horror'),
    path('action', views.action,name='action'),
    path('comedy', views.comedy,name='comedy'),
    path('watchlist', views.watchlist,name='watchlist'),
    path('trending', views.trending,name='trending'),
]
