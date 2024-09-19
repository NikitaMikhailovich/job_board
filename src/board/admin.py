from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.http.request import HttpRequest

from .models import Application, Company, Specialization, Vacancy


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    fields = (
        'name',
        'logo',
    )
    list_filter = (
        'name',
    )

    def has_change_permission(self, *args, **kwargs) -> bool:
        return True

    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False
    

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'city',
        'enployee_amount',
    )
    search_fields = (
        'name',
    )
    # fields = (
    #     'name',
    #     'logo',
    # )
    list_filter = (
        'city',
    )
    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'specialization',
        'salary_min',
        'salary_max',
    )
    search_fields = (
        'title',
        'company__name',
        'specialization__name',
    )
    fields = (
        'title',
        'company',
        'specialization',
        'salary_min',
        'salary_max',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    list_filter = (
        'company',
    )
@admin.register(Application)
class VacancyAdmin(admin.ModelAdmin):
    pass


class CompanyInline(admin.TabularInline):
    model = Company
    fields = (
        'name',
    )


class UserAdmin(UserAdmin):
    inlines = [CompanyInline]
    # list_select_related = ('companies',)
    # fieldsets = ('companies',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)