from rest_framework.serializers import ModelSerializer, ReadOnlyField
from board.models import Vacancy, Company, Application


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'salary_min',
            'salary_max',
            'created_at',
        )

class CompanyInVacancySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'name',
        )


class VacancySerializer(ModelSerializer):
    company = CompanyInVacancySerializer(read_only=True)
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'specialization',
            'company',
            'skills',
            'description',
            'salary_min',
            'salary_max',
            'created_at',
            'updated_at'
        )


class CompanyListSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'name',
            'city',
            'enployee_amount'
        )

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyCreateSerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'user',
            'name',
            'city',
            'logo',
            'information',
            'enployee_amount',
        )

    def create(self, validated_data):
        author = self.context['request'].user # context - это словарь, значенеи по ключу request это ОБЬЕКТ запрос(это каклй то экземпляр класса) и user это атрибут экземпляра класса
        validated_data['user'] = author
        company = Company.objects.create(**validated_data)
        return company


class ApplicationVacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'company',
            'specialization'
        )


class ApplicationSerializer(ModelSerializer):
    # vacancy = ApplicationVacancySerializer(read_only=True)
    vacancy_name = ReadOnlyField(source='vacancy.title')
    class Meta:
        model = Application
        fields = (
            'name',
            'phone',
            'letter',
            'vacancy',
            'vacancy_name'
        )
        # read_only_fields = ('vacancy',)
