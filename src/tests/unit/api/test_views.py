"""
1. Тестирование успешной выдачи по api одной компании.

"""
import pytest

from rest_framework.test import APIClient

from board.models import Company, Vacancy, Application



# https://www.django-rest-framework.org/api-guide/testing/#apiclient


@pytest.mark.django_db
def test_retrieve_company(create_company, api_client):
    """
    Тестирование успешной выдачи по api одной компании.
    
    1. Создать компанию в БД
    2. Делаем http запрос 
    3. Проверить статус ответа
    4. Проверить cодержимое ответа
    
    """

    assert Company.objects.count() == 1
    
    # 2
    response = api_client.get(f'/api/v1/companies/{create_company.id}/')
    # 3
    assert response.status_code == 200
    # 4
    response_data = response.data
    
    assert response_data['name'] == create_company.name
    assert response_data['city'] == create_company.city
    assert response_data['enployee_amount'] == create_company.enployee_amount

@pytest.mark.django_db
def test_list_company():
    assert Company.objects.count() == 0

    data = {'name': 'company', 'city': 'Moscow', 'enployee_amount': 100}
    data1 = {'name': 'company1', 'city': 'Perm', 'enployee_amount': 1000}
        

    Company.objects.create(**data)
    Company.objects.create(**data1)
    assert Company.objects.count() == 2
    client = APIClient()
    response = client.get(f'/api/v1/companies/')
    # print(dir(response))
    assert response.status_code == 200
    assert len(response.data['results']) == 2

@pytest.mark.django_db
def test_post_company(auth_client):
    data = {'name': 'obi', 'city': 'Moscow', 'enployee_amount': 100}
    # url_create_user = f'/api/auth/users/'
    # url_create_token = f'/api/auth/token/login/'
    # user_data =  {'username': 'admin', 'password': 'adminnimda123'}

    # token = '2baec92ebb30beec94ef2cb0c3c8e303ac203127'

    # client = APIClient()
    # create_user = client.post(url_create_user, user_data, format='json')
    # method_list = [method for method in dir(create_user) if method.startswith(('_', 'a', 'c')) is False]
    # assert create_user.status_code == 201
    # response_token = client.post(url_create_token, user_data, format='json')
    # assert response_token.status_code == 200
    # token = response_token.data.get('auth_token')
    # client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    response = auth_client.post(f'/api/v1/companies/', data)
    assert response.status_code == 201
    assert Company.objects.filter(**data).exists()

@pytest.mark.django_db
def test_retrieve_vacancy(api_client, create_vacancy, get_vacancy):

    # data = {'title': 'Seller', 'company': create_company}

    # vacancy = Vacancy.objects.create(**data)
    # assert Vacancy.objects.count() == 1

    response = api_client.get(f'/api/v1/vacancies/{create_vacancy.id}/')
    print('hello'*100)
    print(type(response))

    assert response.status_code == 200
    response_data = response.data

    assert response_data['title'] == create_vacancy.title
    
    assert response_data['company'].get('name') == create_vacancy.company.name

@pytest.mark.django_db
def test_post_application(api_client, create_vacancy):

    data = {
        'name': 'new_name',
        'phone': 888,
        'letter': 'hello'
    }

    response = api_client.post(
        f'/api/v1/vacancies/{create_vacancy.id}/send_app/', data
        )
    
    assert response.status_code == 201

    assert response.data.get('name') == data.get('name')
    assert Application.objects.get(vacancy=create_vacancy.id).vacancy == create_vacancy





    


