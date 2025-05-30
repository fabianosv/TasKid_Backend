from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, TaskPhoto
from .serializers import TaskSerializer, TaskPhotoSerializer
from ai.services import validar_tarefa_com_ia
from django.conf import settings
import os

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'completed', 'assigned_to', 'points']
    permission_classes = []

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

class TaskPhotoUploadView(APIView):
    permission_classes = []

    def post(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id, assigned_to=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Tarefa não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        if 'image' not in request.FILES or 'type' not in request.data:
            return Response({'error': 'Imagem e tipo são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        photo = TaskPhoto.objects.create(
            task=task,
            image=request.FILES['image'],
            type=request.data['type']
        )
        serializer = TaskPhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskValidateAIView(APIView):
    permission_classes = []

    def post(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id, assigned_to=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Tarefa não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        before_photos = task.photos.filter(type='before')
        after_photos = task.photos.filter(type='after')

        if not before_photos.exists() or not after_photos.exists():
            return Response({'message': 'Imagens insuficientes para validação.'}, status=status.HTTP_400_BAD_REQUEST)

        before_path = os.path.join(settings.MEDIA_ROOT, before_photos.last().image.name)
        after_path = os.path.join(settings.MEDIA_ROOT, after_photos.last().image.name)

        is_valid, result = validar_tarefa_com_ia(before_path, after_path)

        if is_valid:
            task.completed = True
            task.save()
            return Response({'message': result}, status=status.HTTP_200_OK)
        else:
            return Response({'message': result}, status=status.HTTP_400_BAD_REQUEST)
