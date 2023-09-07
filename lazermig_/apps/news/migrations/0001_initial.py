# Generated by Django 4.2.5 on 2023-09-07 05:12

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('short_description', models.CharField(max_length=255, verbose_name='Короткое описание')),
                ('description', tinymce.models.HTMLField(verbose_name='Описание')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-id'],
            },
        ),
    ]
