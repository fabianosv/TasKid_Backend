from rest_framework import serializers
from .models import User

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

    class Meta:
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
        read_only_fields = ['id', 'kids', 'guardians']

    def validate_user_type(self, value):
        if value not in ['guardian', 'kid']:
            raise serializers.ValidationError("Tipo de usuário inválido.")
        return value
