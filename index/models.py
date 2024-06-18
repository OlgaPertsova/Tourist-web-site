from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тэг"
        verbose_name_plural = "Тэги"


class Paper(models.Model):
    title = models.CharField(max_length=100)
    description_one = models.TextField(blank=True, null=True)
    description_two = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to="index/%Y/%m/%d/", default="matreshka.png")
    demo_link = models.CharField(max_length=1000, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "статью"
        verbose_name_plural = "Статьи"
