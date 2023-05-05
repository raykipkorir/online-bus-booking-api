from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# BookBus = apps.get_model("booking", "BookBus")
User = get_user_model()

class Driver(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    phone_number = PhoneNumberField(blank=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class BusRoute(models.Model):
    route = models.CharField(max_length=100, unique=True)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.route} {self.get_cost}"
    
    @property
    def get_cost(self):
        return f"{settings.CURRENCY}{self.cost}"


class Bus(models.Model):
    bus_number = models.PositiveIntegerField(unique=True)
    number_of_seats = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=True)

    # user = models.ManyToManyField(User, through="booking.BookBus")
    route = models.ForeignKey(BusRoute, on_delete=models.SET_NULL, null=True)
    driver = models.OneToOneField(Driver, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Buses"

    def __str__(self):
        return f"{self.bus_number} driven by {self.driver}"
    
        
class Seat(models.Model):

    class SeatNumber(models.IntegerChoices):
        SEAT_1 = 1
        SEAT_2 = 2
        SEAT_3 = 3
        SEAT_4 = 4
        SEAT_5 = 5
        SEAT_6 = 6
        SEAT_7 = 7
        SEAT_8 = 8
        SEAT_9 = 9
        SEAT_10 = 10
        SEAT_11 = 11
        SEAT_12 = 12
        SEAT_13 = 13
        SEAT_14 = 14
        SEAT_15 = 15
        SEAT_16 = 16
        SEAT_17 = 17
        SEAT_18 = 18
        SEAT_19 = 19
        SEAT_20 = 20
        SEAT_21 = 21
        SEAT_22 = 22
        SEAT_23 = 23
        SEAT_24 = 24
        SEAT_25 = 25
        SEAT_26 = 26
        SEAT_27 = 27
        SEAT_28 = 28
        SEAT_29 = 29
        SEAT_30 = 30

    seat_number = models.PositiveSmallIntegerField(choices=SeatNumber.choices)
    is_booked = models.BooleanField(default=False)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Seat {self.seat_number} of {self.bus.bus_number}"
    