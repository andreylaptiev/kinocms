from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django import forms
from . import models


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.CustomUser
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
        the user, but replaces the password field with admins
        disabled password hash display field.
        """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.CustomUser
        fields = '__all__'


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
            label='Эл.почта',
            widget=forms.TextInput(attrs={'autofocus': True,
                                          'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(
                attrs={'autocomplete': 'current-password',
                       'class': 'form-control'})
    )


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
