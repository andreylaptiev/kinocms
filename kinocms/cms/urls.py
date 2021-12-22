from django.urls import path
from .views import *


urlpatterns = [
    path('statistics/', statistics, name='statistics'),
    path('banners/', banners, name='banners'),
    path('film_list/', FilmListView.as_view(), name='film_list'),
    path('film_add/', film_add, name='film_add'),
    # path('film/<int:pk>', FilmDetailView.as_view(), name='film_detail'),
    path('cinema_list/', cinema_list, name='cinema_list'),
    path('news/', news_list, name='news_list'),
    path('actions/', actions_list, name='actions_list'),
    path('pages/', pages_list, name='pages_list'),
    path('users/', users, name='users'),
    path('mailing/', mailing, name='mailing'),
]
