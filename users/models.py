from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('parent', 'Responsável'),
        ('child', 'Filho(a)'),
    )

    # Tipo do usuário: responsável ou filho(a)
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        verbose_name="Tipo de usuário",
        help_text="Selecione o tipo de usuário",
    )

    # Campo adicional opcional para uma biografia curta
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name="Biografia",
        help_text="Descrição opcional do usuário",
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
