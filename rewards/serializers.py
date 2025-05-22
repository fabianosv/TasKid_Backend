from rest_framework import serializers
from .models import Reward, ChildReward

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['id', 'title', 'description', 'points_required']

class ChildRewardSerializer(serializers.ModelSerializer):
    reward = RewardSerializer(read_only=True)
    reward_id = serializers.PrimaryKeyRelatedField(queryset=Reward.objects.all(), source='reward', write_only=True)

    class Meta:
        model = ChildReward
        fields = ['id', 'child', 'reward', 'reward_id', 'redeemed', 'redeemed_at']
        read_only_fields = ['redeemed_at']
