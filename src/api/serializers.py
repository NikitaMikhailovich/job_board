from rest_framework.serializers import ModelSerializer, ReadOnlyField, RelatedField
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


class VacancyCreateSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class CompanyInVacancySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


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
        validated_data['user'] = self.context['request'].user
        return Company.objects.create(**validated_data)


class ApplicationVacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'company',
            'specialization'
        )


class ApplicationSerializer(ModelSerializer):
    vacancy = ApplicationVacancySerializer(read_only=True)
    class Meta:
        model = Application
        fields = (
            'name',
            'phone',
            'letter',
            'vacancy'
        )
