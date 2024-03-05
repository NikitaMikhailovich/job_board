from rest_framework.pagination import PageNumberPagination

class VacancyPagination(PageNumberPagination):
    page_size = 5