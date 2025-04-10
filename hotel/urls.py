from django.urls import path
from .views import get_hotels, reservation_confirmation,create_hotel

urlpatterns = [
    path('hotels/', get_hotels, name='get_hotels'),
    path('reservation/', reservation_confirmation, name='reservation_confirmation'),
    path('add-hotel/', create_hotel, name='hotel_create'),
]
