from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Specialization(models.Model):
    name = models.CharField(
        'Название',
        max_length=127,
        )
    logo = models.ImageField(
        'Ярлык',
        upload_to=settings.MEDIA_SPECIALIZATION_IMAGE_DIR,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='companies',
        )
    name = models.CharField(
        max_length=127,
        verbose_name='Наименование',
        )
    city = models.CharField(
        max_length=127,
        verbose_name='Город',
        )
    logo = models.ImageField(
        'Логотип',
        upload_to=settings.MEDIA_COMPANY_IMAGE_DIR,
        blank=True,
        null=True,
    )
    information = models.TextField(
        'Информация о компании',
        blank=True,
        default=''
        )
    enployee_amount = models.IntegerField(
        verbose_name='Количество сотрудников',
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self) -> str:
        return f'{self.name} из города {self.city}'


class Vacancy(models.Model):
    title = models.CharField(max_length=127)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    specialization = models.ForeignKey(
        Specialization,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='vacancies',
    )
    skills = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    salary_min = models.IntegerField(
        verbose_name='Нижний предел запраты', blank=True, null=True,
        )
    salary_max = models.IntegerField(
        verbose_name='Верхний предел зарплаты', blank=True, null=True,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """class Meta."""

        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created_at']

    def __str__(self):  # noqa: D105
        return f'{self.title} для компании {self.company}'
    

class Application(models.Model):
    name = models.CharField(
        max_length=127,
        verbose_name= 'Имя',
    )
    phone = models.CharField(
        max_length=31,
        verbose_name='Номер телефона',
    )
    letter = models.TextField(
        verbose_name='Сопроводительное письмо',
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='applications',
    )
