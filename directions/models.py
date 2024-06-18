from django.db import models
from users.models import Profile


class TypesRecreation(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Виды отдыха")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "вид"
        verbose_name_plural = "Виды отдыха"


class Tours(models.Model):
    owner = models.ForeignKey(TypesRecreation, on_delete=models.CASCADE, verbose_name="Вид отдыха")
    name = models.CharField(max_length=100, verbose_name="Название")
    tour_images = models.ImageField(upload_to="tour_images/", default="tour_images/trending-1.jpg", verbose_name="Изображение")
    preview = models.CharField(max_length=300, verbose_name="Превью")
    program = models.TextField(blank=True, verbose_name="Программа тура")
    price = models.DecimalField(max_digits=8, decimal_places=0, default=0, verbose_name="Цена")
    duration = models.PositiveIntegerField(default=0, verbose_name="Продолжительность")
    all_rat = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, verbose_name="Рейтинг")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-rating', '-all_rat']
        verbose_name = "тур"
        verbose_name_plural = "Туры"

    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    def get_stars_count(self):
        reviews = self.review_set.all()
        all_stars = reviews.count()
        five_stars = reviews.filter(value="5").count() * 5
        four_stars = reviews.filter(value="4").count() * 4
        three_stars = reviews.filter(value="3").count() * 3
        two_stars = reviews.filter(value="2").count() * 2
        one_stars = reviews.filter(value="1").count() * 1
        sum_stars = five_stars + four_stars + three_stars + two_stars + one_stars

        percent = sum_stars / all_stars
        self.all_rat = all_stars
        self.rating = percent
        self.save()


class Photo(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, verbose_name="Тур")
    add_photo = models.ImageField(upload_to="tour_images/add/", blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "Изображения"


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    order_name = models.CharField(max_length=100, verbose_name="Имя")
    order_email = models.CharField(max_length=100, verbose_name="Почта")
    order_tel = models.CharField(max_length=100, verbose_name="Телефон")
    order_nik_tg = models.CharField(max_length=100, verbose_name="Ник в телеграмме")
    order_people = models.PositiveIntegerField(default=0, verbose_name="Кол-во человек")
    order_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name="Когда?")
    order_tour = models.ForeignKey(Tours, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Тур")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "Заявки"


class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name="Кто оставил")
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, verbose_name="Какой тур")
    body = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    value = models.IntegerField(default=0, verbose_name="Сколько звезд")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Когда")

    def __str__(self):
        return str(f"Отзыв на {self.tour} от {self.owner}")

    class Meta:
        unique_together = [['owner', 'tour']]
        verbose_name = "отзыв"
        verbose_name_plural = "Отзывы"
