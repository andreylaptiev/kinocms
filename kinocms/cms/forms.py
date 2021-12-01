from django import forms
from django.forms import ModelForm, modelformset_factory, modelform_factory
from django.forms.widgets import TextInput, PasswordInput, FileInput
from . import models


FilmBannerFormSet = modelformset_factory(models.FilmBanner, fields='__all__', can_delete=True)


NewsBannerFormSet = modelformset_factory(models.NewsBanner, fields='__all__', extra=3)
