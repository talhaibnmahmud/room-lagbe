from django_filters import rest_framework as drf_filters
from rest_framework import generics


# Create your views here.
from room import filters, models, serializers


class DistrictList(generics.ListAPIView):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


class HotelList(generics.ListAPIView):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelSerializer


class RoomView(generics.ListAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    filter_backends = (drf_filters.DjangoFilterBackend, )
    filterset_class = filters.RoomFilter


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = serializers.ReservationSerializer


class ReservationListView(generics.ListAPIView):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
