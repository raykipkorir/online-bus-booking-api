# pylint: disable=E1101

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Bus, BusRoute, Driver
from .serializers import BusRouteSerializer, BusSerializer, DriverSerializer


class DriverViewSet(ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    permission_classes = [IsAdminUser]


class BusRouteViewSet(ModelViewSet):
    serializer_class = BusRouteSerializer
    queryset = BusRoute.objects.all()
    permission_classes = [IsAdminUser]


class BusViewSet(ModelViewSet):
    serializer_class = BusSerializer
    queryset = Bus.objects.all()
    permission_classes = [IsAdminUser]
