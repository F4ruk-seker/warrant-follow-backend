#
# from django.urls import path
# from .. api import views
#
from django.urls import path

from finance.api import views

app_name: str = "finance_api"
#
urlpatterns = [
    path('stock/', views.StockSearchListView.as_view()),
    path('stock/all/', views.AllStockSearchListView.as_view()),

]