from django.db import models
from django_extensions.db.fields import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

from lazermig_.utils import image_upload_to, generate_slug


class News(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = AutoSlugField('Slug', populate_from='title', slugify_function=generate_slug)
    image = models.ImageField('Изображение', upload_to=image_upload_to)
    short_description = models.CharField('Короткое описание', max_length=255)
    description = RichTextUploadingField(verbose_name='Описание')
    date = models.DateField('Дата', auto_now=True)
    is_active = models.BooleanField('Активность', default=False)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-id']

    def __str__(self):
        return self.title
