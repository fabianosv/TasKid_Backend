from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')  # rota raiz do app

urlpatterns = [
    path('', include(router.urls)),
]

