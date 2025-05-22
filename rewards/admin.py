from django.contrib import admin
from .models import Reward, ChildReward

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('title', 'points_required')
    search_fields = ('title',)
    list_filter = ('points_required',)

@admin.register(ChildReward)
class ChildRewardAdmin(admin.ModelAdmin):
    list_display = ('child', 'reward', 'redeemed', 'redeemed_at')
    list_filter = ('redeemed',)
    search_fields = ('child__username', 'reward__title')
    readonly_fields = ('redeemed_at',)
