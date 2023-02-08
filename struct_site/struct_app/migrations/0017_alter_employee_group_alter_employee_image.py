# Generated by Django 4.1.5 on 2023-02-08 18:13

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('struct_app', '0016_rename_unit_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='group',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='struct_app.group', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='employee_photos/default/default.jpg', null=True, upload_to='employee_photos/'),
        ),
    ]
