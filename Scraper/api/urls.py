from django.urls import path

from . import views

app_name: str = "scraper_api"

urlpatterns = [
    path('<token>/', views.ScraperView.as_view()),
]

