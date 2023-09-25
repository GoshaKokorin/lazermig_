from django.urls import include, path

urlpatterns = [
    path('feedback/', include('lazermig.apps.api.feedbacks.urls')),
    path('catalog/', include('lazermig.apps.api.catalog.urls')),
    path('news/', include('lazermig.apps.api.news.urls')),
    path('main/', include('lazermig.apps.api.main.urls')),
]