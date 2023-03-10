# Generated by Django 4.1.5 on 2023-01-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0003_alter_event_options_alter_meet_options_event_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/meets/%Y/%m/%d/', verbose_name='Фото')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ManyToManyField(blank=True, to='meets.appphoto'),
        ),
        migrations.AddField(
            model_name='meet',
            name='photo',
            field=models.ManyToManyField(blank=True, to='meets.appphoto'),
        ),
    ]
