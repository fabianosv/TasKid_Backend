from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_patterns = [
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
    path('rewards/', include('rewards.urls')),
    path('ai/', include('ai.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)