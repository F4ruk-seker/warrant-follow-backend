from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from finance.api.serializers import StockSerializer
from finance.models import StockModel


class AllStockSearchListView(ListAPIView):
    serializer_class = StockSerializer
    queryset = StockModel.objects.all()
    permission_classes = [
        IsAuthenticated
    ]

