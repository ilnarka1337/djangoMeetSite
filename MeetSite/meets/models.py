from users.models import MeetsUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.


class Meet(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название')
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    location = models.CharField(max_length=200)
    info = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='photos/meets/%Y/%m/%d/', verbose_name='Фото', blank=True)
    meet_event = models.ForeignKey('Event', blank=True, null=True, on_delete=models.CASCADE,
                                   verbose_name="Связанное мероприятие", related_name="event_linked_meets")
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    STATUS_OF_MEET = {
        ('0', "Приватная встреча"),
        ('1', "Открытая встреча"),
        ('2', "Доступ по ссылке"),
    }
    status = models.CharField(choices=STATUS_OF_MEET, default=0, verbose_name='Статус', max_length=30)
    owner = models.ForeignKey(MeetsUser, related_name='created_meets', on_delete=models.CASCADE,
                              verbose_name='Создатель', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    people = models.ManyToManyField(MeetsUser, blank=True, verbose_name="Участники встречи", related_name="meet_users")

    def get_absolute_url(self):
        return reverse('viewMeet', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'встреча'
        verbose_name_plural = 'встречи'


class Event(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name="Название")
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    location = models.CharField(max_length=200)
    info = models.TextField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to='photos/events/%Y/%m/%d/', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    STATUS_OF_EVENT = {
        ('0', "Приватное мероприятие"),
        ('1', "Открытое мероприятие"),
        ('2', "Доступ по ссылке"),
    }
    status = models.CharField(choices=STATUS_OF_EVENT, default=0, verbose_name='Статус', max_length=30)
    owner = models.ForeignKey(MeetsUser, related_name='created_events', on_delete=models.CASCADE,
                              verbose_name='Создатель', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    willing_people = models.ManyToManyField(MeetsUser, blank=True)

    def get_absolute_url(self):
        return reverse('viewEvent', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ивент'
        verbose_name_plural = 'ивенты'
        ordering = ['date']
