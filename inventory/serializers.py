from rest_framework import serializers
from .models import Driver, BusRoute, Bus, Seat


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ["name", "age", "phone_number"]


class BusRouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusRoute
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    route = BusRouteSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Bus
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
