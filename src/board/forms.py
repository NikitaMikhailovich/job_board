from django.forms import ModelForm

from board.models import Application, Vacancy


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ["name", "phone", "letter"]


class VacancyCreateForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'company', 'specialization', 'skills', 'description', 'salary_min', 'salary_max']
