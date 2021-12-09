from django import forms
from . import models


class FilmBannerForm(forms.ModelForm):
    class Meta:
        model = models.FilmBanner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                    {'placeholder': f'{field.capitalize()}',
                     'class': 'form-control'}
            )


FilmBannerFormSet = forms.modelformset_factory(models.FilmBanner, form=FilmBannerForm, can_delete=True, extra=0)


class BackgroundBannerForm(forms.ModelForm):
    image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Image
        fields = ('image',)


NewsBannerFormSet = forms.modelformset_factory(models.NewsBanner, fields='__all__', extra=3)
