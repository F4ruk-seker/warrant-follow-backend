from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "api"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('account/', include('Account.api.urls', namespace="account_api")),
    path('finance/', include('finance.api.urls', namespace="finance_api")),
    path('scraper/', include('Scraper.api.urls', namespace="scraper_api")),
]

