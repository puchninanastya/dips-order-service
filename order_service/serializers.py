from rest_framework import serializers

from .models import Order, OrderCourse

class OrderCourseSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = OrderCourse
        fields = ('course_id',)

class OrderSerializer(serializers.ModelSerializer):
    courses = OrderCourseSerializer(many=True, read_only=True)
    #courses = serializers.SlugRelatedField(many=True, read_only=True, slug_field='course_id')
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'order_date', 'amount', 'is_paid', 'courses')
        read_only_fields = ('is_paid',)
