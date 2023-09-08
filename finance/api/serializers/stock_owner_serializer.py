from rest_framework import serializers
from finance.models import StockOwnerModel
from .stock_serializer import StockSerializer


class StockOwnerSerializer(serializers.ModelSerializer):
    stock = StockSerializer()

    class Meta:
        model = StockOwnerModel
        fields = '__all__'


