from rest_framework import routers

from .views import AdminUserCreateViewSet

admins_router = routers.DefaultRouter()
admins_router.register("admins", AdminUserCreateViewSet, basename="admins")

urlpatterns = admins_router.urls
