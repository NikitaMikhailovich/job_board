# Generated by Django 4.1.7 on 2023-08-02 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Наименование')),
                ('city', models.CharField(max_length=127, verbose_name='Город')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_image', verbose_name='Логотип')),
                ('information', models.TextField(blank=True, default='')),
                ('enployee_amount', models.IntegerField(verbose_name='Количество сотрудников')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='specialization_image', verbose_name='Ярлык')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('skills', models.TextField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('salary_min', models.IntegerField(blank=True, null=True, verbose_name='Нижний предел запраты')),
                ('salary_max', models.IntegerField(blank=True, null=True, verbose_name='Верхний предел зарплаты')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='board.company')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vacancies', to='board.specialization')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-created_at'],
            },
        ),
    ]