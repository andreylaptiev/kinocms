from django.db import models
from django.conf import settings
from django.urls import reverse
from multiselectfield import MultiSelectField


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


class Seo(models.Model):
    url = models.URLField(verbose_name='URL', unique=True)
    title = models.CharField(max_length=50, verbose_name='title')
    keywords = models.CharField(max_length=100, verbose_name='keywords')
    seo_description = models.TextField(verbose_name='description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SEO-блок'
        verbose_name_plural = 'SEO-блоки'


class Cinema(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    address = models.CharField(max_length=50, unique=True, verbose_name='адрес')
    map_coordinates = models.CharField(max_length=200, verbose_name='координаты Google Maps')
    phone_number = models.CharField(max_length=13, verbose_name='номер телефона')
    email = models.EmailField(verbose_name='эл.почта')
    logo_image = models.ImageField(upload_to='cinema/', unique=True, verbose_name='логотип')
    main_image = models.ImageField(upload_to='cinema/', unique=True, verbose_name='главная картинка')
    seo = models.OneToOneField(Seo, on_delete=models.SET_NULL, null=True)
    gallery = models.OneToOneField(Gallery, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'кинотеатр'
        verbose_name_plural = 'кинотеатры'


class Hall(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    row_quantity = models.IntegerField(verbose_name='кол-во рядов')
    place_per_row = models.IntegerField(verbose_name='кол-во мест в ряду')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    scheme_image = models.ImageField(upload_to='hall/', unique=True, verbose_name='схема зала')
    main_image = models.ImageField(upload_to='hall/', unique=True, verbose_name='главная картинка')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='кинотеатр')
    creation_date = models.DateField(auto_now_add=True)
    seo = models.OneToOneField(Seo, on_delete=models.SET_NULL, null=True)
    gallery = models.OneToOneField(Gallery, on_delete=models.SET_NULL, null=True)

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

    name = models.CharField(max_length=50, unique=True, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    premiere_date = models.DateField(verbose_name='дата премьеры')
    main_image = models.ImageField(upload_to='film/', unique=True, verbose_name='главная картинка')
    trailer = models.URLField(verbose_name='ссылка на трейлер')
    formats = MultiSelectField(max_length=20, choices=FILM_FORMAT_CHOICES, verbose_name='форматы')
    genre = models.CharField(blank=False, default='action', max_length=10, verbose_name='жанр')
    age_limit = models.CharField(max_length=30, verbose_name='возрастное ограничение')
    country = models.CharField(max_length=30, verbose_name='страна')
    duration = models.CharField(max_length=20, verbose_name='продолжительность')
    budget = models.CharField(max_length=20, verbose_name='бюджет')
    director = models.CharField(max_length=100, verbose_name='режиссер')
    producer = models.CharField(max_length=100, verbose_name='продюсер')
    is_active = models.BooleanField(verbose_name='активный')
    seo = models.OneToOneField(Seo, on_delete=models.SET_NULL, null=True)
    gallery = models.OneToOneField(Gallery, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('film_update', kwargs={'film_id': self.pk})

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'


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


class Page(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    main_image = models.ImageField(upload_to='page/', unique=True, verbose_name='главная картинка')
    video_url = models.URLField(null=True, blank=True, verbose_name='ссылка на видео')
    publish_at = models.DateField(null=True, blank=True, verbose_name='дата публикации')
    is_active = models.BooleanField(verbose_name='активная')  # Сделать это на свитче
    creation_date = models.DateField(auto_now_add=True)
    seo = models.OneToOneField(Seo, on_delete=models.SET_NULL, null=True)
    gallery = models.OneToOneField(Gallery, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'


class MainPageInfo(models.Model):
    phone_number1 = models.CharField(max_length=15, verbose_name='номер телефона 1')
    phone_number2 = models.CharField(max_length=15, null=True, blank=True, verbose_name='номер телефона 2')
    seo_text = models.TextField(verbose_name='SEO-текст')
    seo = models.OneToOneField(Seo, on_delete=models.SET_NULL, null=True, verbose_name='SEO-блок')

    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главные страницы'


class MainPageTopBanner(models.Model):
    image = models.ImageField(upload_to='main_page/top_banner/', unique=True)
    url = models.URLField()
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'главная - баннеры верх'
        verbose_name_plural = 'главная - баннеры верх'


class MainPageNewsBanner(models.Model):
    image = models.ImageField(upload_to='main_page/news_banner/', unique=True, verbose_name='картинка')
    url = models.URLField(verbose_name='URL')

    class Meta:
        verbose_name = 'главная - баннеры новостей'
        verbose_name_plural = 'главная - баннеры новостей'
