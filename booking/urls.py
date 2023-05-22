from rest_framework_nested import routers
from inventory.urls import bus_router
from .views import TicketViewSet, TripBusViewSet

router = routers.NestedDefaultRouter(bus_router, "buses", lookup="buses")
router.register("trip-bus", TripBusViewSet, basename="trip-bus")

ticket_router = routers.NestedDefaultRouter(router, "trip-bus", lookup="trip_bus")
ticket_router.register("tickets", TicketViewSet, basename="tickets")

urlpatterns = router.urls + ticket_router.urls
