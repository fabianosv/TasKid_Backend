from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    kids = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text="Lista de IDs das crianças associadas ao responsável"
    )
    guardians = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text="Lista de IDs dos responsáveis associados à criança"
    )

    class Meta:  # <-- Corrigido: agora está DENTRO do UserSerializer
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'user_type',
            'bio',
            'kids',
            'guardians',
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'user_type': self.user.user_type,
        })
        return data