from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import OrderSerializer, OrderCourseSerializer
from .models import Order, OrderCourse

#TODO: Create tests for views
#TODO: delete filter app

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
