from rest_framework import routers

from .views import AdminUserViewSet

admins_router = routers.DefaultRouter()
admins_router.register("admins", AdminUserViewSet, basename="admins")

urlpatterns = admins_router.urls
