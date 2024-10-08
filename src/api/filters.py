from django_filters.rest_framework import FilterSet, filters

from board.models import Vacancy


class VacancyFilter(FilterSet):
    company_id = filters.NumberFilter(field_name="company")
    specialization_id = filters.NumberFilter(field_name="specialization")

    class Meta:
        model = Vacancy
        fields = ['company_id', 'specialization_id']