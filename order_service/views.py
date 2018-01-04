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

class UserOrderList(APIView):
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            userId = kwargs.get('user_id', None)
            if userId is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            queryset = Order.objects.filter(user=userId)
            if queryset.exists():
                '''
                # TODO: Pagination. DJANGO REST has no pagination for API Views
                page = paginate_queryset(queryset)
                if page is not None:
                    serializer = OrderSerializer(page, many=True)
                    return get_paginated_response(serializer.data)
                '''

                serializer = OrderSerializer(queryset, many=True)
                return Response(serializer.data)

            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            userId = kwargs['user_id']
            queryset = Order.objects.filter(user=userId)

            if queryset.exists():
                for instance in queryset:
                    instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
