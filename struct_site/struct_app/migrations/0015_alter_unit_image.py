# Generated by Django 4.1.5 on 2023-02-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0014_alter_unit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='image',
            field=models.ImageField(blank=True, default='unit_photos/default/default.jpg', null=True, upload_to='unit_photos/'),
        ),
    ]
