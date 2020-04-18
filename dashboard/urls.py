from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.show_followed_artists, name='show_artists'),
]