from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RewardViewSet, ChildRewardViewSet

router = DefaultRouter()
router.register(r'rewards', RewardViewSet, basename='reward')
router.register(r'child-rewards', ChildRewardViewSet, basename='childreward')

urlpatterns = [
    path('', include(router.urls)),
]
