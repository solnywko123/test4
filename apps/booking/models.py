from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

from apps.room.models import Room


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.room} - {self.start_date} to {self.end_date}"
