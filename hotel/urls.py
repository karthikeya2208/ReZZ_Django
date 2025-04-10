from django.urls import path
from .views import get_hotels, reservation_confirmation

urlpatterns = [
    path('hotels/', get_hotels, name='get_hotels'),
    path('reservation/', reservation_confirmation, name='reservation_confirmation'),
]
