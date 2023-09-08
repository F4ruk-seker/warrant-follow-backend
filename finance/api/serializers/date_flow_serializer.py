from rest_framework import serializers
from finance.models import DateFlowModel


class DateFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateFlowModel
        fields = '__all__'


