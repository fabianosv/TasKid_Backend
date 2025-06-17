from django.db import models

class Reward(models.Model):
    title = models.CharField(max_length=100)
    points_required = models.PositiveIntegerField()

    def __str__(self):
        return self.title
