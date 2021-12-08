from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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


class LoginUser(LoginView):
    form_class = forms.UserLoginForm
    template_name = 'cms/login.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('statistics')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def statistics(request):
    context = {
        'title': 'CMS | Статистика',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/statistics.html', context=context)


@login_required(login_url='login')
def banners(request):
    film_banners_formset = forms.FilmBannerFormSet()
    background_banner = forms.BackgroundBannerForm()
    context = {
        'title': 'CMS | Баннеры',
        'sidebar_pages': sidebar_pages,
        'film_banners_formset': film_banners_formset,
        'background_banner': background_banner,
    }

    if request.method == 'POST':
        film_banners_formset = forms.FilmBannerFormSet(request.POST, request.FILES)
        background_banner = forms.BackgroundBannerForm(request.POST, request.FILES)

        if film_banners_formset.is_valid():
            film_banners_formset.save()
            return redirect('banners')

        elif background_banner.is_valid():
            background_banner.save()
            return redirect('banners')

        else:
            return HttpResponseNotFound()

    else:
        return render(request, 'cms/banners.html', context=context)


@login_required(login_url='login')
def films_list(request):
    context = {
        'title': 'CMS | Фильмы',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/films/films_list.html', context=context)


@login_required(login_url='login')
def cinemas_list(request):
    context = {
        'title': 'CMS | Кинотеатры',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/cinemas/cinemas_list.html', context=context)


@login_required(login_url='login')
def news_list(request):
    context = {
        'title': 'CMS | Новости',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/news/news_list.html', context=context)


@login_required(login_url='login')
def actions_list(request):
    context = {
        'title': 'CMS | Акции',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/actions/actions_list.html', context=context)


@login_required(login_url='login')
def pages_list(request):
    context = {
        'title': 'CMS | Страницы',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/pages/pages_list.html', context=context)


@login_required(login_url='login')
def users(request):
    context = {
        'title': 'CMS | Пользователи',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/users.html', context=context)


@login_required(login_url='login')
def mailing(request):
    context = {
        'title': 'CMS | Рассылка',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/mailing.html', context=context)
