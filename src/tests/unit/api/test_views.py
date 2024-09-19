"""
1. Тестирование успешной выдачи по api одной компании.

"""
import pytest
from rest_framework.test import APIClient

from board.models import Application, Company, Vacancy


@pytest.mark.django_db
def test_retrieve_company(create_company, api_client):
    """
    Тестирование успешной выдачи по api одной компании.

    """

    assert Company.objects.count() == 1
    response = api_client.get(f'/api/v1/companies/{create_company.id}/')
    assert response.status_code == 200
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
    assert response.status_code == 200
    assert len(response.data['results']) == 2


@pytest.mark.django_db
def test_post_company(auth_client):
    data = {'name': 'obi', 'city': 'Moscow', 'enployee_amount': 100}
    response = auth_client.post(f'/api/v1/companies/', data)
    assert response.status_code == 201
    assert Company.objects.filter(**data).exists()


@pytest.mark.django_db
def test_retrieve_vacancy(api_client, create_vacancy):

    response = api_client.get(f'/api/v1/vacancies/{create_vacancy.id}/')
    assert response.status_code == 200
    response_data = response.data

    assert response_data['title'] == create_vacancy.title
    
    assert response_data['company'].get('name') == create_vacancy.company.name


@pytest.mark.django_db
def test_list_vacancy(api_client, create_list_vacancy):
    titles = ['Python Developer', 'Manager']
    assert Vacancy.objects.count() == 2
    response = api_client.get(f'/api/v1/vacancies/')
    assert response.status_code == 200
    response_data = response.data.get('results')
    for i in range(len(response_data)):
        # assert response_data[i].get('title') == titles[i]
        assert response_data[i].get('title') in create_list_vacancy.get('title') # нужно из create_list_vacancy досттаь title



@pytest.mark.django_db
def test_post_vacancy(vacancy_data, auth_client):
    assert Vacancy.objects.count() == 0
    response = auth_client.post(f'/api/v1/vacancies/', vacancy_data)
    print(response.data)
    assert response.status_code == 201
    assert response.data.get('title') == vacancy_data.get('title')



@pytest.mark.django_db
def test_post_application(api_client, create_vacancy):

    data = {
        'name': 'new_name',
        'phone': 888,
        'letter': 'hello'
    }

    response = api_client.post(
        f'/api/v1/vacancies/{create_vacancy.id}/response_to_vacancy/', data
        )
    
    assert response.status_code == 201

    assert response.data.get('name') == data.get('name')
    assert Application.objects.get(vacancy=create_vacancy.id).vacancy == create_vacancy
