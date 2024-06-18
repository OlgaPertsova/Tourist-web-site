from django.db import models
from cities.models import City


class Months(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Месяца")
    css = models.CharField(max_length=200, default="-", verbose_name="CSS класс")
    dt_f = models.CharField(max_length=200, default="-", verbose_name="data-f")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "месяца"
        verbose_name_plural = "Месяц"


class Festival(models.Model):
    owner = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Город")
    title = models.CharField(max_length=100, verbose_name="Название")
    info = models.TextField(blank=True, verbose_name="Информация")
    date_of_the = models.DateField(auto_now=False, verbose_name="Когда?")
    link = models.CharField(max_length=500, blank=True, null=True, verbose_name="ссылка на сайт")
    css = models.CharField(max_length=200, default="-", verbose_name="CSS класс")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_of_the']
        verbose_name = "фестиваль"
        verbose_name_plural = "Фестивали"


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name="Описание")
    featured_image = models.ImageField(upload_to="news/%Y/%m/%d/", verbose_name="Изображение")
    new_link = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Ссылка")
    tags = models.TextField(blank=True, null=True, verbose_name="Тэг")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name = "новость"
        verbose_name_plural = "Новости"


class LifeHacks(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=600, verbose_name="Описание")
    featured_image = models.ImageField(upload_to="lifehacks/%Y/%m/%d/", verbose_name="Изображение")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name = "лайфхак"
        verbose_name_plural = "Лайфхаки"

