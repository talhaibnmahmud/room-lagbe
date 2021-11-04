import uuid

from django.db import models
from django.utils.translation import gettext_lazy


# Create your models here.
class District(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    class RoomType(models.TextChoices):
        SINGLE = 'SL', gettext_lazy('Single')
        DOUBLE = 'DB', gettext_lazy('Double')
        DELUXE = 'DL', gettext_lazy('Deluxe')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=RoomType.choices)

    total_bedrooms = models.PositiveSmallIntegerField()
    total_bathrooms = models.PositiveSmallIntegerField()

    has_tv = models.BooleanField()
    has_kitchen = models.BooleanField()
    has_ac = models.BooleanField()
    has_heating = models.BooleanField()
    has_internet = models.BooleanField()

    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.type} --- {self.hotel.name}'


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self) -> str:
        return f'{self.room.type} {self.room.hotel.name}'


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=15, decimal_places=4)
    reserved_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.room.type} {self.hotel.name} {self.price}'
