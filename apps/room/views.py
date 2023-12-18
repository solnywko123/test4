from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('cost', 'capacity')





