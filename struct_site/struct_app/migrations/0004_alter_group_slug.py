# Generated by Django 4.1.5 on 2023-02-05 18:38

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0003_group_full_title_alter_group_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
