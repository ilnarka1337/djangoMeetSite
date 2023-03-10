# Generated by Django 4.1.5 on 2023-02-11 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meets', '0011_alter_event_owner_alter_event_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='status',
            field=models.CharField(choices=[(1, 'Открытая встреча'), (2, 'Доступ по ссылке'), (0, 'Приватная встреча')], default=0, max_length=30, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='Meet_people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meets.meet', verbose_name='Встреча')),
                ('person', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Люди')),
            ],
        ),
    ]
