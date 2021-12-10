from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django import forms
from . import models


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(label='Псевдоним')
    email = forms.EmailField(label='Эл.почта')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = models.CustomUser
        exclude = ['is_staff', 'is_active', 'date_joined']

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
    username = forms.CharField(label='Псевдоним')
    email = forms.EmailField(label='Эл.почта')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    phone_number = forms.CharField(label='Номер мобильного')
    city = forms.CharField(label='Город')
    date_of_birth = forms.DateField(label='Дата рождения')
    gender = forms.CharField(label='Пол')
    language = forms.CharField(label='Язык')
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.CustomUser
        exclude = ['is_staff', 'is_active', 'date_joined']


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
