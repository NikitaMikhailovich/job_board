from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet, CompanyViewSet

app_name = 'api'
router = DefaultRouter()


router.register('vacancies', VacancyViewSet, basename='vacancies')
router.register('companies', CompanyViewSet, basename='companies')

api_v1 = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('v1/', include(api_v1)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]