# TasKids/ai/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ImageValidationView(APIView):
    def post(self, request, *args, **kwargs):
        return Response({"valid": True}, status=status.HTTP_200_OK)
