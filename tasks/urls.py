from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskPhotoUploadView, TaskValidateAIView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:task_id>/upload_photo/', TaskPhotoUploadView.as_view(), name='task-photo-upload'),
    path('tasks/<int:task_id>/validate_ai/', TaskValidateAIView.as_view(), name='task-validate-ai'),
]
