from django.urls import include, path

from . import views

app_name = 'board'

vacancy_patterns = [
    path('', views.VacanciesListView.as_view(), name='vacancies'),
    path('<int:pk>', views.VacancyView.as_view(), name='vacancy'),
    path('create', views.VacancyCreateView.as_view(), name='create'), 
]

company_patterns = [
    path('create', views.CompanyCreateView.as_view(), name='create_company'),
    path('<int:pk>', views.CompanyDetailView.as_view(), name='company'),
    path('', views.CompanyListView.as_view(), name='companies'),
]
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vacancy/', include(vacancy_patterns)),
    path('company/', include(company_patterns)),
    path('my_vacancy_responses', views.MyCompanyApplicationView.as_view(), name='apps'),
]
