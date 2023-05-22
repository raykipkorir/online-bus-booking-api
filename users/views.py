from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import AdminUserSerializer

User = get_user_model()

class AdminUserViewSet(ModelViewSet):

    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(is_superuser=True)
