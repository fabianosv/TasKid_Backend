from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer, TaskSubmitSerializer, TaskValidateSerializer
from users.models import User

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'child':
            # A criança só vê suas tarefas
            return Task.objects.filter(assigned_to=user)
        elif user.user_type == 'responsible':
            # Responsável vê as tarefas criadas por ele
            return Task.objects.filter(created_by=user)
        return Task.objects.none()

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        task = self.get_object()
        user = request.user
        if user != task.assigned_to:
            return Response({"detail": "Apenas a criança designada pode submeter a tarefa."},
                            status=status.HTTP_403_FORBIDDEN)
        if task.status != 'PENDING':
            return Response({"detail": "Tarefa já submetida ou validada."},
                            status=status.HTTP_400_BAD_REQUEST)

        task.submit()
        return Response({"detail": "Tarefa submetida para aprovação."})

    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        task = self.get_object()
        user = request.user
        if user != task.created_by:
            return Response({"detail": "Apenas o responsável pode validar a tarefa."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = TaskValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        action = serializer.validated_data['action']
        if action == 'approve':
            task.approve()
            return Response({"detail": "Tarefa aprovada."})
        elif action == 'reject':
            task.reject()
            return Response({"detail": "Tarefa rejeitada."})

    @action(detail=False, methods=['get'])
    def check_block(self, request):
        user = request.user
        if user.user_type != 'child':
            return Response({"detail": "Apenas crianças usam este endpoint."},
                            status=status.HTTP_403_FORBIDDEN)

        today = timezone.now().date()
        pending_tasks = Task.objects.filter(
            assigned_to=user,
            due_date=today
        ).exclude(status='APPROVED')

        is_blocked = pending_tasks.exists()
        # Atualiza flag do usuário (opcional)
        user.is_blocked = is_blocked
        user.save(update_fields=['is_blocked'])

        return Response({"is_blocked": is_blocked})
