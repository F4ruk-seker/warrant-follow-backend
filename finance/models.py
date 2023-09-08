from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


def upper_case(value: str):
    if not value.isupper():
        raise ValidationError(
            "Names are get as a STOCK CODE, must be uppercase",
            params={"value": value}
        )


class StockModel(models.Model):
    name = models.TextField(validators=[upper_case],)
    date_flow = models.ForeignKey('finance.DateFlowModel', on_delete=models.CASCADE, null=True)
    service = models.ForeignKey('finance.SaleServiceModel', on_delete=models.CASCADE, null=True)

    current_price = models.FloatField(default=.0)
    is_blocked = models.BooleanField(default=False)


class StockOwnerModel(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    initial_price = models.FloatField(default=.0)
    purchase_quantity = models.IntegerField(default=0)
    process = models.BooleanField(default=False)
    stock = models.ForeignKey('finance.StockModel', on_delete=models.CASCADE)


class DateFlowModel(models.Model):
    request_start_date = models.DateField(default=None, null=True, blank=True)
    request_end_date = models.DateField(default=None, null=True, blank=True)

    process_start_date = models.DateField(default=None, null=True, blank=True)

    gross_end_date = models.DateField(default=None, null=True, blank=True)


class SaleServiceModel(models.Model):
    name = models.TextField(validators=[upper_case],)

