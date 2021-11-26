from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, modelformset_factory, formset_factory
from django.forms.widgets import TextInput, PasswordInput
from . import models


class CinemaForm(ModelForm):
    class Meta:
        model = models.Cinema
        fields = ['name', 'description', 'city', 'address', 'map_coordinate', 'phone_number', 'email']


class PageGalleryForm(ModelForm):
    class Meta:
        model = models.PageGallery
        fields = ['page', 'main_image']


PageGalleryFormSet = modelformset_factory(models.PageGallery, fields=['additional_image'], extra=5)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))
