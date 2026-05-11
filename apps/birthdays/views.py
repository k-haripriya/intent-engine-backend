from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import BirthdayReminder
from .serializers import BirthdaySerializer

from datetime import date


class BirthdayListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        birthdays = BirthdayReminder.objects.filter(user=request.user)
        serializer = BirthdaySerializer(birthdays, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BirthdaySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class BirthdayDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, user, pk):
        return BirthdayReminder.objects.get(id=pk, user=user)

    def put(self, request, pk):
        birthday = self.get_object(request.user, pk)
        serializer = BirthdaySerializer(birthday, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        birthday = self.get_object(request.user, pk)
        birthday.delete()
        return Response(status=204)

class UpcomingBirthdaysView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        birthdays = BirthdayReminder.objects.filter(user=request.user)

        def next_birthday(b):
            next_bday = b.dob.replace(year=today.year)
            if next_bday < today:
                next_bday = next_bday.replace(year=today.year + 1)
            return next_bday

        sorted_birthdays = sorted(birthdays, key=next_birthday)

        serializer = BirthdaySerializer(sorted_birthdays, many=True)
        return Response(serializer.data)