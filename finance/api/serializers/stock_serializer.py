from rest_framework import serializers
from finance.models import StockModel
from .date_flow_serializer import DateFlowSerializer


class StockSerializer(serializers.ModelSerializer):
    date_flow = DateFlowSerializer()

    class Meta:
        model = StockModel
        fields = '__all__'


