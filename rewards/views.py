from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reward, ChildReward
from .serializers import RewardSerializer, ChildRewardSerializer

class IsOwnerOrChildPermission(BasePermission):
    """
    Permissão customizada para garantir que apenas o dono ou a criança relacionada
    possa acessar o objeto.
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if hasattr(obj, 'child'):
            return obj.child.user == request.user
        return False

class RewardViewSet(viewsets.ModelViewSet):
    serializer_class = RewardSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrChildPermission]

    def get_queryset(self):
        # Retorna recompensas pertencentes ao usuário autenticado
        return Reward.objects.filter(owner=self.request.user)

class ChildRewardViewSet(viewsets.ModelViewSet):
    serializer_class = ChildRewardSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrChildPermission]

    def get_queryset(self):
        # Retorna ChildRewards vinculadas à criança do usuário autenticado
        return ChildReward.objects.filter(child__user=self.request.user)

    @action(detail=True, methods=['post'])
    def redeem(self, request, pk=None):
        """
        Action customizada para resgatar uma recompensa.
        Marca a recompensa como resgatada.
        """
        child_reward = self.get_object()

        if hasattr(child_reward, 'redeemed') and child_reward.redeemed:
            return Response({'detail': 'Recompensa já resgatada.'}, status=status.HTTP_400_BAD_REQUEST)

        child_reward.redeemed = True
        child_reward.save()

        return Response({'status': 'Recompensa resgatada com sucesso!'}, status=status.HTTP_200_OK)
