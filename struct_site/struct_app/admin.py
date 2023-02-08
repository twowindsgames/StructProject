from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Group, Employee


class GroupAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Group, GroupAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("employee_name",)}


admin.site.register(Employee, EmployeeAdmin)
