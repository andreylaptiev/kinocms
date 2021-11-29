from django.shortcuts import render, redirect
from django.contrib.auth import logout
from . import forms


sidebar_pages = [
    {'title': 'Статистика', 'url': 'statistics'},
    {'title': 'Баннеры/Слайдеры', 'url': 'banners'},
    {'title': 'Фильмы', 'url': 'films_list'},
    {'title': 'Кинотеатры', 'url': 'cinemas_list'},
    {'title': 'Новости', 'url': 'news_list'},
    {'title': 'Акции', 'url': 'actions_list'},
    {'title': 'Страницы', 'url': 'pages_list'},
    {'title': 'Пользователи', 'url': 'users'},
    {'title': 'Рассылка', 'url': 'mailing'},
]


def logout_user(request):
    logout(request)
    return redirect('login')


def statistics(request):
    context = {
        'title': 'CMS | Статистика',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/statistics.html', context=context)


def banners(request):
    film_banners_form = forms.FilmBannerFormSet()
    news_banners_form = forms.NewsBannerFormSet()

    context = {
        'title': 'CMS | Баннеры',
        'sidebar_pages': sidebar_pages,
        'film_banners_form': film_banners_form,
        'news_banners_form': news_banners_form
    }
    return render(request, 'cms/banners.html', context=context)


def films_list(request):
    context = {
        'title': 'CMS | Фильмы',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/films/films_list.html', context=context)


def cinemas_list(request):
    context = {
        'title': 'CMS | Кинотеатры',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/cinemas/cinemas_list.html', context=context)


def news_list(request):
    context = {
        'title': 'CMS | Новости',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/news/news_list.html', context=context)


def actions_list(request):
    context = {
        'title': 'CMS | Акции',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/actions/actions_list.html', context=context)


def pages_list(request):
    context = {
        'title': 'CMS | Страницы',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/pages/pages_list.html', context=context)


def users(request):
    context = {
        'title': 'CMS | Пользователи',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/users.html', context=context)


def mailing(request):
    context = {
        'title': 'CMS | Рассылка',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/mailing.html', context=context)
