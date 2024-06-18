from django.db import models


class City(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="Название")
    city_image = models.ImageField(upload_to="cities/", default="cities/window.jpg", verbose_name="Изображение")
    preview = models.TextField(null=True, blank=True, verbose_name="Превью")
    info = models.TextField(blank=True, verbose_name="информация")
    link_site_city = models.CharField(max_length=500, null=True, blank=True, verbose_name="сайт города")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'город'
        verbose_name_plural = 'Города'


class Excursions(models.Model):
    owner = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Город")
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    excursions_image = models.ImageField(upload_to="excursions/", default="excursions/excursions.jpg", null=True, blank=True, verbose_name="Изображение")
    link = models.CharField(max_length=500, null=True, blank=True, verbose_name="Ссылка")
    price = models.CharField(max_length=50, null=True, blank=True, verbose_name="Цена")
    duration = models.CharField(max_length=50, null=True, blank=True, verbose_name="Продолжительность")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-duration', 'price']
        verbose_name = 'экскурсию'
        verbose_name_plural = 'Экскурсии'

