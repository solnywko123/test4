from django.db import models


class Room(models.Model):
    room_id = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.room_id
