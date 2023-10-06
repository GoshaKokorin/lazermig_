from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-docs/', include('lazermig.apps.api.docs.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('api/', include('lazermig.apps.api.urls')),

]

admin.site.site_title = ' '
admin.site.site_header = 'Lasermig'
admin.site.index_title = 'Панель управления'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
