# Generated by Django 4.1.5 on 2023-02-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0005_alter_group_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]