from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import OrderSerializer, OrderCourseSerializer
from .models import Order, OrderCourse

#TODO: Create tests for views

class OrderViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
'''
# orders/{order_id}/courses
class OrderCourseList(APIView):
  def get(self, request, order_id):
    courses = OrderCourse.objects.filter(order.id=order_id)
    serializer = OrderCourseSerializer(courses, many=True)
    return Response(serializer.data)

'''
class OrderCourseViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = OrderCourse.objects.all()
    serializer_class = OrderCourseSerializer

    def get_queryset(self):
        return OrderCourse.objects.filter(order__id=self.kwargs['order_id'])
