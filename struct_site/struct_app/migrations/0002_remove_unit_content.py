# Generated by Django 4.1.5 on 2023-01-28 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='content',
        ),
    ]