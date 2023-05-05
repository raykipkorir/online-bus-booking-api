from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Ticket, BookBus

User = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name"]

class BookBusDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookBus
        fields = ["bus", "travel_date"]

class TicketSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    book_bus = BookBusDetailsSerializer()
    class Meta:
        model = Ticket
        fields = ["ticker_number", "booked_on", "user", "book_bus"]
        