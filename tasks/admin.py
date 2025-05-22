from django.contrib import admin
from django.utils.html import format_html
from .models import Task, TaskPhoto

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'assigned_to', 'points')
    list_filter = ('assigned_to',)
    search_fields = ('title', 'assigned_to__username')
    ordering = ('title',)
    raw_id_fields = ('assigned_to',)

@admin.register(TaskPhoto)
class TaskImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Preview'
