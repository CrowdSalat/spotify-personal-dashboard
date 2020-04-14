from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.show_albums, name='show_albums'),
]