from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from . import models


@login_required(login_url='login_user')
def statistics(request):
    context = {}
    return render(request, 'cms/statistics.html', context=context)


@login_required(login_url='login_user')
def banners(request):
    if request.method == 'POST':
        top_banner_formset = forms.MainPageTopBannerFormSet(request.POST, request.FILES,
                                                            queryset=models.MainPageTopBanner.objects.none(),
                                                            prefix='top_banner')
        background_banner_form = forms.ImageForm(request.POST, request.FILES)
        news_banner_formset = forms.MainPageNewsBannerFormSet(request.POST, request.FILES, prefix='news_banner')
        if top_banner_formset.is_valid():
            top_banner_formset.save()
            return redirect('banners')
        elif background_banner_form.is_valid():
            bg_banner = background_banner_form.save(commit=False)
            gallery = models.Gallery.objects.get(name='main_page')
            bg_banner.gallery = gallery
            bg_banner.save()
            return redirect('banners')
        elif news_banner_formset.is_valid():
            news_banner_formset.save()
            return redirect('banners')
    else:
        top_banners = models.MainPageTopBanner.objects.all()
        top_banner_formset = forms.MainPageTopBannerFormSet(queryset=models.MainPageTopBanner.objects.none(),
                                                            prefix='top_banner')
        bg_banner = models.Image.objects.get(gallery__name='main_page')
        background_banner_form = forms.ImageForm()
        news_banner_formset = forms.MainPageNewsBannerFormSet(prefix='news_banner')
        context = {
            'top_banner_formset': top_banner_formset,
            'background_banner_form': background_banner_form,
            'news_banner_formset': news_banner_formset,
            'top_banners': top_banners,
            'bg_banner': bg_banner,
        }
        return render(request, 'cms/banners.html', context)


@login_required(login_url='login_user')
def film_add(request):
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
        film_form = forms.FilmForm()
        seo_form = forms.SeoForm()
        # Don't pull images from model when creating new film
        image_qs = models.Image.objects.none()
        image_formset = forms.ImageFormSet(queryset=image_qs)
        context = {
            'film_form': film_form,
            'seo_form': seo_form,
            'image_formset': image_formset
        }
        return render(request, 'cms/film/film_form.html', context=context)


@login_required(login_url='login_user')
def film_update(request, film_id):
    if request.method == 'POST':
        film_form = forms.FilmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film_form.save()
        return redirect('film_list')
    else:
        film = get_object_or_404(models.Film, id=film_id)
        seo = film.seo
        image_queryset = models.Image.objects.filter(gallery=film.gallery)
        film_form = forms.FilmForm(instance=film)
        seo_form = forms.SeoForm(instance=seo)
        image_formset = forms.ImageFormSet(queryset=image_queryset)
        context = {
            'film_form': film_form,
            'seo_form': seo_form,
            'image_formset': image_formset
        }
        return render(request, 'cms/film/film_update.html', context)


class FilmListView(LoginRequiredMixin, ListView):
    login_url = 'login_user'
    model = models.Film
    template_name = 'cms/film/film_list.html'
    context_object_name = 'films'


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
