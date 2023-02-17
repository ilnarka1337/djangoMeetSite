# Generated by Django 4.1.5 on 2023-02-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0017_alter_event_status_alter_meet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[(2, 'Доступ по ссылке'), (1, 'Открытое мероприятие'), (0, 'Приватное мероприятие')], default=0, max_length=30, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='meet',
            name='status',
            field=models.CharField(choices=[(2, 'Доступ по ссылке'), (1, 'Открытая встреча'), (0, 'Приватная встреча')], default=0, max_length=30, verbose_name='Статус'),
        ),
    ]
