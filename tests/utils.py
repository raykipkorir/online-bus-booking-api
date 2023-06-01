from django.urls import reverse

from users.models import User


def authenticate_as_admin(client) -> None:
    """Admin authentication"""
    User.objects.create_superuser(
        first_name="Admin1",
        last_name="Admin1",
        email="admin1@gmail.com",
        phone_number="254799999998",
        password="testing321"
    )

    response = client.post(
        reverse("token_obtain_pair"),
        data={"email": "admin1@gmail.com", "password": "testing321"}
    )
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.json()['access']}")

def authenticate_as_normal_user(client) -> None:
    """Authenticating as normal user"""
    User.objects.create_user(
        first_name="Normal",
        last_name="User",
        email="normaluser@email.com",
        phone_number="254799999988",
        password="testing321"
    )
    response = client.post(
        reverse("token_obtain_pair"),
        data={"email": "normaluser@email.com", "password": "testing321"}
    )
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.json()['access']}")
