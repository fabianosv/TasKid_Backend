import os

apps = {
    "users": {
        "serializers.py": '''from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type']
''',
        "views.py": '''from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
''',
        "urls.py": '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
''',
        "admin.py": '''from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'user_type')
    list_filter = ('user_type',)
'''
    },
    "tasks": {
        "serializers.py": '''from rest_framework import serializers
from .models import Task, TaskImage

class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ['id', 'image', 'is_before']

class TaskSerializer(serializers.ModelSerializer):
    images = TaskImageSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'created_at', 'due_date', 'points', 'images']
''',
        "views.py": '''from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task, TaskImage
from .serializers import TaskSerializer, TaskImageSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskImageViewSet(viewsets.ModelViewSet):
    queryset = TaskImage.objects.all()
    serializer_class = TaskImageSerializer
    permission_classes = [IsAuthenticated]
''',
        "urls.py": '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskImageViewSet

router = DefaultRouter()
router.register(r'', TaskViewSet)
router.register(r'images', TaskImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
''',
        "admin.py": '''from django.contrib import admin
from .models import Task, TaskImage

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'assigned_to', 'due_date', 'points')
    list_filter = ('assigned_to',)

@admin.register(TaskImage)
class TaskImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'is_before', 'image')
'''
    },
    "rewards": {
        "serializers.py": '''from rest_framework import serializers
from .models import Reward, ChildReward

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['id', 'name', 'description', 'points_required']

class ChildRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildReward
        fields = ['id', 'child', 'reward', 'redeemed', 'redeemed_at']
''',
        "views.py": '''from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Reward, ChildReward
from .serializers import RewardSerializer, ChildRewardSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [IsAuthenticated]

class ChildRewardViewSet(viewsets.ModelViewSet):
    queryset = ChildReward.objects.all()
    serializer_class = ChildRewardSerializer
    permission_classes = [IsAuthenticated]
''',
        "urls.py": '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RewardViewSet, ChildRewardViewSet

router = DefaultRouter()
router.register(r'', RewardViewSet)
router.register(r'child-rewards', ChildRewardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
''',
        "admin.py": '''from django.contrib import admin
from .models import Reward, ChildReward

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'points_required')

@admin.register(ChildReward)
class ChildRewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'child', 'reward', 'redeemed', 'redeemed_at')
    list_filter = ('redeemed',)
'''
    }
}

# Criação dos arquivos
for app, files in apps.items():
    os.makedirs(app, exist_ok=True)
    for filename, content in files.items():
        file_path = os.path.join(app, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Criar __init__.py
for app in apps.keys():
    init_path = os.path.join(app, '__init__.py')
    if not os.path.exists(init_path):
        with open(init_path, 'w') as f:
            f.write('# Init file for {} app\n'.format(app))

print("✅ Todos os arquivos e __init__.py foram gerados com sucesso!")