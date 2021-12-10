from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import forms
from . import models


class UserAdmin(BaseUserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number',
                    'city', 'date_of_birth', 'gender', 'language', 'is_staff', 'is_active'
                    )
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'phone_number',
                                      'city', 'date_of_birth', 'gender', 'language',)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')}),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(models.CustomUser, UserAdmin)
