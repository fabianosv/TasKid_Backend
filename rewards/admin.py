from django.contrib import admin
from .models import Reward

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('title', 'points_required')
    search_fields = ('title',)
    list_filter = ('points_required',)

