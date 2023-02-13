# Generated by Django 4.1.5 on 2023-02-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0020_employee_last_name_employee_patronymic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_post',
            field=models.CharField(blank=True, max_length=50, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Фамилия сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество сотрудника'),
        ),
        migrations.AlterField(
            model_name='group',
            name='full_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(blank=True, max_length=20, verbose_name='Краткое наименование'),
        ),
    ]
