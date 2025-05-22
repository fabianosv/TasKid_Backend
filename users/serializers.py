from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Inclui campos padrão + user_type e bio
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'bio']
        read_only_fields = ['id']

    # Você pode adicionar validações customizadas aqui, se quiser
    def validate_user_type(self, value):
        if value not in ['parent', 'child']:
            raise serializers.ValidationError("Tipo de usuário inválido.")
        return value
