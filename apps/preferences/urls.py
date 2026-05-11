from django.urls import path
from .views import UserPreferenceView

urlpatterns = [
    path('getpreferences/', UserPreferenceView.as_view()),
]