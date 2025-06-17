from rest_framework import viewsets, permissions
from .models import Reward
from .serializers import RewardSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.AllowAny]