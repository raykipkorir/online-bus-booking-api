from django.urls import reverse
from rest_framework.test import APITestCase

from inventory.models import Driver, Bus, BusRoute
from tests.utils import authenticate_as_admin, authenticate_as_normal_user


class TestBusesApi(APITestCase):
    """Test Inventory apis"""

    def setUp(self) -> None:
        self.driver = Driver.objects.create(name="Driver1", age=40, phone_number="254729482942")
        self.driver2 = Driver.objects.create(name="Driver2", age=50, phone_number="254729482642")
        self.bus_route = BusRoute.objects.create(
            route="Mombasa-Nairobi",
            vip_cost=1500,
            first_class_cost=1200, 
            business_class_cost=1000
        )
        self.bus = Bus.objects.create(
            driver_id=self.driver.id, 
            route_id=self.bus_route.id, 
            bus_number=100, 
            number_of_seats=30, 
            is_available=True
        )


    def test_retrieve_buses_list(self):
        authenticate_as_admin(self.client)
        response = self.client.get(reverse("buses-list"))

        self.assertEqual(response.status_code, 200)
    
    def test_retrieve_buses_list_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.get(reverse("buses-list"))

        self.assertEqual(response.status_code, 403)
    
    def test_retrieve_buses_list_fail_when_not_authenticated(self):
        response = self.client.get(reverse("buses-list"))

        self.assertEqual(response.status_code, 401)
    
    def test_bus_creation(self):
        authenticate_as_admin(self.client)
        response = self.client.post(
            reverse("buses-list"),
            data={
                "route_id": 1,
                "driver_id": 2, 
                "bus_number": 102, 
                "number_of_seats": 40,
                "is_available": False
            }
        )

        self.assertEqual(response.status_code, 201)
        bus = Bus.objects.get(pk=2)
        self.assertEqual(bus.bus_number, 102)

    def test_bus_creation_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.post(
            reverse("buses-list"),
            data={
                "driver_id": 2,
                "route_id": 1, 
                "bus_number": 102, 
                "number_of_seats": 40,
                "is_available": False
            }
        )

        self.assertEqual(response.status_code, 403)
    
    def test_bus_creation_fail_when_not_authenticated(self):
        response = self.client.post(
            reverse("buses-list"),
            data={
                "driver_id": 2,
                "route_id": 1, 
                "bus_number": 102, 
                "number_of_seats": 40,
                "is_available": False
            }
        )

        self.assertEqual(response.status_code, 401)

    def test_bus_update(self):
        authenticate_as_admin(self.client)
        response = self.client.put(
            reverse("buses-detail", kwargs={"pk": 1}),
            data={
                "driver_id": 2,
                "route_id": 1,
                "bus_number": 102, 
                "number_of_seats": 40,
                "is_available": False
            }
        )

        self.assertEqual(response.status_code, 200)
        bus = Bus.objects.get(pk=1)
        self.assertEqual(bus.bus_number, 102)

    def test_bus_update_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.put(
            reverse("buses-detail", kwargs={"pk": 1}),
            data={
                "driver_id": 1,
                "route_id": 1, 
                "bus_number": 102, 
                "number_of_seats": 40, 
                "is_available": False
            }
        )

        self.assertEqual(response.status_code, 403)
    
    def test_bus_update_fail_when_not_authenticated(self):
        response = self.client.put(
            reverse("buses-detail", kwargs={"pk": 1}),
            data={
                "driver_id": 1,
                "route_id": 1, 
                "bus_number": 102, 
                "number_of_seats": 40, 
                "is_available": False
            }
        )

        self.assertEqual(response.status_code, 401)

    def test_retrieve_bus_by_id(self):
        authenticate_as_admin(self.client)
        response = self.client.get(reverse("buses-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 200)

    def test_retrieve_bus_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.get(reverse("buses-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 403)

    def test_retrieve_bus_fail_when_not_authenticated(self):
        response = self.client.get(reverse("buses-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 401)

    def test_bus_delete(self):
        authenticate_as_admin(self.client)
        response = self.client.delete(reverse("buses-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 204)

    def test_delete_bus_fail_when_authenticated_as_normal_user(self):
        authenticate_as_normal_user(self.client)
        response = self.client.delete(reverse("buses-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 403)

    def test_delete_bus_fail_when_not_authenticated(self):
        response = self.client.delete(reverse("buses-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 401)
