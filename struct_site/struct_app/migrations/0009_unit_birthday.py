# Generated by Django 4.1.5 on 2023-02-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0008_alter_unit_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
