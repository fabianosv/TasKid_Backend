from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Título"))
    description = models.TextField(verbose_name=_("Descrição"))
    points = models.PositiveIntegerField(default=10, verbose_name=_("Pontos"))
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name=_("Atribuído a")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Criado em"))
    completed = models.BooleanField(default=False, verbose_name=_("Concluída"))

    def __str__(self):
        return f"{self.title} ({'Concluída' if self.completed else 'Pendente'})"

    class Meta:
        verbose_name = _("Tarefa")
        verbose_name_plural = _("Tarefas")
        ordering = ['-created_at']


class TaskPhoto(models.Model):
    class PhotoType(models.TextChoices):
        BEFORE = 'before', _('Antes')
        AFTER = 'after', _('Depois')

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name=_("Tarefa")
    )
    image = models.ImageField(upload_to='task_photos/', verbose_name=_("Imagem"))
    type = models.CharField(
        max_length=10,
        choices=PhotoType.choices,
        verbose_name=_("Tipo")
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Enviado em"))

    def __str__(self):
        return f"{self.task.title} - {self.get_type_display()}"

    class Meta:
        verbose_name = _("Foto da Tarefa")
        verbose_name_plural = _("Fotos das Tarefas")
        ordering = ['-uploaded_at']
