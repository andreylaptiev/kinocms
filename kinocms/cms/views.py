from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from . import models


@login_required(login_url='login_user')
def statistics(request):
    context = {}
    return render(request, 'cms/statistics.html', context=context)


@login_required(login_url='login_user')
def banners(request):
    top_banner_formset = forms.MainPageTopBannerFormSet(prefix='top_banners')
    background_banner = forms.BackgroundBannerForm()
    news_banner_formset = forms.MainPageNewsBannerFormSet(prefix='news_banners')
    context = {
        'top_banner_formset': top_banner_formset,
        'background_banner': background_banner,
        'news_banner_formset': news_banner_formset,
    }

    if request.method == 'POST':
        top_banner_formset = forms.MainPageTopBannerFormSet(request.POST, request.FILES, prefix='top_banners')
        background_banner = forms.BackgroundBannerForm(request.POST, request.FILES)
        news_banner_formset = forms.MainPageNewsBannerFormSet(request.POST, request.FILES, prefix='news_banners')

        if top_banner_formset.is_valid():
            top_banner_formset.save()
            return redirect('banners')

        elif background_banner.is_valid():
            background_banner.save()
            return redirect('banners')

        elif news_banner_formset.is_valid():
            news_banner_formset.save()
            return redirect('banners')

        else:
            return HttpResponseNotFound()

    else:
        return render(request, 'cms/banners.html', context=context)


@login_required(login_url='login_user')
def film_add(request):
    film_form = forms.FilmForm()
    seo_form = forms.SeoForm()
    image_formset = forms.ImageFormSet()
    context = {
        'film_form': film_form,
        'seo_form': seo_form,
        'image_formset': image_formset
    }

    if request.method == 'POST':
        film_form = forms.FilmForm(request.POST, request.FILES)
        seo_form = forms.SeoForm(request.POST, request.FILES)
        image_formset = forms.ImageFormSet(request.POST, request.FILES)

        if film_form.is_valid() and seo_form.is_valid() and image_formset.is_valid():
            seo_form.save()
            seo_url = seo_form.cleaned_data['url']
            current_seo = models.Seo.objects.get(url=seo_url)

            film = film_form.save(commit=False)
            film_name = film_form.cleaned_data['name'].lower()
            film.gallery = models.Gallery.objects.create(name=film_name)
            film.seo = current_seo
            film.save()

            images = image_formset.save(commit=False)
            for image in images:
                image.gallery = models.Gallery.objects.get(name=film_name)
                image.save()
        return redirect('film_list')

    else:
        return render(request, 'cms/film/film_form.html', context=context)


class FilmListView(LoginRequiredMixin, ListView):
    login_url = 'login_user'
    model = models.Film
    template_name = 'cms/film/film_list.html'
    context_object_name = 'films'


class FilmDetailView(LoginRequiredMixin, DetailView):
    pass


@login_required(login_url='login_user')
def cinema_list(request):
    context = {}
    return render(request, 'cms/cinema/cinema_list.html', context=context)


@login_required(login_url='login_user')
def news_list(request):
    context = {
        'title': 'CMS | Новости',
    }
    return render(request, 'cms/page/page_list.html', context=context)


@login_required(login_url='login_user')
def action_list(request):
    context = {
        'title': 'CMS | Акции',
    }
    return render(request, 'cms/page/page_list.html', context=context)


@login_required(login_url='login_user')
def page_list(request):
    context = {
        'title': 'CMS | Страницы',
    }
    return render(request, 'cms/page/page_list.html', context=context)


@login_required(login_url='login_user')
def users(request):
    context = {}
    return render(request, 'cms/user/user_list.html', context=context)


@login_required(login_url='login_user')
def mailing(request):
    context = {}
    return render(request, 'cms/mailing.html', context=context)
