# Generated by Django 4.1.5 on 2023-02-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0018_alter_employee_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birthday_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_joining',
            field=models.DateField(blank=True),
        ),
    ]
