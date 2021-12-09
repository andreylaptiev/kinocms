from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from .managers import CustomUserManager


# Copy and change AbstractUser
class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    ]
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('ua', 'Украинский')
    ]

    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    username = models.CharField(max_length=30, validators=[username_validator], unique=True, verbose_name='псевдоним')
    email = models.EmailField(unique=True, verbose_name='эл.почта')
    phone_number = models.CharField(max_length=13, unique=True, verbose_name='номер мобильного')
    city = models.CharField(max_length=20, verbose_name='город')
    date_of_birth = models.DateField(verbose_name='дата рождения')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name='пол')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, verbose_name='язык')
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Email this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
