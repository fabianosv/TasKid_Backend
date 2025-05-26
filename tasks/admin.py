from django.contrib import admin
from django.utils.html import format_html
from .models import Task, TaskPhoto

class TaskPhotoInline(admin.TabularInline):
    model = TaskPhoto
    extra = 0
    readonly_fields = ('image_preview', 'uploaded_at', 'type')
    fields = ('image_preview', 'type', 'uploaded_at')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'assigned_to', 'points', 'completed')
    list_filter = ('assigned_to', 'completed')
    search_fields = ('title', 'assigned_to__username')
    ordering = ('title',)
    raw_id_fields = ('assigned_to',)
    inlines = [TaskPhotoInline]
    readonly_fields = ('completed',)

@admin.register(TaskPhoto)
class TaskImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'type', 'uploaded_at', 'image_tag')
    list_filter = ('type',)
    readonly_fields = ('uploaded_at', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Preview'
