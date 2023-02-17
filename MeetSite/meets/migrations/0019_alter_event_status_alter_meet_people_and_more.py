# Generated by Django 4.1.5 on 2023-02-15 10:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meets', '0018_alter_event_status_alter_meet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[(1, 'Открытое мероприятие'), (2, 'Доступ по ссылке'), (0, 'Приватное мероприятие')], default=0, max_length=30, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='meet',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='meet_users', to=settings.AUTH_USER_MODEL, verbose_name='Участники встречи'),
        ),
        migrations.AlterField(
            model_name='meet',
            name='status',
            field=models.CharField(choices=[(0, 'Приватная встреча'), (2, 'Доступ по ссылке'), (1, 'Открытая встреча')], default=0, max_length=30, verbose_name='Статус'),
        ),
    ]