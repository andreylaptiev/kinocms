from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='название')
    main_image = models.ImageField(upload_to='???', unique=True, verbose_name='главная картинка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'


class Image(models.Model):
    image = models.ImageField(upload_to='???', unique=True, verbose_name='картинка')
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
    phone_number = models.CharField(max_length=15, verbose_name='номер телефона')
    email = models.EmailField(verbose_name='эл.почта')
    logo_image = models.ImageField(unique=True, verbose_name='логотип')
    gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, editable=False)

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
    scheme_image = models.ImageField(unique=True, verbose_name='схема зала')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, unique=True, verbose_name='кинотеатр')
    gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, editable=False)

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
    gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
        unique_together = ('name', 'premiere_date')


class User(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    ]

    first_name = models.CharField(max_length=20, verbose_name='имя')
    last_name = models.CharField(max_length=20, verbose_name='фамилия')
    username = models.CharField(max_length=30, unique=True, verbose_name='псевдоним')
    email = models.EmailField(unique=True, verbose_name='эл.почта')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='номер мобильного')
    city = models.CharField(max_length=20, verbose_name='город')
    date_of_birth = models.DateField(verbose_name='дата рождения')
    hashed_password = models.CharField(max_length=200, verbose_name='пароль')
    gender = models.CharField(max_length=6, choice=GENDER_CHOICES, verbose_name='пол')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='посетитель')
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
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, editable=False)
    gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return self.name

    # Для случаев, когда взаимодействуем с БД при переходе по ссылкам
    # from django.url import reverse
    # и исп-ть в шаблонах ссылки, которые будут сгенерированы автоматически
    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'


class MainPage(models.Model):
    phone_number1 = models.CharField(max_length=15, verbose_name='номер телефона 1')
    phone_number2 = models.CharField(max_length=15, null=True, blank=True, verbose_name='номер телефона 2')
    seo_text = models.TextField(verbose_name='SEO-текст')
    bg_image = models.ImageField(unique=True, verbose_name='фоновое изображение')
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name='SEO-блок')

    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главные страницы'


class FilmBanner(models.Model):
    image = models.ImageField(unique=True, verbose_name='картинка')
    url = models.URLField(verbose_name='URL')
    text = models.CharField(max_length=100, verbose_name='текст')

    class Meta:
        verbose_name = 'баннеры фильмов'
        verbose_name_plural = 'баннеры фильмов'


class NewsBanner(models.Model):
    image = models.ImageField(unique=True, verbose_name='картинка')
    url = models.URLField(verbose_name='URL')

    class Meta:
        verbose_name = 'баннеры новостей'
        verbose_name_plural = 'баннеры новостей'
