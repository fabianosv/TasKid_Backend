from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, register_user, CustomAuthToken, KidsOfGuardianListView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('kids/', KidsOfGuardianListView.as_view(), name='kids-of-guardian'),
]
