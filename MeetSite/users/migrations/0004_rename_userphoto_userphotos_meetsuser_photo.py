# Generated by Django 4.1.5 on 2023-01-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPhoto',
            new_name='UserPhotos',
        ),
        migrations.AddField(
            model_name='meetsuser',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
