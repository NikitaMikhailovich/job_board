from django.urls import include, path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vacancies', views.VacanciesListView.as_view(), name='vacancies'),
    path('vacancy/<int:pk>', views.VacancyView.as_view(), name='vacancy'),
    path('vacancy/create', views.VacancyCreateView.as_view(), name='create'),
    path('company/create', views.CompanyCreateView.as_view(), name='create_company'),
    path('company/<int:pk>', views.CompanyView.as_view(), name='company'),
    path('companies', views.CompaniesView.as_view(), name='companies'),
    path('myapp', views.MyCompanyApplicationView.as_view(), name='apps'),
]
