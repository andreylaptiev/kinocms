from django.urls import path
from .views import *


urlpatterns = [
    path('statistics/', statistics, name='statistics'),
    path('banners/', banners, name='banners'),
    path('film_list/', FilmListView.as_view(), name='film_list'),
    path('film_add/', film_add, name='film_add'),
    path('film_update/<int:film_id>/', film_update, name='film_update'),
    path('cinema_list/', cinema_list, name='cinema_list'),
    path('news_list/', news_list, name='news_list'),
    path('action_list/', action_list, name='actions_list'),
    path('page_list/', page_list, name='page_list'),
    path('users/', users, name='users'),
    path('mailing/', mailing, name='mailing'),
]
