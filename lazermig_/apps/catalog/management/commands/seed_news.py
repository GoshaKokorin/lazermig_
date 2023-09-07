import datetime
import logging
import random

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker

from psb.news.models import News, NewsTag
from psb.seed_utils import get_file_logo
from psb.utils import generate_slug


logger = logging.getLogger('seed_news')


class Command(BaseCommand):
    help = 'Заполнение новостей тестовыми данными.'

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('Только для режима DEBUG')

        fake = Faker('ru_Ru')

        logger.info('-------Заполнение тегов-------')
        # NewsTag.objects.all().delete()
        if not NewsTag.objects.count():
            for tag_name in ['Открытая лекция', 'Финансы', 'Тематический урок', 'Технологии', 'Олимпиада']:
                logger.info(NewsTag.objects.create(**{'name': tag_name}))
        else:
            logger.info('Таблица NewsTag не пустая')

        logger.info('-------Заполнение новостей-------')
        # News.objects.all().delete()
        if not News.objects.count():
            tag_max_variants = 3 if NewsTag.objects.count() > 3 else NewsTag.objects.count()
            for _ in range(40):
                title = fake.catch_phrase()
                slug = generate_slug(title)
                new_news = {
                    'title': title,
                    'slug': slug,
                    'announcement': fake.bs(),
                    'description': fake.text(max_nb_chars=300),
                    'image': get_file_logo() if random.choice([True, False]) else None,
                    'publication_date': timezone.now() - datetime.timedelta(
                        days=random.randint(1, 1500),
                        hours=random.randint(0, 23),
                    ),
                    'time_for_read': random.randint(1, 30),
                    'meta_keywords': fake.bs(),
                    'meta_description': fake.text(max_nb_chars=100),
                    'is_active': random.choice([True, False]),
                }
                try:
                    obj = News.objects.create(**new_news)
                    # add tags
                    obj.tags.set(NewsTag.objects.order_by('?')[0: random.randint(1, tag_max_variants)])
                    # add related news
                    if obj.is_active:
                        exist_news_ids = News.objects.exclude(id=obj.id).filter(is_active=True)\
                            .order_by('?').values_list('id', flat=True)
                        if len(exist_news_ids) > 5:
                            obj.related_news.set(News.objects.filter(id__in=exist_news_ids[:3]))

                    logger.info(obj)
                except Exception as exc:
                    logger.error('News create: {}'.format(exc))
        else:
            logger.info('Таблица News не пустая')
