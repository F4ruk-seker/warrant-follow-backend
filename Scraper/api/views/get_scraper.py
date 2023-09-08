from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404

from Scraper.models import ScraperModel
from Scraper.serializers import ScraperSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class ScraperThrottle(UserRateThrottle):
    rate = '3/minute'  # for scraper request per 1 minute


class ScraperView(RetrieveAPIView):
    serializer_class = ScraperSerializer
    queryset = ScraperModel.objects.all()
    lookup_field = 'token'
    throttle_classes = [ScraperThrottle, ]

