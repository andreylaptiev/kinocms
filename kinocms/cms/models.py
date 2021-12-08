from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .managers import CustomUserManager


class Gallery(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', unique=True, verbose_name='картинка')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='галерея')

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'


class Cinema(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    city = models.CharField(max_length=20, verbose_name='город')
    address = models.CharField(max_length=50, verbose_name='адрес')
    map_coordinate = models.CharField(max_length=30, verbose_name='координаты Google Maps')
    phone_number = models.CharField(max_length=13, verbose_name='номер телефона')
    email = models.EmailField(verbose_name='эл.почта')
    logo_image = models.ImageField(upload_to='cinemas/', unique=True, verbose_name='логотип')
    main_image = models.ImageField(upload_to='cinemas/', unique=True, verbose_name='главная картинка')
    gallery = models.OneToOneField(Gallery, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'кинотеатр'
        verbose_name_plural = 'кинотеатры'
        unique_together = ('city', 'address')


class Hall(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    row_quantity = models.IntegerField(verbose_name='кол-во рядов')
    place_per_row = models.IntegerField(verbose_name='кол-во мест в ряду')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    scheme_image = models.ImageField(upload_to='halls/', unique=True, verbose_name='схема зала')
    main_image = models.ImageField(upload_to='halls/', unique=True, verbose_name='главная картинка')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='кинотеатр')
    gallery = models.OneToOneField(Gallery, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'зал'
        verbose_name_plural = 'залы'
        unique_together = ('name', 'cinema')


class Film(models.Model):
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

    name = models.CharField(max_length=50, verbose_name='название')
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, verbose_name='жанр')
    age_limit = models.CharField(max_length=30, verbose_name='возрастное ограничение')
    premiere_date = models.DateField(verbose_name='дата премьеры')
    country = models.CharField(max_length=30, verbose_name='страна')
    duration = models.CharField(max_length=20, verbose_name='продолжительность')
    budget = models.CharField(max_length=20, verbose_name='бюджет')
    director = models.CharField(max_length=100, verbose_name='режиссер')
    producer = models.CharField(max_length=100, verbose_name='продюсер')
    trailer_url = models.URLField(verbose_name='ссылка на трейлер')
    film_format = models.CharField(max_length=20, choices=FILM_FORMAT_CHOICES, verbose_name='формат')
    is_active = models.BooleanField(verbose_name='статус показа')
    main_image = models.ImageField(upload_to='films/', unique=True, verbose_name='главная картинка')
    gallery = models.OneToOneField(Gallery, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
        unique_together = ('name', 'premiere_date')


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


class Schedule(models.Model):
    date = models.DateField(verbose_name='дата')
    time = models.TimeField(verbose_name='время')
    ticket_price = models.IntegerField(verbose_name='стоимость билета')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name='зал')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='фильм')

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписание'
        unique_together = ('date', 'time', 'hall')


class Reservation(models.Model):
    row_number = models.IntegerField(verbose_name='ряд')
    place_number = models.IntegerField(verbose_name='место')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='посетитель')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name='событие')

    class Meta:
        verbose_name = 'бронирование'
        verbose_name_plural = 'бронирования'
        unique_together = ('row_number', 'place_number', 'schedule')


class Seo(models.Model):
    url = models.URLField(verbose_name='URL', unique=True)
    title = models.CharField(max_length=50, verbose_name='title')
    keywords = models.CharField(max_length=100, verbose_name='keywords')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SEO-блок'
        verbose_name_plural = 'SEO-блоки'


class Page(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    published_at = models.DateField(null=True, blank=True, verbose_name='дата публикации')
    video_url = models.URLField(null=True, blank=True, verbose_name='ссылка на видео')
    main_image = models.ImageField(upload_to='pages/', unique=True, verbose_name='главная картинка')
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, editable=False)
    gallery = models.OneToOneField(Gallery, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'


class MainPage(models.Model):
    phone_number1 = models.CharField(max_length=15, verbose_name='номер телефона 1')
    phone_number2 = models.CharField(max_length=15, null=True, blank=True, verbose_name='номер телефона 2')
    seo_text = models.TextField(verbose_name='SEO-текст')
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name='SEO-блок')

    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главные страницы'


class FilmBanner(models.Model):
    image = models.ImageField(upload_to='main_page/film_banners/', unique=True)
    url = models.URLField()
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'баннеры фильмов'
        verbose_name_plural = 'баннеры фильмов'


class NewsBanner(models.Model):
    image = models.ImageField(upload_to='main_page/news_banners/', unique=True, verbose_name='картинка')
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'баннеры новостей'
        verbose_name_plural = 'баннеры новостей'
