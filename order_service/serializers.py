from rest_framework import serializers

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

        #retrieve the Order
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if order_courses_data is not None:
            for order_course in order_courses:
                order_course.delete()
            #retrieve the OrderCourses
            for order_course_data in order_courses_data:
                OrderCourse.objects.create(order=instance, **order_course_data)

        return instance
