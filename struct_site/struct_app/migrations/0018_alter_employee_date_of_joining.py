# Generated by Django 4.1.5 on 2023-02-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0017_alter_employee_group_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
    ]