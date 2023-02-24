# Generated by Django 4.1.5 on 2023-02-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0022_rename_e_photo_event_photo_rename_m_photo_meet_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date'], 'verbose_name': 'ивент', 'verbose_name_plural': 'ивенты'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='e_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='e_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='meet',
            old_name='m_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='meet',
            old_name='m_time',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('1', 'Открытое мероприятие'), ('2', 'Доступ по ссылке'), ('0', 'Приватное мероприятие')], default=0, max_length=30, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='meet',
            name='status',
            field=models.CharField(choices=[('0', 'Приватная встреча'), ('1', 'Открытая встреча'), ('2', 'Доступ по ссылке')], default=0, max_length=30, verbose_name='Статус'),
        ),
    ]