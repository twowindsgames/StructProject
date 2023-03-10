# Generated by Django 4.1.5 on 2023-02-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0002_remove_unit_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='full_title',
            field=models.CharField(default='null', max_length=100, verbose_name='Полное наименование'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Краткое наименование'),
        ),
    ]
