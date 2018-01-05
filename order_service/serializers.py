from rest_framework import serializers
from rest_framework import exceptions

from .models import Order, OrderCourse

class OrderCourseSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = OrderCourse
        fields = ('course_id',)

class OrderSerializer(serializers.ModelSerializer):
    courses = OrderCourseSerializer(many=True)
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'order_date', 'amount', 'is_paid', 'courses')

    def create(self, validated_data):
        order_courses_data = validated_data.pop('courses')
        order = Order.objects.create(**validated_data)
        if order is not None:
            order.save()
        for order_course_data in order_courses_data:
            OrderCourse.objects.create(order=order, **order_course_data)
        return order

    def update(self, instance, validated_data):
        order_courses_data = validated_data.pop('courses', None)
        order_courses = (instance.courses).all()
        order_courses = list(order_courses)

        # retrieve the Order
        instance.user = validated_data.get('user', instance.user)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.amount = validated_data.get('amount', instance.amount)

        # check payment status to set 'is_paid' field
        # query string ?paid={num} need to be equal to order amount
        request = self.context.get("request")
        is_paid_data = validated_data.pop('is_paid', instance.is_paid)
        if is_paid_data is True:
            amount_paid_data = self.context['request'].query_params.get('paid', None)
            if (amount_paid_data is not None) and (int(amount_paid_data) == instance.amount):
                instance.is_paid = True
            else:
                raise exceptions.ValidationError()
        else:
            instance.is_paid = False

        instance.save()

        # retrieve the OrderCourses if exists 'courses'
        if order_courses_data is not None:
            for order_course in order_courses:
                order_course.delete()
            for order_course_data in order_courses_data:
                OrderCourse.objects.create(order=instance, **order_course_data)

        return instance
