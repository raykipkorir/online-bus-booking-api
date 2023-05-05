from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import models

from inventory.models import Bus, Seat

# Bus = apps.get_model("inventory", "Bus")
User = get_user_model()


class TripBus(models.Model):
    """Stores info for a certain trip"""
    travel_datetime = models.DateTimeField(auto_now_add=False)

    bus = models.ForeignKey(Bus, models.CASCADE)

    class Meta:
        verbose_name_plural = "Trip Bus"


class Ticket(models.Model):
    ticket_no = models.PositiveIntegerField(help_text="Don't share your ticket number", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.get_fullname}'s ticket"

    