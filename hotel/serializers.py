from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class ReservationSerializer(serializers.Serializer):
    hotel_name = serializers.CharField(max_length=255)
    checkin = serializers.DateField()
    checkout = serializers.DateField()
    guests_list = serializers.ListField(
        child=serializers.DictField()
    )
