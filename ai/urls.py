# TasKids/ai/urls.py

from django.urls import path
from .views import ImageValidationView

urlpatterns = [
    path('validate/', ImageValidationView.as_view(), name='image-validate'),
]
