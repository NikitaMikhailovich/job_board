from typing import Any

from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from board.forms import ApplicationForm
from board.models import Application, Company, Specialization, Vacancy
from django.shortcuts import get_object_or_404

from board.constants import COMPANY_ON_PAGE, SPECIALIZATION_ON_PAGE


class IndexView(View):  # noqa: D101
    template_name = 'board/index.html'

    def get(self, request, *args, **kwargs):  # noqa: D102
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):  # noqa: D102
        context = {}
        context['companies'] = Company.objects.all()[:COMPANY_ON_PAGE]
        context['specialization'] = Specialization.objects.all()[:SPECIALIZATION_ON_PAGE]
        return context

    
class VacanciesListView(ListView):
    
    template_name = 'board/vacancies.html'
    model = Vacancy

    def get_queryset(self, *args, **kwargs):
        """
            Params: 
                company_id; /vacancies?company_id=5
                specialization_id; /vacancies?specialization_id=5
        """
        queryset = super().get_queryset(*args, **kwargs)

        query = self.request.GET
        company_id = query.get('company_id')
        specialization_id = query.get('specialization_id')

        if company_id is not None:
            queryset = queryset.filter(company__id=int(company_id))
        if specialization_id is not None:
            queryset = queryset.filter(
                specialization__id=int(specialization_id),
                )

        return queryset


class VacancyView(DetailView):  # noqa: D101
    model = Vacancy
    template_name = 'board/vacancy.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm()
        return context

    def post(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.filter(pk=kwargs.get('pk')).first()
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = vacancy
            application.save()
        return HttpResponseRedirect(request.path_info)


class VacancyCreateView(CreateView):
    model = Vacancy
    template_name = 'board/create_vacancy.html'
    success_url = '/'
    fields = [
        'title', 'company', 'specialization', 'skills',
        'description', 'salary_min', 'salary_max',
    ]


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'board/company_create.html'
    success_url = '/'
    fields = ['name', 'city', 'logo', 'information', 'enployee_amount']
    
    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        user = request.user
        if form.is_valid():
            company = form.save(commit=False)
            company.user = user
            company.save()
        return HttpResponseRedirect(request.path_info)
            

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'board/company.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Company, pk=self.kwargs.get('pk'))


class CompanyListView(ListView):

    model = Company
    template_name = 'board/companies.html'

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        query = self.request.GET
        user = self.request.user
        my_param = query.get('my')
        if my_param is not None:
            queryset = queryset.filter(user=user)
        return queryset


class MyCompanyApplicationView(ListView):

    model = Application
    template_name = 'board/my_company.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        queryset = queryset.filter(vacancy__company__user=user)
        return queryset
