from django.urls import path
from .views import *


urlpatterns = [
    path('statistics/', statistics, name='statistics'),
    path('banners/', banners, name='banners'),
    path('films/', films_list, name='films_list'),
    path('cinemas/', cinemas_list, name='cinemas_list'),
    path('news/', news_list, name='news_list'),
    path('actions/', actions_list, name='actions_list'),
    path('pages/', pages_list, name='pages_list'),
    path('users/', users, name='users'),
    path('mailing/', mailing, name='mailing'),
]
