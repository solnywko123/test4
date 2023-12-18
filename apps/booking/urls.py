from django.urls import path
from .views import SearchAvailableRoomsAPIView, BookRoomAPIView, ManageRoomsAPIView, DeleteBookingAPIView

urlpatterns = [
    path('search/', SearchAvailableRoomsAPIView.as_view()),
    path('book/<int:room_id>/', BookRoomAPIView.as_view()),
    path('manage/', ManageRoomsAPIView.as_view()),
    path('delete/<int:booking_id>/', DeleteBookingAPIView.as_view()),
]

