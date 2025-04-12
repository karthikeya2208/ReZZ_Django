from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Hotel, Reservation, Guest
from .serializers import HotelSerializer, ReservationSerializer
import random
import json

@api_view(['GET'])
def get_hotels(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def reservation_confirmation(request):
    serializer = ReservationSerializer(data=request.data)
    if not serializer.is_valid():
        print(f"Validation Errors: {serializer.errors}")
    
    if serializer.is_valid():
        data = serializer.validated_data

        # Create and save reservation (auto-generates confirmation number)
        reservation = Reservation(
            hotel_name=data['hotel_name'],
            checkin=data['checkin'],
            checkout=data['checkout'],
            name=data['name'],               
            amount=data['amount']     
        )
        reservation.save()
        print(f"Reservation ID: {reservation.id}")
        
       # Save each guest
        for guest_data in data['guests_list']:
            Guest.objects.create(
                reservation=reservation,
                name=guest_data['name'],
                gender=guest_data['gender']
            )

        return Response(reservation.confirmation_number, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_hotel(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name = data.get('name')
            price = data.get('price')
            location = data.get('location')
            availability = data.get('availability', True)  # default to True if not sent

            if not all([name, price, location]):
                return JsonResponse({'error': 'Missing required fields.'}, status=400)

            hotel = Hotel.objects.create(
                name=name,
                price=price,
                location=location,
                availability=availability
            )

            return JsonResponse({
                'message': 'Hotel created successfully.',
                'hotel': {
                    'id': hotel.id,
                    'name': hotel.name,
                    'price': str(hotel.price),
                    'location': hotel.location,
                    'availability': hotel.availability
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method allowed.'}, status=405)