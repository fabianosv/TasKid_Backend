# tasks/models.py

from django.db import models
from users.models import User
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('SUBMITTED', 'Aguardando Aprovação'),
        ('APPROVED', 'Aprovada'),
        ('REJECTED', 'Reprovada'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_tasks',
        limit_choices_to={'user_type': 'responsible'},
        help_text='Usuário responsável que criou a tarefa'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_tasks',
        limit_choices_to={'user_type': 'child'},
        help_text='Criança para quem a tarefa foi atribuída'
    )
    due_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    validated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['due_date', 'status']

    def submit(self):
        self.status = 'SUBMITTED'
        self.submitted_at = timezone.now()
        self.save()

    def approve(self):
        self.status = 'APPROVED'
        self.validated_at = timezone.now()
        self.save()

    def reject(self):
        self.status = 'REJECTED'
        self.validated_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} - {self.assigned_to.username}"

    from django.db import models

class TaskPhoto(models.Model):
        TYPE_CHOICES = (
            ('before', 'Antes'),
            ('after', 'Depois'),
        )

        task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='photos')
        image = models.ImageField(upload_to='task_photos/')
        type = models.CharField(max_length=10, choices=TYPE_CHOICES)
        uploaded_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Foto {self.type} da tarefa {self.task.title}"
