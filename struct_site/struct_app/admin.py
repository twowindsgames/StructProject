from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Group, Unit


class GroupAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Group, GroupAdmin)


class UnitAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("employeeName",)}


admin.site.register(Unit, UnitAdmin)