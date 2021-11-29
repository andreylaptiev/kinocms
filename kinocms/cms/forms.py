from django import forms
from django.forms import ModelForm, modelformset_factory
from django.forms.widgets import TextInput, PasswordInput, FileInput
from . import models


FilmBannerFormSet = modelformset_factory(models.FilmBanner, fields='__all__', extra=3,
                                         widgets={'url': TextInput(attrs={'class': 'form-control'}),
                                                  'text': TextInput(attrs={'class': 'form-control'}),
                                                  'image': FileInput(attrs={'class': 'form-control'})}
                                         )


NewsBannerFormSet = modelformset_factory(models.NewsBanner, fields='__all__', extra=3)
