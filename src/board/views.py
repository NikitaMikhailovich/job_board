from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from board.models import Specialization, Company, Vacancy, Application

from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from board.forms import ApplicationForm, VacancyCreateForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# https://github.com/django/django/blob/main/django/views/generic/base.py#L36

# def index(request, *args, **kwargs):
#     template = 'board/index.html'
    # context = {
    #     'specialization' : Specialization.objects.all(),
    #     'company' : Company.objects.all(),
    # }
#     return render(request, template, context)



class IndexView(View):
    template_name = 'board/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        # print(self)
        # print(self.__dict__)
        # print(dir(self))
        # print(request)
        # print(request.__dict__)
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        # context = super().get_context_data(*args, **kwargs)
        # company = Company.objects.all()
        context = {}
        context['companies'] = Company.objects.all()[:8]
        context['spec'] = Specialization.objects.all()[:4]
        # vac_amount = company.vacancies
        return context

# id = self.kwargs['id']: можно ли было так?, так как с усл-м value в таком случае
# в каком случае нам пришлось бы применять метод get context data()
# вопрос по поводу наследования: в случае чего мы не применили бы super().
# отличие queryset от модели
# сейчас возврвщает object_list c параметрами queryset, а что будет если я применю метод get context data, котор тоже возвращает...
# вопрос с path
# разные шаблоны в одном view
# class VacancySpecView(ListView):
#     """Вакансии в определенной специализации."""

#     template_name = 'board/vacancy_spec.html'

#     model = Vacancy
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset(*args, **kwargs)
#         _, _, _, id, _ = self.request.path.split('/') # vacancy/specialization/<int:id>/  vacancy/company/<int:id>/
#         id = int(id)
#         queryset = queryset.filter(specialization__id=id)
#         print(id)
#         print(queryset)
        
#         return queryset
    
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

        params = self.request.GET
        company_id = params.get('company_id')
        specialization_id = params.get('specialization_id')

        if company_id is not None:
            queryset = queryset.filter(company__id=int(company_id))
        if specialization_id is not None:
            queryset = queryset.filter(
                specialization__id=int(specialization_id),
                )

        return queryset


class VacancyView(DetailView):
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
    # form_class = VacancyCreateForm
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
        #username = self.request.user
        # print(request)
        # print(args)
        # print(kwargs)
        # print(self)
        # print(self.__dict__)
        # print(dir(self))
        # print(request.__dict__)
        # print(dir(request))
        print(self.get_form())
        print(self.get_form_class())
        # form_class = self.get_form_class()
        # form = form_class(request.POST)
        form = self.get_form_class()(request.POST)
        user = request.user
        if form.is_valid():
            company = form.save(commit=False)
            company.user = user
            company.save()
        return HttpResponseRedirect(request.path_info)
            

class CompanyView(DetailView):
    model = Company
    template_name = 'board/company.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Company.objects.get(pk=pk)


class CompaniesView(ListView):

    model = Company
    template_name = 'board/companies.html'

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        param = self.request.GET
        user = self.request.user
        my_param = param.get('my')
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




    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # return super().get_context_data(**kwargs)
            


# class VacancyListView(ListView):
#     template_name = ...
#     queryset = Vacancy.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['company'] = Company.objects.all()
    #     return context

# view которая выдает одну вакансиб по id 

# def index(request, vacancy_id, *args, **kwargs):
#     template = 'board/index.html'
#     context = {
#         'vacancy' : get_object_or_404(Vacancy, pk=vacancy_id),
#     }
#     return render(request, template, context)


# class VacancyDetailView(DetailView):
#     template_name = ...
#     queryset = Vacancy.objects.all()

# https://github.com/django/django/blob/main/django/views/generic/detail.py#L174

# class SpecializationList(View)


# copmanies = Company.objects.all()[:4]
# response = {}
# for company in copmanies:
#     response[company.name] = {
#         'name': company.name,
#         'url': company.logo.url,
#         'count': company.vacancies.count(),
#     }