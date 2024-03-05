from django.forms import ModelForm
from board.models import Application, Vacancy, Company

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ["name", "phone", "letter"]


class VacancyCreateForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'company', 'specialization', 'skills', 'description', 'salary_min', 'salary_max']

# class CompanyCreateForm(ModelForm):
#     class Meta:
#         model = Company
#         fields = '__all__'




