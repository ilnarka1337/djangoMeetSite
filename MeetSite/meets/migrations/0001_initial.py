# Generated by Django 4.1.5 on 2023-01-12 17:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('m_date', models.DateField()),
                ('m_time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('info', models.TextField(max_length=1000)),
                ('people', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('e_date', models.DateField()),
                ('e_time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('info', models.TextField(max_length=1000)),
                ('e_meets', models.ManyToManyField(to='meets.meet')),
                ('willing_people', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
