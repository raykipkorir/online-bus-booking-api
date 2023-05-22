from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

class Driver(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    phone_number = PhoneNumberField(blank=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class BusRoute(models.Model):
    route = models.CharField(max_length=100, unique=True)
    vip_cost = models.PositiveIntegerField()
    first_class_cost = models.PositiveIntegerField()
    business_class_cost = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.route}"


class Bus(models.Model):
    bus_number = models.PositiveIntegerField(unique=True)
    number_of_seats = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=True)

    route = models.ForeignKey(BusRoute, on_delete=models.SET_NULL, null=True)
    driver = models.OneToOneField(Driver, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Buses"

    def __str__(self):
        return f"{self.bus_number} driven by {self.driver} from {self.route}"


class Seat(models.Model):
    is_booked = models.BooleanField(default=False)
    seat_number = models.PositiveSmallIntegerField()
    trip_bus = models.ForeignKey("booking.TripBus", on_delete=models.CASCADE)

    def __str__(self):
        return f"Seat {self.seat_number} of {self.trip_bus}"
