from django.urls import reverse
from rest_framework.test import APITestCase

from inventory.models import Driver
from tests.utils import authenticate_as_admin, authenticate_as_normal_user


class TestDriversApi(APITestCase):
    """Test Inventory apis"""

    def setUp(self) -> None:
        Driver.objects.create(name="Driver1", age=40, phone_number="254729482942")

    def test_retrieve_drivers_list(self):
        authenticate_as_admin(self.client)
        response = self.client.get(reverse("drivers-list"))

        self.assertEqual(response.status_code, 200)
    
    def test_retrieve_drivers_list_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.get(reverse("drivers-list"))

        self.assertEqual(response.status_code, 403)
    
    def test_retrieve_drivers_list_fail_when_not_authenticated(self):
        response = self.client.get(reverse("drivers-list"))

        self.assertEqual(response.status_code, 401)

    def test_driver_creation(self):
        authenticate_as_admin(self.client)
        response = self.client.post(
            reverse("drivers-list"),
            data={"name": "Driver1", "age": 30, "phone_number": "254782949823"}
        )

        self.assertEqual(response.status_code, 201)
        driver = Driver.objects.get(pk=1)
        self.assertEqual(driver.name, "Driver1")

    def test_driver_creation_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.post(
            reverse("drivers-list"),
            data={"name": "Driver1", "age": 30, "phone_number": "254782949823"}
        )

        self.assertEqual(response.status_code, 403)
    
    def test_driver_creation_fail_when_not_authenticated(self):
        response = self.client.post(
            reverse("drivers-list"),
            data={"name": "Driver1", "age": 30, "phone_number": "254782949823"}
        )

        self.assertEqual(response.status_code, 401)

    def test_driver_update(self):
        authenticate_as_admin(self.client)
        response = self.client.put(
            reverse("drivers-detail", kwargs={"pk": 1}),
            data={"name": "UpdatedDriver", "age": 30, "phone_number": "254782949823"}
        )

        self.assertEqual(response.status_code, 200)
        driver = Driver.objects.get(pk=1)
        self.assertEqual(driver.name, "UpdatedDriver")

    def test_driver_update_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.put(
            reverse("drivers-detail", kwargs={"pk": 1}),
            data={"name": "Driver1", "age": 30, "phone_number": "254782949823"}
        )

        self.assertEqual(response.status_code, 403)
    
    def test_driver_update_fail_when_not_authenticated(self):
        response = self.client.put(
            reverse("drivers-detail", kwargs={"pk": 1}),
            data={"name": "Driver1", "age": 30, "phone_number": "254782949823"}
        )

        self.assertEqual(response.status_code, 401)

    def test_retrieve_driver_by_id(self):
        authenticate_as_admin(self.client)
        response = self.client.get(reverse("drivers-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 200)

    def test_retrieve_driver_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.get(reverse("drivers-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 403)

    def test_retrieve_driver_fail_when_not_authenticated(self):
        response = self.client.get(reverse("drivers-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 401)

    def test_driver_delete(self):
        authenticate_as_admin(self.client)
        response = self.client.delete(reverse("drivers-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 204)

    def test_delete_driver_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.delete(reverse("drivers-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 403)

    def test_delete_driver_fail_when_not_authenticated(self):
        response = self.client.delete(reverse("drivers-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 401)
