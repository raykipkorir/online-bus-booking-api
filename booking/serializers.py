# pylint: disable=E1101

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from inventory.models import Bus, Seat
from inventory.serializers import BusSerializer, SeatsSerializer

from .models import Ticket, TripBus
from .utils import generate_ticket_number

User = get_user_model()


class TripBusSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    class Meta:
        model = TripBus
        fields = ["id", "bus", "travel_date"]

    def validate(self, attrs):
        """
        Check whether bus selected has driver and route and
        also check if it's already scheduled for a trip on the given date
        """
        bus_id = self.context.get("bus_id")

        try:
            bus = Bus.objects.get(id=bus_id)
        except Bus.DoesNotExist as err:
            raise serializers.ValidationError(err)

        if bus.route and bus.driver:
            # check whether bus is already scheduled for a trip on given date
            travel_date = attrs.get("travel_date")
            trip_bus = TripBus.objects.filter(bus=bus, travel_date=travel_date).exists()
            if trip_bus:
                raise serializers.ValidationError("Bus is already scheduled for a trip on the specified date")
            return attrs
        raise serializers.ValidationError("Bus chose must have driver and route selected")


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class TicketSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    trip_bus = TripBusSerializer(read_only=True)
    seat = SeatsSerializer(read_only=True)
    seat_number = serializers.IntegerField(required=True, write_only=True)
    cost = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Ticket
        fields = ["id", "user", "ticket_number", "trip_bus", "seat", "created_at", "seat_number", "cost"]
        read_only_fields = ("ticket_number",)

    def validate(self, attrs):
        """Check whether seat number is already is booked"""
        seat_number = attrs.get("seat_number")
        trip_bus_id = self.context.get("trip_bus_id")
        trip_bus = get_object_or_404(TripBus, id=trip_bus_id)
        query_seat = Seat.objects.filter(seat_number=seat_number, trip_bus=trip_bus).exists()
        if query_seat:
            raise serializers.ValidationError("Seat is already booked")
        return attrs

    def create(self, validated_data):
        seat_number = validated_data.get("seat_number")
        cost = validated_data.get("cost")
        trip_bus_id = self.context.get("trip_bus_id")
        trip_bus = get_object_or_404(TripBus, id=trip_bus_id)
        seat = Seat.objects.create(seat_number=seat_number, is_booked=True, trip_bus=trip_bus)
        max_length = Ticket._meta.get_field("ticket_number").max_length
        ticket_number = generate_ticket_number(max_length)
        ticket = Ticket.objects.create(
            ticket_number=ticket_number,
            cost=cost,
            seat=seat,
            user=self.context.get("request").user,
            trip_bus=trip_bus
        )
        return ticket
