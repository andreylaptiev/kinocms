from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms
from . import models


sidebar_pages = [
    {'title': 'Статистика', 'url': 'statistics'},
    {'title': 'Баннеры/Слайдеры', 'url': 'banners'},
    {'title': 'Фильмы', 'url': 'film_list'},
    {'title': 'Кинотеатры', 'url': 'cinema_list'},
    {'title': 'Новости', 'url': 'news_list'},
    {'title': 'Акции', 'url': 'actions_list'},
    {'title': 'Страницы', 'url': 'pages_list'},
    {'title': 'Пользователи', 'url': 'users'},
    {'title': 'Рассылка', 'url': 'mailing'},
]


@login_required(login_url='login_user')
def statistics(request):
    context = {
        'title': 'CMS | Статистика',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/statistics.html', context=context)


@login_required(login_url='login_user')
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


@login_required(login_url='login_user')
def film_add(request):
    film_form = forms.FilmForm()
    seo_form = forms.SeoForm()
    context = {
        'title': 'CMS | Добавить фильм',
        'sidebar_pages': sidebar_pages,
        'film_form': film_form,
        'seo_form': seo_form,
    }

    if request.method == 'POST':
        film_form = forms.FilmForm(request.POST, request.FILES)
        seo_form = forms.SeoForm(request.POST, request.FILES)
        if film_form.is_valid() and seo_form.is_valid():
            seo_form.save()
            seo_url = seo_form.cleaned_data['url']
            current_seo = models.Seo.objects.get(url=seo_url)

            film = film_form.save(commit=False)
            film_name = film_form.cleaned_data['name'].lower()
            film.gallery = models.Gallery.objects.create(name=film_name)
            film.seo = current_seo
            film.save()
        return redirect('film_list')
    else:
        return render(request, 'cms/film/film_form.html', context=context)


@login_required(login_url='login_user')
def film_list(request):
    context = {
        'title': 'CMS | Фильмы',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/film/film_list.html', context=context)


@login_required(login_url='login_user')
def cinema_list(request):
    context = {
        'title': 'CMS | Кинотеатры',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/cinemas/cinemas_list.html', context=context)


@login_required(login_url='login_user')
def news_list(request):
    context = {
        'title': 'CMS | Новости',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/news/news_list.html', context=context)


@login_required(login_url='login_user')
def actions_list(request):
    context = {
        'title': 'CMS | Акции',
        'sidebar_pages': sidebar_pages,
    }
    return render(request, 'cms/actions/actions_list.html', context=context)


@login_required(login_url='login_user')
def pages_list(request):
    context = {
        'title': 'CMS | Страницы',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/pages/pages_list.html', context=context)


@login_required(login_url='login_user')
def users(request):
    context = {
        'title': 'CMS | Пользователи',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/users.html', context=context)


@login_required(login_url='login_user')
def mailing(request):
    context = {
        'title': 'CMS | Рассылка',
        'sidebar_pages': sidebar_pages
    }
    return render(request, 'cms/mailing.html', context=context)
