from django.urls import include, path

urlpatterns = [
    path('feedback/', include('lazermig_.apps.api.feedbacks.urls')),
    path('catalog/', include('lazermig_.apps.api.catalog.urls')),
]