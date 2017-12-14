from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('is_paid',)
