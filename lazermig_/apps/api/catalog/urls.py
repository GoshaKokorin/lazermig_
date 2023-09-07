from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet


router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
