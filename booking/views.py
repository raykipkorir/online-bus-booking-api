# pylint: disable=E1101

from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from inventory.models import Bus, BusRoute
from inventory.serializers import BusRouteSerializer

from .models import Ticket, TripBus
from .serializers import TicketSerializer, TripBusSerializer


class TripBusViewSet(viewsets.ModelViewSet):
    serializer_class = TripBusSerializer
    queryset = TripBus.objects.all()

    def get_permissions(self):
        if self.action in ("retrieve", "list") and self.request.query_params:
            self.permission_classes = [AllowAny]
        elif self.action in ("create", "list", "update", "destroy"):
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def get_serializer_context(self):
        context =  super().get_serializer_context()
        context["bus_id"] = self.kwargs.get("buses_pk")
        return context

    def perform_create(self, serializer):
        bus = Bus.objects.get(id=self.kwargs["buses_pk"])
        return serializer.save(bus=bus)

    def list(self, request, *args, **kwargs):
        if self.request.query_params:
            trip_buses, route = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(trip_buses, many=True)
            route_serializer = BusRouteSerializer(route)
            return Response({"trip_buses": serializer.data, "route": route_serializer.data})
        return super().list(request=request, *args, **kwargs)

    def get_queryset(self):
        if self.request.query_params:
            travelling_from = self.request.query_params.get("from")
            travelling_to = self.request.query_params.get("to")
            travel_date = self.request.query_params.get("travel_date")
            return_date = self.request.query_params.get("return_date")
            if travelling_from and travelling_to and travelling_to:
                route = "-".join([travelling_from.title(), travelling_to.title()])
                route = get_object_or_404(BusRoute, route=route)
                travel_date = travel_date.split("-")
                travel_date = list(map(int, travel_date))
                trip_buses = get_list_or_404(
                    TripBus,
                    bus__route=route,
                    travel_date__year=travel_date[0],
                    travel_date__month=travel_date[1],
                    travel_date__day=travel_date[2]
                )
                return trip_buses, route
        return super().get_queryset()


# book ticket view
class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_permissions(self):
        if self.action in ("retrieve", "create"):
            self.permission_classes = [IsAuthenticated]
        elif self.action in ("list", "update", "destroy"):
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["trip_bus_id"] = self.kwargs["trip_bus_pk"]
        return context

    def get_queryset(self):
        """Get all tickets for a certain trip"""
        trip_bus_id = self.kwargs["trip_bus_pk"]
        trip_bus = get_object_or_404(TripBus, id=trip_bus_id)
        ticket = Ticket.objects.filter(trip_bus=trip_bus)
        return ticket
