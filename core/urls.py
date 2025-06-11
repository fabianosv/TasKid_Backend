from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),  # todas as rotas de tasks começam com /api/tasks/
    path('api/auth/', include('rest_framework.urls')),  # autenticação DRF
]
