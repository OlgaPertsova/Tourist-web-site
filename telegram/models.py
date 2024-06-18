from django.db import models


class TgSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name="Токен")
    tg_chat = models.CharField(max_length=200, verbose_name="Чат")
    tg_message = models.TextField(null=True, blank=True, verbose_name="Сообщение")

    def __str__(self):
        return self.tg_chat
