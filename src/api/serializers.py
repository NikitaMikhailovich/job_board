from rest_framework.serializers import ModelSerializer
from board.models import Vacancy, Company


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'salary_min',
            'salary_max',
            'created_at',
        )


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


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
