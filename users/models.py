from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('guardian', 'Responsável'),
        ('kid', 'Criança'),
    )

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        verbose_name="Tipo de usuário",
        help_text="Selecione o tipo de usuário",
    )

    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name="Biografia",
        help_text="Descrição opcional do usuário",
    )

    # Um usuário do tipo 'kid' pode estar associado a um ou mais responsáveis
    guardians = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='kids',
        blank=True,
        verbose_name="Responsáveis",
        help_text="Responsáveis ligados a essa criança"
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
