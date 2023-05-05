import pytest
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()


# @pytest.mark.django_db
# def test_driver_viewset():
#     payload = {
#         "name": "Driver John",
#         "age": 40,
#         "phone_number": "07000000099"
#     }
#     response = client.post(reverse("drivers-list"), payload)

#     data = response.data

#     assert response.status_code == 201
#     assert data["name"] == payload["name"]
#     assert data["age"] == payload["age"]
#     assert data["phone_number"] == payload["name"]