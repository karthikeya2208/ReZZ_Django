from rest_framework import serializers
from .models import Hotel

class GuestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=["Male", "Female"])


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class ReservationSerializer(serializers.Serializer):
    hotel_name = serializers.CharField(max_length=255)
    checkin = serializers.DateField()
    checkout = serializers.DateField()
    name = serializers.CharField(max_length=255)  # NEW
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)  # NEW
    guests_list = serializers.ListSerializer(
        child=GuestSerializer()
    )
