from django.test import TestCase

from order_service.models import Order, OrderCourse

class OrderModelTestCase(TestCase):
    """This class defines the test suite for the Order model."""

    def setUp(self):
        self.newOrder1 = Order.objects.create(
            amount=10000, is_paid=False,
            user_id=2)

    def test_model_get_order(self):
        """Test the course model can get order."""
        order1 = Order.objects.get(pk=self.newOrder1.id)
        self.assertEqual(order1.amount, 10000)
        self.assertEqual(order1.is_paid, False)
        self.assertEqual(order1.user_id, 2)

class OrderCourseModelTestCase(TestCase):
    """This class defines the test suite for the OrderCourse model."""

    def setUp(self):
        self.newOrder1 = Order.objects.create(
            amount=10000, is_paid=False,
            user_id=2)
        self.newOrderCourse1 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=1)
        self.newOrderCourse2 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=2)
        self.newOrderCourse3 = OrderCourse.objects.create(
            order=self.newOrder1, course_id=3)

    def test_model_get_single_order_course(self):
        """Test the course model can get single order course."""
        orderCourse1 = OrderCourse.objects.get(pk=self.newOrderCourse1.id)
        self.assertEqual(orderCourse1.order.id, self.newOrder1.id)
        self.assertEqual(orderCourse1.course_id, self.newOrderCourse1.course_id)

    def test_model_get_all_order_courses(self):
        """Test the course model can get all order courses."""
        orderCourses = OrderCourse.objects.filter(order_id=self.newOrder1.id)
        self.assertEqual(orderCourses[0].order.id, self.newOrder1.id)
        self.assertEqual(orderCourses[0].course_id, self.newOrderCourse1.course_id)
        self.assertEqual(orderCourses[1].order.id, self.newOrder1.id)
        self.assertEqual(orderCourses[1].course_id, self.newOrderCourse2.course_id)
        self.assertEqual(orderCourses[2].order.id, self.newOrder1.id)
        self.assertEqual(orderCourses[2].course_id, self.newOrderCourse3.course_id)
