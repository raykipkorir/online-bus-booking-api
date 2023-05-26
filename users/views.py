from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import AdminUserSerializer

User = get_user_model()

class AdminUserViewSet(ModelViewSet):
    """Admin"""
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = User.objects.filter(is_superuser=True)
