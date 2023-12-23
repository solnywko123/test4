from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Room, Booking
from .serializers import BookingSerializer
from apps.room.serializers import RoomSerializer


class SearchAvailableRoomsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({'error': 'Both start_date and end_date are required'},
                            status=status.HTTP_400_BAD_REQUEST)

        booked_rooms = Booking.objects.filter(
            start_date__lte=end_date,
            end_date__gte=start_date
        ).values_list('room_id', flat=True)

        available_rooms = Room.objects.exclude(id__in=booked_rooms)
        serializer = RoomSerializer(available_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookRoomAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, room_id, *args, **kwargs):
        room = get_object_or_404(Room, pk=room_id)
        serializer = BookingSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user,
                            room=room)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class ManageRoomsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        bookings = Booking.objects.all()
        room_serializer = RoomSerializer(rooms,
                                         many=True)
        booking_serializer = BookingSerializer(bookings,
                                               many=True)
        return Response({'rooms': room_serializer.data,
                         'bookings': booking_serializer.data})


class DeleteBookingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking,
                                    pk=booking_id, user=request.user)
        booking.delete()
        return Response({'message': 'Booking cancelled successfully'},
                        status=status.HTTP_204_NO_CONTENT)
