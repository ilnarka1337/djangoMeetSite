# Generated by Django 4.1.5 on 2023-02-05 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0005_remove_event_photo_remove_meet_photo_event_e_photo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['e_date'], 'verbose_name': 'ивент', 'verbose_name_plural': 'ивенты'},
        ),
    ]