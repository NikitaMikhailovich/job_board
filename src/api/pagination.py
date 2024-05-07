from rest_framework.pagination import PageNumberPagination
from job_board.settings import VACANCIES_ON_PAGE


class VacancyPagination(PageNumberPagination):
    page_size = VACANCIES_ON_PAGE
