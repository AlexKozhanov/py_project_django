from django.contrib.auth.models import AbstractUser
from django.db import models


class Idiots(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email')
    phone_number = models.CharField(
        max_length=35,
        verbose_name='Телефон',
        blank=True,
        null=True,
        help_text='Номер Телефона')
    tg_name = models.CharField(
        max_length=35,
        verbose_name='Ник ТГ',
        blank=True,
        null=True,
        help_text='Ник ТГ')
    avatar = models.ImageField(
        upload_to='idiots/avatars/',
        verbose_name='Аватар',
        blank=True,
        null=True,
        help_text='Аватар')
    country = models.CharField(
        max_length=50,
        verbose_name='Страна',
        blank=True,
        null=True,
        help_text='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
