# Generated by Django 4.1.5 on 2023-02-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_userphotos_owner_remove_meetsuser_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetsuser',
            name='photo',
        ),
        migrations.AddField(
            model_name='meetsuser',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='photos/users/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='UserPhotos',
        ),
    ]