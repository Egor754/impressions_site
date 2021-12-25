from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Memories(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    latitude = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='Долгота')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='memories',
                              verbose_name='Пользователь')
