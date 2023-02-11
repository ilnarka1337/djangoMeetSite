import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.urls import reverse


# Create your models here.

class MeetsUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация')
    photo = models.ImageField(upload_to='photos/users/%Y/%m/%d/', blank=True)
    location = models.CharField(max_length=30, blank=True, verbose_name='Локация')
    birth_date = models.DateField(blank=True, default=datetime.date(2000, 1, 1), verbose_name='Дата рождения')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile_view', kwargs={"pk": self.pk})


class City(models.Model):
    title = models.CharField(max_length=40, blank=True)
