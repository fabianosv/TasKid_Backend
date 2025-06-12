from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from .models import User
from .serializers import UserSerializer

User = get_user_model()


# ✅ Registro de novo usuário
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data

    if User.objects.filter(username=data['username']).exists():
        return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=data['username'],
        email=data['email'],  # ✅ Add email field
        password=make_password(data['password']),
        user_type=data.get('user_type', 'guardian')
    )

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'message': 'User registered successfully',
        'token': token.key,
        'user_id': user.pk,
        'email': user.email
    }, status=status.HTTP_201_CREATED)


# ✅ Login de usuário com token
class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user_type': user.user_type,
        })


# ✅ Lista/CRUD completo de usuários (admin ou uso interno)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_type', 'username', 'email']


# ✅ Lista de crianças do responsável autenticado
class KidsOfGuardianListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.kids.all()
