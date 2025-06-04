from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, TaskPhoto
from ai.validator import compare_images
from django.conf import settings
import os


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Tarefa criada: {instance.title}")
    else:
        print(f"Tarefa atualizada: {instance.title}")


@receiver(post_save, sender=TaskPhoto)
def validate_task_photos(sender, instance, created, **kwargs):
    # Só executa a IA se for uma imagem do tipo 'AFTER'
    if not created or instance.type != TaskPhoto.PhotoType.AFTER:
        return

    task = instance.task
    before = task.photos.filter(type=TaskPhoto.PhotoType.BEFORE).first()

    if before:
        print(f"[IA] Executando validação para tarefa '{task.title}'...")

        before_path = os.path.join(settings.MEDIA_ROOT, before.image.name)
        after_path = os.path.join(settings.MEDIA_ROOT, instance.image.name)

        if os.path.exists(before_path) and os.path.exists(after_path):
            try:
                result = compare_images(before_path, after_path)
                task.is_validated = result
                task.save(update_fields=["is_validated"])
                print(f"[IA] Resultado da IA: {'válido' if result else 'inválido'}")
            except Exception as e:
                print(f"[IA] Erro durante a validação: {e}")


