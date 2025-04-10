from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer, ReservationSerializer
import random

@api_view(['GET'])
def get_hotels(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def reservation_confirmation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        confirmation_number = f"RES-{random.randint(100000, 999999)}"
        return Response({"confirmation_number": confirmation_number}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

