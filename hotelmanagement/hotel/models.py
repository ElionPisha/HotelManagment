from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    room_num = models.IntegerField()
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.room_num)  