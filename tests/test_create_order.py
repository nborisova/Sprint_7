import requests
from utils.urls import CREATE_AND_GET_ORDERS_URL
from utils.data import create_order_data
import pytest
import allure


class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цветов самоката и без его указания')
    @allure.description('Отправка набора данных на сервер методом POST')
    @pytest.mark.parametrize('order_data', create_order_data)
    def test_create_order(self, order_data):
        response = requests.post(CREATE_AND_GET_ORDERS_URL, json=order_data)

        assert response.status_code == 201
        assert 'track' in response.json()
