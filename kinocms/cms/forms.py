from django import forms
from . import models
from django.forms.widgets import Textarea


class FilmForm(forms.ModelForm):
    FILM_FORMAT_CHOICES = [
        ('2D', '2D'),
        ('3D', '3D'),
        ('4DX', '4DX'),
        ('IMAX', 'IMAX')
    ]
    GENRE_CHOICES = [
        ('action', 'Боевик'),
        ('comedy', 'Комедия'),
        ('detective', 'Детектив'),
        ('horror', 'Ужасы'),
        ('thriller', 'Триллер')
    ]
    description = forms.CharField(label='Описание',
                                  widget=Textarea(attrs={'rows': 5})
                                  )

    class Meta:
        model = models.Film
        exclude = ['gallery', 'seo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                    {'placeholder': self.fields[field].label,
                     'class': 'form-control'}
            )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Image
        fields = ['image']


ImageFormSet = forms.modelformset_factory(models.Image,
                                          form=ImageForm,
                                          extra=0)


class SeoForm(forms.ModelForm):
    seo_description = forms.CharField(label='Description',
                                      widget=Textarea(attrs={'rows': 3})
                                      )

    class Meta:
        model = models.Seo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                    {'placeholder': self.fields[field].label,
                     'class': 'form-control'}
            )


class MainPageTopBannerForm(forms.ModelForm):
    image = forms.ImageField(label='')
    url = forms.URLField(label='URL')
    text = forms.CharField(label='Текст')

    class Meta:
        model = models.MainPageTopBanner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                    {'placeholder': self.fields[field].label,
                     'class': 'form-control'}
            )


MainPageTopBannerFormSet = forms.modelformset_factory(models.MainPageTopBanner,
                                                      form=MainPageTopBannerForm,
                                                      can_delete=True,
                                                      extra=0
                                                      )


class BackgroundBannerForm(forms.ModelForm):
    image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Image
        exclude = ['gallery']


class MainPageNewsBannerForm(forms.ModelForm):
    image = forms.ImageField(label='')
    url = forms.URLField(label='URL')

    class Meta:
        model = models.MainPageNewsBanner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                    {'placeholder': self.fields[field].label,
                     'class': 'form-control'}
            )


MainPageNewsBannerFormSet = forms.modelformset_factory(models.MainPageNewsBanner,
                                                       form=MainPageNewsBannerForm,
                                                       can_delete=True,
                                                       extra=0
                                                       )
