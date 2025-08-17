import requests
from utils.constants import BASE_URL 
import allure


@allure.title('Получения списка заказов с сервера')
@allure.description('Отправка запроса на сервер методом GET')
def test_get_orders_list():
    response = requests.get(BASE_URL + '/api/v1/orders')
    body = response.json()

    assert response.status_code == 200
    assert len(body['orders']) > 0
