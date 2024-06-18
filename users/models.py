from datetime import date
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Имя")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="Почта")
    username = models.CharField(max_length=50, null=True, blank=True, verbose_name="Логин")
    my_city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Мой город")
    profile_image = models.ImageField(upload_to="profiles/", default="profiles/notphoto.jpg", verbose_name="Фото")
    bio = models.TextField(null=True, blank=True, verbose_name="О себе")
    verify = models.BooleanField(default=False, verbose_name="Подтверждение почты")

    def __str__(self):
        return str(f"Пользователь {self.username}")

    class Meta:
        ordering = ['name']
        verbose_name = "профиль"
        verbose_name_plural = "Профили"


class Verification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"Verification object for {self.user.email}"

    def send_verification_email(self):
        link = reverse('verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        message = f'Для подтверждения учетной записи {self.user.email} перейдите по ссылке {verification_link}'

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [self.user.email]
            )
        except BadHeaderError:
            return HttpResponse("Обнаружен неверный заголовок!")

    def is_expired(self):
        return True if now() >= self.expiration else False

    class Meta:
        verbose_name = 'верификацию'
        verbose_name_plural = 'Верификация по почте'


class Places(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name="Локация")
    experience = models.TextField(null=True, blank=True, verbose_name="Впечатление")
    place_image = models.ImageField(upload_to="places/", default="places/window.jpg", verbose_name="Фото")
    creates = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return str(f"{self.location}")

    class Meta:
        verbose_name = "локацию"
        verbose_name_plural = "Локации"


class TravelDiary(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Кто создал")
    place = models.CharField(max_length=100, verbose_name="Место отдыха")
    arrival_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name="Когда приехали?")
    departure_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name="Когда уехали?")
    tickets_to_and_from = models.DecimalField(max_digits=8, decimal_places=0, default=0, verbose_name="Стоимость билетов туда и обратно")
    cafes = models.TextField(null=True, blank=True, verbose_name="Кафе и рестораны")
    housing = models.CharField(max_length=100, verbose_name="Где остановились?")
    entertainments = models.TextField(null=True, blank=True, verbose_name="Развлечения")
    transportation_costs = models.DecimalField(max_digits=8, decimal_places=0, default=0, verbose_name="Потрачено на транспорт")
    travel_image = models.ImageField(upload_to="travels/", default="travels/window.jpg", verbose_name="Фото")
    money_spend_on_eats = models.DecimalField(max_digits=8, decimal_places=0, default=0, verbose_name="Потрачено на еду")
    money_spend_on_housing = models.DecimalField(max_digits=8, decimal_places=0, default=0, verbose_name="Потрачено на жилье")
    money_spend_on_entertainments = models.DecimalField(max_digits=8, decimal_places=0, default=0, verbose_name="Потрачено на развлечения")

    def sum(self):
        return self.tickets_to_and_from + self.transportation_costs + self.money_spend_on_eats + self.money_spend_on_entertainments + self.money_spend_on_housing

    def diff_date(self):
        start = date.fromisoformat(str(self.arrival_date))
        end = date.fromisoformat(str(self.departure_date))
        self.delta = end - start
        return self.delta

    def __str__(self):
        return str(f"{self.place}")

    class Meta:
        verbose_name = "путешествие"
        verbose_name_plural = "Дневник путешествий"


class MorePhoto(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Кто создал")
    place = models.ForeignKey(TravelDiary, on_delete=models.CASCADE, verbose_name="Путешествие")
    add_more_photo = models.ImageField(upload_to="travels/add/", blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return str(f"+1 фото для {self.place}")

    class Meta:
        verbose_name = "ещё изображение"
        verbose_name_plural = "Ещё изображения"
