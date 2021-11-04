from rest_framework import serializers

from room import models


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = ['name', ]


class HotelSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField()

    class Meta:
        model = models.Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField()

    class Meta:
        model = models.Room
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'
