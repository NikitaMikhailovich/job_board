# from django.shortcuts import render

# # Create your views here.
# # 1) Список вакансий (GET), поля: все
# # 1.1) company_id 
# # 1.2) specialization_id
# # 2) Конкретная вакансия (GET), поля: все, кроме(created_at, updated_at)
# # 3) Создание вакансий (POST), поля: все, кроме(created_at, updated_at)
# # 4) Создание компании (POST), поля: 'name', 'city', 'logo', 'information', 'enployee_amount'
from django_filters import rest_framework as filters
from .pagination import VacancyPagination
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response
from board.models import Vacancy, Company
from .serializers import (VacancyListSerializer, VacancySerializer,
                        CompanySerializer, CompanyListSerializer, CompanyCreateSerializer)
from .filters import VacancyFilter

class VacancyViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Vacancy.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VacancyFilter
    pagination_class = VacancyPagination
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VacancySerializer
        return VacancyListSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CompanySerializer
        elif self.action == 'list':
            return CompanyListSerializer
        return CompanyCreateSerializer

    @action(
        methods=['GET'], detail=False
    )
    def my(self, request):
        user = request.user
        my_company = Company.objects.filter(user=user)
        serializer = CompanyListSerializer(my_company, many=True)
        return Response(serializer.data)
    
