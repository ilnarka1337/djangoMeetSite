# Generated by Django 4.1.5 on 2023-02-23 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0021_alter_event_status_alter_meet_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='e_photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='meet',
            old_name='m_photo',
            new_name='photo',
        ),
    ]
