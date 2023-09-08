from django.contrib import admin
from . import models

# Register your models here.

# for model in filter(lambda name: name.endswith('Model'), dir(models)):
#     admin.site.register(getattr(models, model))
#


@admin.register(models.ScraperModel)
class ScraperModelAdmin(admin.ModelAdmin):
    readonly_fields = 'token',
    # fields = '__all__'

