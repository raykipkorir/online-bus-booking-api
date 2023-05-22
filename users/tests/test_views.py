# import pytest
# from django.urls import reverse
# from rest_framework.test import APIClient


# @pytest.mark.django_db
# def test_admin_create_viewset(admin_client):
#     payload = {
#         "first_name": "New",
#         "last_name": "Admin",
#         "email": "admin@gmail.com",
#         "password": "testing321"
#     }
#     response = admin_client.post(reverse("admins-list"), payload)

#     assert response.status_code == 201
