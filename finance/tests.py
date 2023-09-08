from datetime import datetime, timedelta

from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from dataclasses import dataclass
from django.contrib.auth.models import User
from finance.models import StockModel, StockOwnerModel, SaleServiceModel, DateFlowModel
import random


@dataclass
class UserModel:
    username: str
    password: str


TEST_USER_FIRST: UserModel = UserModel(username='TestUserFirst', password='TestUserPasswordV1234!')
TEST_USER_SECOND: UserModel = UserModel(username='TestUserSecond', password='TestUserPasswordV1234!')

TEST_USER_LIST = [
    TEST_USER_FIRST, TEST_USER_SECOND
]


def create_current_date(day=0):
    current_date = datetime.now().date()
    if day == 0:
        return current_date
    return current_date + timedelta(days=day)


class GetJustOwnerStock(APITestCase):

    def setUp(self) -> None:
        for test_user in TEST_USER_LIST:
            user = User.objects.create_user(
                username=test_user.username,
                password=test_user.password
            )
            StockOwnerModel.objects.create(
                owner=user,
                stock=StockModel.objects.create(
                    service=SaleServiceModel.objects.create(name='IST'),
                    name=random.choice(['test s', 'echo s', 'json s']),
                    is_blocked=random.randint(0, 1),
                    date_flow=DateFlowModel.objects.create(
                        gross_end_date=create_current_date(10),
                        request_end_date=create_current_date(),
                        process_start_date=create_current_date(),
                        request_start_date=create_current_date()
                    ),
                    current_price=float(f"{random.randint(1,100)}.{random.randint(0, 99)}")
                ),
                purchase_quantity=random.randint(0, 100),
                initial_price=float(f"{random.randint(1,100)}.{random.randint(0, 99)}"),
                process=random.randint(0, 1),
            )

    def test_get_just_owner_stock(self):
        owen_stock_id_list = [stock.id for stock in StockOwnerModel.objects.filter(owner_id=1).all()]

        self.client.login(**TEST_USER_FIRST.__dict__)
        if response := self.client.get('/api/finance/stock/'):
            for owen_stock in response.json():
                self.assertIn(owen_stock.get('id'), owen_stock_id_list)

    def test_get_just_not_owner_stock(self):
        owen_stock_id_list = [stock.id for stock in StockOwnerModel.objects.filter(owner_id=2).all()]

        self.client.login(**TEST_USER_FIRST.__dict__)
        if response := self.client.get('/api/finance/stock/'):
            for owen_stock in response.json():
                self.assertNotIn(owen_stock.get('id'), owen_stock_id_list)

