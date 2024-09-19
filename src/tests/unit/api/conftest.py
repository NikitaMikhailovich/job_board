import pytest
from rest_framework.test import APIClient

from board.models import Company, Vacancy


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def user_data():
    return {'username': 'admin', 'password': 'adminnimda123'}

@pytest.fixture()
def vacancy_data(create_company):
    return {'title': 'Product Manager', 'company': 1}

@pytest.fixture()
def vacancy_list_data(create_company):
    return [
        {'title': 'Python Developer', 'company': create_company},
        {'title': 'Manager', 'company': create_company}
    ]


@pytest.fixture()
def create_user(api_client, user_data):
    url_create_user = f'/api/auth/users/'
    api_client.post(url_create_user, user_data, format='json')

@pytest.fixture()
def user_auth_token(api_client, create_user, user_data):
    url_create_token = f'/api/auth/token/login/'
    response_token = api_client.post(url_create_token, user_data, format='json')
    return response_token.data.get('auth_token')


@pytest.fixture()
def auth_client(api_client, user_auth_token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {user_auth_token}')
    return api_client


@pytest.fixture()
def create_company():

    data = {'name': 'company', 'city': 'Moscow', 'enployee_amount': 100}
    company = Company.objects.create(**data)
    return company


@pytest.fixture()
def create_vacancy(create_company):
    
    data = {'title': 'Seller', 'company': create_company}
    vacancy = Vacancy.objects.create(**data)
    return vacancy


@pytest.fixture()
def create_list_vacancy(vacancy_list_data):
    vacancies = []
    for vacancy in vacancy_list_data:
        create_vacancy = Vacancy.objects.create(**vacancy)
        vacancies.append(create_vacancy)
    return vacancies


@pytest.fixture()
def get_vacancy(api_client, create_vacancy):
    response = api_client.get(f'/api/v1/vacancies/{create_vacancy.id}/')
    return response
