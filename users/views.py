from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model

from .serializers import AdminUserCreateSerializer

User = get_user_model()

class AdminUserCreateViewSet(CreateModelMixin, GenericViewSet):

    serializer_class = AdminUserCreateSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    