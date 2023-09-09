import django_filters as drf_filters
from rest_framework import mixins, viewsets, permissions
from rest_framework.response import Response

from lazermig_.apps.api.mixins import MultiSerializerViewSetMixin
from lazermig_.apps.api.pagination import PageNumberPagination
from lazermig_.apps.news.models import News, NewsTag
from .serializers import NewsDetailSerializer, NewsListSerializer, NewsTagsSerializer


class NumberInFilter(drf_filters.BaseInFilter, drf_filters.NumberFilter):
    pass


class NewsFilter(drf_filters.FilterSet):
    position = NumberInFilter(field_name='tags', distinct=True, )

    class Meta:
        model = News
        fields = []


class NewsViewSet(
    MultiSerializerViewSetMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = News.objects.filter(is_active=True)
    serializer_classes = {
        'retrieve': NewsDetailSerializer,
        'list': NewsListSerializer,
    }
    pagination_class = PageNumberPagination
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['tags']

    def list(self, request, *args, **kwargs):
        news_response = super().list(request, *args, **kwargs)
        news_tags_serializer = NewsTagsSerializer(NewsTag.objects.all(), many=True)
        return Response({
            "news_tags": news_tags_serializer.data,
            "news": news_response.data
        })

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
