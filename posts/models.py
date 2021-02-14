from django.db import models
from django.urls import reverse
from django.contrib import admin


class Category(models.Model):
    """Категории"""
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Language(models.Model):  # Actor
    """Языки программирования"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Дата создания", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="languages/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"


class Genre(models.Model):
    """Направление"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Course(models.Model):  #
    """Курсы"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Картинка", upload_to="Courses/")
    year = models.PositiveSmallIntegerField("Дата релиза", default=2020)
    country = models.CharField("Язык", max_length=30)
    directors = models.CharField(verbose_name="Автор", max_length=100)
    languages = models.ManyToManyField(Language, verbose_name="Язык программирования")
    genre = models.ManyToManyField(Genre, verbose_name="Направления")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def get_absolute_url(self):
        return reverse('courses_detail', kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)


"""
class Books(models.Model):  # 
    # Книги
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Картинка", upload_to="Courses/")
    year = models.PositiveSmallIntegerField("Дата релиза", default=2020)
    country = models.CharField("Язык", max_length=30)
    directors = models.CharField(verbose_name="Автор", max_length=100)
    languages = models.ManyToManyField(Language, verbose_name="Язык программирования")
    genre = models.ManyToManyField(Genre, verbose_name="Направления")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def get_absolute_url(self):
        return reverse('courses_detail', kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)
"""


class RatingStar(models.Model):
    """Звезды рейтинга"""
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    course = models.ForeignKey(Course, on_delete=models.CharField, verbose_name="курс")

    def __str__(self):
        return f"{self.star} - {self.course}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey("self", verbose_name='Родитель', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, verbose_name="курс", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.course}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

