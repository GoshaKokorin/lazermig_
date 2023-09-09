from rest_framework import mixins, viewsets, permissions

from lazermig_.apps.api.mixins import MultiSerializerViewSetMixin
from lazermig_.apps.api.pagination import PageNumberPagination
from lazermig_.apps.catalog.models import Category, Product
from .serializers import CategoryListSerializer, ProductListSerializer, ProductDetailSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ProductViewSet(
    MultiSerializerViewSetMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Product.objects.filter(is_active=True)
    serializer_classes = {
        'retrieve': ProductDetailSerializer,
        'list': ProductListSerializer,
    }
    pagination_class = PageNumberPagination
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
