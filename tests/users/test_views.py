from django.urls import reverse
from rest_framework.test import APITestCase

from tests.utils import authenticate_as_admin, authenticate_as_normal_user
from users.models import User


class TestUsersApi(APITestCase):
    """Tests for users api"""

    def test_admin_creation(self):
        """Test admin creation"""
        authenticate_as_admin(self.client)
        response = self.client.post(
            reverse("admins-list"),
            data={
                "first_name": "Admin2",
                "last_name": "Admin2",
                "email": "admin2@gmail.com",
                "phone_number": "254700000008",
                "password": "admin",
                "re_password": "admin"
            }
        )

        self.assertEqual(response.status_code, 201)

    def test_admin_creation_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.post(
            reverse("admins-list"),
            data={
                "first_name": "System",
                "last_name": "Admin",
                "email": "admin@gmail.com",
                "phone_number": "254700000008",
                "password": "admin",
                "re_password": "admin"
            }
        )

        self.assertEqual(response.status_code, 403)
    
    def test_admin_creation_when_not_authenticated(self):
        response = self.client.post(
            reverse("admins-list"),
            data={
                "first_name": "System",
                "last_name": "Admin",
                "email": "admin@gmail.com",
                "phone_number": "254700000008",
                "password": "admin",
                "re_password": "admin"
            }
        )

        self.assertEqual(response.status_code, 401)

    def test_retrieve_all_admins(self):
        authenticate_as_admin(self.client)
        response = self.client.get(reverse("admins-list"))

        self.assertEqual(response.status_code, 200)

    def test_retrieve_admins_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.get(reverse("admins-list"))

        self.assertEqual(response.status_code, 403)

    def test_retrieve_admins_fail_when_not_authenticated(self):
        response = self.client.get(reverse("admins-list"))

        self.assertEqual(response.status_code, 401)
    
    def test_retrieve_admin_by_id(self):
        authenticate_as_admin(self.client)
        response = self.client.get(reverse("admins-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 200)

    def test_retrieve_admin_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.get(reverse("admins-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 403)

    def test_retrieve_admin_fail_when_not_authenticated(self):
        response = self.client.get(reverse("admins-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 401)

    def test_admin_update(self):
        authenticate_as_admin(self.client)
        response = self.client.put(
            reverse("admins-detail", kwargs={"pk": 1}),
            data={
                "first_name": "System",
                "last_name": "Admin",
                "email": "systemadmin@gmail.com",
                "phone_number": "254700000608",
                "password": "admin",
                "re_password": "admin"
            }
        )

        self.assertEqual(response.status_code, 200)
        admin1 = User.objects.get(id=1)
        self.assertEqual(admin1.first_name, "System")
        self.assertEqual(admin1.email, "systemadmin@gmail.com")

    def test_admin_update_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.put(
            reverse("admins-detail", kwargs={"pk": 1}),
            data={
                "first_name": "System",
                "last_name": "Admin",
                "email": "systemadmin@gmail.com",
                "phone_number": "254700000608",
                "password": "admin",
                "re_password": "admin"
            }
        )

        self.assertEqual(response.status_code, 403)

    def test_admin_update_fail_when_not_authenticated(self):
        response = self.client.put(
            reverse("admins-detail", kwargs={"pk": 1}),
            data={
                "first_name": "System",
                "last_name": "Admin",
                "email": "systemadmin@gmail.com",
                "phone_number": "254700000608",
                "password": "admin",
                "re_password": "admin"
            }
        )

        self.assertEqual(response.status_code, 401)

    def test_admin_delete(self):
        authenticate_as_admin(self.client)
        response = self.client.delete(reverse("admins-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 204)

    def test_delete_admin_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.delete(reverse("admins-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 403)

    def test_delete_admin_fail_when_not_authenticated(self):
        response = self.client.delete(reverse("admins-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 401)
