from rest_framework import serializers
from .models import Task, TaskPhoto


class TaskPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPhoto
        fields = ['id', 'image', 'type', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']


class TaskSerializer(serializers.ModelSerializer):
    photos = TaskPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'assigned_to',
            'created_at', 'completed', 'points', 'photos'
        ]
        read_only_fields = ['id', 'created_at']
