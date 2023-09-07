from rest_framework import mixins, viewsets, permissions

from lazermig_.apps.api.mixins import MultiSerializerViewSetMixin
from lazermig_.apps.api.pagination import PageNumberPagination
from lazermig_.apps.news.models import News
from .serializers import NewsDetailSerializer, NewsListSerializer


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

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
