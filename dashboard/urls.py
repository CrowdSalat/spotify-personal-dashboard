from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.show_followed_artists, name='show_album'),
    path('logout/', views.logout, name='logout'),
]