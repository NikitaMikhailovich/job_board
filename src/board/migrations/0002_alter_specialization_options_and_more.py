# Generated by Django 4.1.7 on 2023-11-01 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialization',
            options={'verbose_name': 'Специализация', 'verbose_name_plural': 'Специализации'},
        ),
        migrations.AlterField(
            model_name='company',
            name='information',
            field=models.TextField(blank=True, default='', verbose_name='Информация о компании'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='name',
            field=models.CharField(max_length=127, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('phone', models.CharField(max_length=31)),
                ('letter', models.TextField()),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='board.vacancy')),
            ],
        ),
    ]
