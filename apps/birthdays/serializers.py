from rest_framework import serializers
from .models import BirthdayReminder
from datetime import date


class BirthdaySerializer(serializers.ModelSerializer):
    days_remaining = serializers.SerializerMethodField()
    class Meta:
        model = BirthdayReminder
        fields = ['id', 'name', 'dob', 'notes', 'reminder_time','days_remaining']

    def get_days_remaining(self, obj):
        today = date.today()

        # Birthday this year
        next_birthday = obj.dob.replace(year=today.year)

        # If already passed → next year
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        return (next_birthday - today).days