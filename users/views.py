from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_type', 'username', 'email'] # Campos filtráveis

class KidsOfGuardianListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
     return self.request.user.kids.all()