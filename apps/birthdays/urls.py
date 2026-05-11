from django.urls import path
from .views import (
    BirthdayListCreateView,
    BirthdayDetailView,
    UpcomingBirthdaysView
)

urlpatterns = [
    path('', BirthdayListCreateView.as_view()),
    path('<int:pk>/', BirthdayDetailView.as_view()),
    path('upcoming/', UpcomingBirthdaysView.as_view()),
]