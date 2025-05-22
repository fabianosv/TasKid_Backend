from django.db import models
from django.conf import settings

class Reward(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    points_required = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Recompensa'
        verbose_name_plural = 'Recompensas'

    def __str__(self):
        return self.title

class ChildReward(models.Model):
    child = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    redeemed = models.BooleanField(default=False)
    redeemed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Recompensa da Criança'
        verbose_name_plural = 'Recompensas das Crianças'

    def __str__(self):
        return f"{self.child.username} - {self.reward.title}"
