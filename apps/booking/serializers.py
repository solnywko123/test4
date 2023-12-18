from rest_framework import serializers
from apps.booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['room', 'start_date', 'end_date']
