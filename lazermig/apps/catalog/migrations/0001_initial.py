# Generated by Django 4.2.5 on 2023-09-07 04:37

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import lazermig.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', verbose_name='Slug')),
                ('image', models.ImageField(upload_to=lazermig.utils.image_upload_to, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', verbose_name='Slug')),
                ('short_description', models.CharField(max_length=255, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('additional_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительный заголовок')),
                ('additional_description', models.TextField(blank=True, null=True, verbose_name='Дополнительное описание')),
                ('advantages', models.TextField(blank=True, null=True, verbose_name='Преимущества')),
                ('accessories', models.TextField(blank=True, null=True, verbose_name='Комплектующие')),
                ('guarantees', models.TextField(blank=True, null=True, verbose_name='Гарантии')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Активность')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=lazermig.utils.image_upload_to, verbose_name='Изображение')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', related_query_name='product_image', to='catalog.product', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображение товаров',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ProductCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('value', models.CharField(max_length=64, verbose_name='Значение')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_characteristics', related_query_name='product_characteristic', to='catalog.product', verbose_name='Характеристики')),
            ],
            options={
                'verbose_name': 'Характеристика товара',
                'verbose_name_plural': 'Характеристики товаров',
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='catalog.producttag', verbose_name='Теги'),
        ),
    ]
