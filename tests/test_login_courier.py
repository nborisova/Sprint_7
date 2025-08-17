import requests
from utils.constants import BASE_URL
from utils.generate_courier_data import register_new_courier_and_return_login_password 
import allure

@allure.title('Возможность курьеру залогиниться с валидными данными')
@allure.description('Отправка валидных данных на сервер методом POST')
def test_login_courier_with_valid_data():
    login, password, first_name = register_new_courier_and_return_login_password()

    response = requests.post(BASE_URL + '/api/v1/courier/login', data={'login': login, 'password': password})

    assert response.status_code == 200
    assert 'id' in response.json()

@allure.title('Невозможность залогиниться без заполнения одного из обязательных полей')
@allure.description('Отправка только логина на сервер методом POST')
def test_login_courier_without_password():
    login, password, first_name = register_new_courier_and_return_login_password()

    response = requests.post(BASE_URL + '/api/v1/courier/login', data={'login': login, 'password': ''})

    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для входа'

@allure.title('Невозможность залогиниться несуществующим пользователем')
@allure.description('Отправка несуществующих данных на сервер методом POST')
def test_login_courier_with_invalid_data():
    response = requests.post(BASE_URL + '/api/v1/courier/login', data={'login': 'login', 'password': 'password'})

    assert response.status_code == 404
    assert response.json()['message'] == 'Учетная запись не найдена'
