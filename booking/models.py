# pylint: disable=E1101

from django.contrib.auth import get_user_model
from django.db import models

from inventory.models import Bus, Seat

User = get_user_model()


class TripBus(models.Model):
    """Stores info for a certain trip"""
    travel_date = models.DateTimeField(auto_now_add=False)
    available_seats = models.PositiveSmallIntegerField(blank=True, null=True)
    bus = models.ForeignKey(Bus, models.CASCADE)

    class Meta:
        verbose_name_plural = "Trip Bus"

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.available_seats is None:
            self.available_seats = self.bus.number_of_seats


class Ticket(models.Model):
    ticket_number = models.CharField(
        help_text="Don't share your ticket number",
        unique=True,
        max_length=8
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cost has to be either of the 3 prices for a trip
    cost = models.PositiveIntegerField()
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    trip_bus = models.ForeignKey(TripBus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.get_fullname}'s ticket"
