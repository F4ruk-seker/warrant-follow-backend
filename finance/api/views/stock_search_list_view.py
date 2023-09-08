from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from finance.api.serializers import StockOwnerSerializer
from finance.models import StockOwnerModel


class StockSearchListView(ListAPIView):
    serializer_class = StockOwnerSerializer
    queryset = StockOwnerModel.objects.all()
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        return StockOwnerModel.objects.filter(
            owner=self.request.user
        ).all()
