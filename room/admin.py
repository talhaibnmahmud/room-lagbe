from django.contrib import admin

from room.models import District, Hotel, Room, Media, Reservation


# Register your models here.
admin.site.register(District)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Media)
admin.site.register(Reservation)
