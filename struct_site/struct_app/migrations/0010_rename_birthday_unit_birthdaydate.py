# Generated by Django 4.1.5 on 2023-02-06 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0009_unit_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='birthday',
            new_name='birthdayDate',
        ),
    ]
