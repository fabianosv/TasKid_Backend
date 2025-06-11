# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('responsible', 'Responsável'),
        ('child', 'Criança'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    bio = models.TextField(blank=True)
    kids = models.ManyToManyField('self', symmetrical=False, related_name='guardians', blank=True)
    is_blocked = models.BooleanField(default=False, help_text="Bloqueado de acessar o app?")

    def __str__(self):
        return self.username
