from django.urls import include, path

urlpatterns = [
    path('feedback/', include('lazermig_.apps.api.feedbacks.urls')),
    path('catalog/', include('lazermig_.apps.api.catalog.urls')),
    path('news/', include('lazermig_.apps.api.news.urls')),
    path('main/', include('lazermig_.apps.api.main.urls')),
]