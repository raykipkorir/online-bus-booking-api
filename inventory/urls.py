from rest_framework import routers

from .views import DriverViewSet, BusRouteViewSet, BusViewSet

drivers_router = routers.DefaultRouter()
drivers_router.register("drivers", DriverViewSet, basename="drivers")

routes_router = routers.DefaultRouter()
routes_router.register("routes", BusRouteViewSet, basename="routes")

bus_router = routers.DefaultRouter()
bus_router.register("buses", BusViewSet, basename="buses")

urlpatterns = routes_router.urls + drivers_router.urls + bus_router.urls
