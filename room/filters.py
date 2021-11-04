from django_filters import rest_framework as drf_filters

from room import models


class RoomFilter(drf_filters.FilterSet):
    price = drf_filters.RangeFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = models.Room
        fields = [
            'hotel__district',
            'type',
            'has_tv',
            'has_ac',
            'has_kitchen',
            'has_heating',
            'has_internet',
        ]
