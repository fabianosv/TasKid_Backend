from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect, get_object_or_404
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
    list_display = ('id', 'title', 'assigned_to', 'status', 'approve_button', 'reject_button')
    list_filter = ('assigned_to', 'status')
    search_fields = ('title', 'assigned_to__username')
    ordering = ('title',)
    raw_id_fields = ('assigned_to',)
    inlines = [TaskPhotoInline]
    readonly_fields = ('created_at', 'submitted_at', 'validated_at')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:task_id>/approve/', self.admin_site.admin_view(self.approve_task), name='approve-task'),
            path('<int:task_id>/reject/', self.admin_site.admin_view(self.reject_task), name='reject-task'),
        ]
        return custom_urls + urls

    def approve_button(self, obj):
        if obj.status == 'SUBMITTED':
            return format_html('<a class="button" href="{}">✅ Aprovar</a>', f'/admin/tasks/task/{obj.id}/approve/')
        return '-'

    def reject_button(self, obj):
        if obj.status == 'SUBMITTED':
            return format_html('<a class="button" href="{}">❌ Rejeitar</a>', f'/admin/tasks/task/{obj.id}/reject/')
        return '-'

    approve_button.short_description = 'Aprovar'
    reject_button.short_description = 'Rejeitar'

    def approve_task(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.approve()
        self.message_user(request, "✅ Tarefa aprovada com sucesso.")
        return redirect(f'/admin/tasks/task/')

    def reject_task(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.reject()
        self.message_user(request, "❌ Tarefa rejeitada com sucesso.")
        return redirect(f'/admin/tasks/task/')


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
