from rest_framework import serializers
from Scraper.models import ScraperModel


class ScraperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScraperModel
        fields = '__all__'

