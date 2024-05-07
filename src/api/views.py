from django_filters import rest_framework as filters
from .pagination import VacancyPagination
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response
from board.models import Vacancy, Company
from .serializers import (VacancyListSerializer, VacancySerializer,
                          ApplicationSerializer, CompanySerializer,
                          CompanyListSerializer, CompanyCreateSerializer,
                          VacancyCreateSerializer,
                          )
from .filters import VacancyFilter

class VacancyViewSet(viewsets.ModelViewSet):

    queryset = Vacancy.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VacancyFilter
    pagination_class = VacancyPagination
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VacancySerializer
        elif self.action == 'list':
            return VacancyListSerializer
        return VacancyCreateSerializer
    
    @action(
        methods=['POST'], detail=True,
    )
    def response_to_vacancy(self, request, pk):
        vacancy = Vacancy.objects.get(id=pk)
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vacancy=vacancy)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CompanySerializer
        elif self.action == 'list':
            return CompanyListSerializer
        return CompanyCreateSerializer

    @action(
        methods=['GET'], detail=False,
    )
    def my(self, request):
        my_company = Company.objects.filter(user=request.user)
        serializer = CompanyListSerializer(my_company, many=True)
        return Response(serializer.data)
