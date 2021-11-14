from django.contrib.postgres.fields import ArrayField
from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    city = models.CharField(max_length=20, verbose_name='город')
    address = models.CharField(max_length=50, verbose_name='адрес', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'кинотеатры'
        verbose_name = 'кинотеатр'


class User(models.Model):
    GENDER_CHOICES = [
        ('Man', 'Мужчина'),
        ('Woman', 'Женщина')
    ]
    first_name = models.CharField(max_length=20, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    username = models.CharField(max_length=20, verbose_name='псевдоним', unique=True)
    email = models.EmailField(verbose_name='эл.почта', unique=True)
    phone_number = models.CharField(max_length=15, verbose_name='номер мобильного', unique=True)
    city = models.CharField(max_length=20, verbose_name='город')
    date_of_birth = models.DateField(verbose_name='дата рождения')
    hashed_password = models.CharField(max_length=100, verbose_name='пароль')
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, verbose_name='пол')
    card_number = models.IntegerField(null=True, blank=True, verbose_name='номер карты')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'пользователи'
        verbose_name = 'пользователь'


class Film(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    genre = models.CharField(max_length=50, verbose_name='жанр')
    age_limit = models.CharField(max_length=50, verbose_name='возрастное ограничение')
    premiere_date = models.DateField(verbose_name='дата премьеры')
    country = models.CharField(max_length=30, verbose_name='страна')
    duration = models.CharField(max_length=20, verbose_name='продолжительность')
    budget = models.CharField(max_length=20, verbose_name='бюджет')
    director = models.CharField(max_length=100, verbose_name='режиссер')
    producer = models.CharField(max_length=100, verbose_name='продюсер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'фильмы'
        verbose_name = 'фильм'
        unique_together = ('name', 'premiere_date')


# Pages: About cinema, Cafe-Bar, VIP-hall, Advertising, Children Room
class Page(models.Model):
    name = models.CharField(max_length=20, verbose_name='название', unique=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'страницы'
        verbose_name = 'страница'


class Gallery(models.Model):
    main_picture = models.ImageField(upload_to='cms_pages/', verbose_name='главная картинка')
    additional_picture = ArrayField(models.ImageField(upload_to='cms_pages/', verbose_name='галерея картинок'), size=5)
    page = models.OneToOneField(Page, on_delete=models.CASCADE)


class Seo(models.Model):
    url = models.URLField(verbose_name='URL', unique=True)
    title = models.CharField(max_length=50, verbose_name='title')
    keywords = models.CharField(max_length=100, verbose_name='keywords')
    description = models.TextField(verbose_name='description')
    page = models.OneToOneField(Page, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'SEO блок'
        verbose_name = 'SEO блок'
