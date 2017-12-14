from rest_framework import serializers

from .models import Order, OrderCourse

class OrderSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('is_paid',)

class OrderCourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = OrderCourse
        fields = '__all__'
