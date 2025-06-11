from rest_framework import serializers
from .models import Task
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.username', read_only=True)


class Meta:
    model = Task
    fields = [
        'id',
        'title',
        'description',
        'created_by',
        'created_by_name',
        'assigned_to',
        'assigned_to_name',
        'due_date',
        'status',
        'created_at',
        'submitted_at',
        'validated_at',
    ]
    read_only_fields = ['status', 'created_at', 'submitted_at', 'validated_at']


class TaskSubmitSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()


class TaskValidateSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=['approve', 'reject'])
