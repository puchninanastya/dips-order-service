from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory

from order_service.models import Order, OrderCourse
from order_service.serializers import OrderSerializer, OrderCourseSerializer
from order_service.views import OrderViewSet

class GetAllOrdersTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newOrder1 = Order.objects.create(
            amount=10000, is_paid=False,
            user_id=2)
        self.newOrder1Course1 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=1)
        self.newOrder1Course2 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=2)
        self.newOrder1Course3 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=3)

        self.newOrder2 = Order.objects.create(
            amount=20000, is_paid=True,
            user_id=2)
        self.newOrder2Course1 = OrderCourse.objects.create(
            order=self.newOrder2, course_id=1)
        self.newOrder2Course2 = OrderCourse.objects.create(
            order=self.newOrder2, course_id=2)
        self.newOrder2Course3 = OrderCourse.objects.create(
            order=self.newOrder2, course_id=3)

    def test_get_all_orders(self):
        """Test the api get orders."""
        # Setup.
        url = "/orders/"
        request = self.factory.get(url)
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        # Run.
        order_list = OrderViewSet.as_view({'get': 'list'})
        response = order_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

class GetSingleOrderTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newOrder1 = Order.objects.create(
            amount=10000, is_paid=False,
            user_id=2)
        self.newOrder1Course1 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=1)
        self.newOrder1Course2 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=2)
        self.newOrder1Course3 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=3)

        self.invalid_pk = 2

    def test_get_valid_single_order(self):
        """Test the api get valid single order."""
        # Setup.
        url = "/orders/" + str(self.newOrder1.pk)
        request = self.factory.get(url)
        serializer = OrderSerializer(self.newOrder1)
        # Run.
        order_detail = OrderViewSet.as_view({'get': 'retrieve'})
        response = order_detail(request, pk=self.newOrder1.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_order(self):
        """Test the api get invalid single order."""
        # Setup.
        url = "/orders/" + str(self.invalid_pk)
        request = self.factory.get(url)
        # Run.
        order_detail = OrderViewSet.as_view({'get': 'retrieve'})
        response = order_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewOrderTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.valid_payload = {
            "user_id": 2,
            "amount": 1000,
            "is_paid": False
        }

        self.invalid_payload = {
            "amount": 7000,
            "is_paid": False
        }

    def test_create_valid_single_order(self):
        """Test the api valid insert new order."""
        # Setup.
        url = "/orders/"
        request = self.factory.post(url, self.valid_payload, format='json')
        # Run.
        order_list = OrderViewSet.as_view({'post': 'create'})
        response = order_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_order(self):
        """Test the api invalid insert new order."""
        # Setup.
        url = "/orders/"
        request = self.factory.post(url, self.invalid_payload, format='json')
        # Run.
        order_list = OrderViewSet.as_view({'post': 'create'})
        response = order_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleOrderTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newOrder1 = Order.objects.create(
            amount=10000, is_paid=False,
            user_id=2)
        self.newOrder1Course1 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=1)
        self.newOrder1Course2 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=2)
        self.newOrder1Course3 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=3)

        self.invalid_pk = 2

    def test_delete_valid_single_order(self):
        """Test the api valid delete new order."""
        # Setup.
        url = "/orders/" + str(self.newOrder1.pk)
        request = self.factory.delete(url)
        # Run.
        order_detail = OrderViewSet.as_view({'delete': 'destroy'})
        response = order_detail(request, pk=self.newOrder1.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_valid_single_order(self):
        """Test the api valid delete new order."""
        # Setup.
        url = "/orders/" + str(self.invalid_pk)
        request = self.factory.delete(url)
        # Run.
        order_detail = OrderViewSet.as_view({'delete': 'destroy'})
        response = order_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
