# Generated by Django 4.1.5 on 2023-02-09 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_user_photo_meetsuser_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetsuser',
            name='registred_at',
        ),
    ]
