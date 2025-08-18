import requests
from utils.urls import CREATE_AND_GET_ORDERS_URL
import allure


class TestGetOrdersList:

    @allure.title('Получения списка заказов с сервера')
    @allure.description('Отправка запроса на сервер методом GET')
    def test_get_orders_list(self):
        response = requests.get(CREATE_AND_GET_ORDERS_URL)
        body = response.json()

        assert response.status_code == 200
        assert len(body['orders']) > 0
