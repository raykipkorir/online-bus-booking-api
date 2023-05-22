# pylint: disable=E1101

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Bus, BusRoute, Driver, Seat


class DriverSerializer(serializers.ModelSerializer):
    """Serializer Driver crud operations"""

    class Meta:
        model = Driver
        fields = ["id", "name", "age", "phone_number"]


class BusRouteSerializer(serializers.ModelSerializer):
    """Serialize BusRoute crud operations"""

    class Meta:
        model = BusRoute
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    """Serialize Bus crud operations"""
    route = BusRouteSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)
    route_id = serializers.IntegerField(write_only=True, required=True)
    driver_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Bus
        fields = "__all__"

    def validate_driver_id(self, value):
        """Check whether driver chose has already been assigned a bus"""
        driver = get_object_or_404(Driver, id=value)
        bus = Bus.objects.filter(driver=driver).exists()
        if bus:
            raise serializers.ValidationError("Driver has already been assigned a bus")
        return value

    def update(self, instance, validated_data):
        route = BusRoute.objects.get(id=validated_data.get("route_id", instance.route.id))
        driver = Driver.objects.get(id=validated_data.get("driver_id", instance.driver.id))
        instance.bus_number = validated_data.get("bus_number", instance.bus_number)
        instance.number_of_seats = validated_data.get("number_of_seats", instance.number_of_seats)
        instance.is_available = validated_data.get("is_available", instance.is_available)
        instance.route = route
        instance.driver = driver
        instance.save()
        return instance

class SeatsSerializer(serializers.ModelSerializer):
    """Serializer seat crud operations"""

    class Meta:
        model = Seat
        fields = "__all__"
