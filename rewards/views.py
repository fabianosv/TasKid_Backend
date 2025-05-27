from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Reward
from .serializers import RewardSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'cost', 'created_by']

    def get_queryset(self):
        return Reward.objects.filter(created_by=self.request.user)

class ChildRewardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['child']

    def get_queryset(self):
        child_id = self.request.query_params.get('child')
        if child_id:
            return Reward.objects.filter(child_id=child_id)
        return Reward.objects.none()
