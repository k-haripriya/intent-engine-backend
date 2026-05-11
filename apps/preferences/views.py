from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserPreference
from .serializers import UserPreferenceSerializer
from rest_framework.permissions import AllowAny

class UserPreferenceView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user.is_anonymous:
            return Response({"error": "User not authenticated"}, status=401)
        preference, created = UserPreference.objects.get_or_create(user=request.user)
        serializer = UserPreferenceSerializer(preference)
        return Response(serializer.data)

    def put(self, request):
        preference, created = UserPreference.objects.get_or_create(user=request.user)
        serializer = UserPreferenceSerializer(preference, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)