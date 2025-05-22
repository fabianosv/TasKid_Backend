from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Tarefa criada: {instance.title}")
    else:
        print(f"Tarefa atualizada: {instance.title}")
