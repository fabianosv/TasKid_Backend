from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reward, ChildReward

class RewardModelTest(TestCase):
    def setUp(self):
        self.reward = Reward.objects.create(title="Bola", description="Uma bola de futebol", points_required=100)

    def test_reward_creation(self):
        self.assertEqual(self.reward.title, "Bola")
        self.assertEqual(self.reward.points_required, 100)

class ChildRewardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='child1', password='pass')
        self.reward = Reward.objects.create(title="Bola", description="Uma bola de futebol", points_required=100)
        self.child_reward = ChildReward.objects.create(child=self.user, reward=self.reward)

    def test_child_reward_creation(self):
        self.assertEqual(self.child_reward.child.username, 'child1')
        self.assertEqual(self.child_reward.reward.title, "Bola")
        self.assertFalse(self.child_reward.redeemed)
