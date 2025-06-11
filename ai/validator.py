from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Task
from ai.validator import compare_images

class ImageValidationView(APIView):
    def post(self, request, *args, **kwargs):
        task_id = request.data.get('task_id')
        if not task_id:
            return Response({"error": "task_id é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

        before_photo = task.photos.filter(photo_type='before').first()
        after_photo = task.photos.filter(photo_type='after').first()

        if not before_photo or not after_photo:
            return Response({"error": "São necessárias fotos do tipo 'before' e 'after'"}, status=status.HTTP_400_BAD_REQUEST)

        # Use os caminhos relativos armazenados no modelo
        image_path_before = before_photo.photo.name
        image_path_after = after_photo.photo.name

        valid = compare_images(image_path_before, image_path_after)

        return Response({
            "task_id": task_id,
            "result": "approved" if valid else "rejected"
        }, status=status.HTTP_200_OK)
