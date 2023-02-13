from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Group, Employee


class GroupSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, )

    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "full_title",
            "slug",
            "parent",
            "get_absolute_url",
            "is_leaf_node",
            "children",
        )
        extra_kwargs = {'children': {'required': False}}


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "full_title",
            "slug",
            "parent",
            "is_leaf_node",
            "get_absolute_url",
            "get_group_stat",
            "children",

        )
        extra_kwargs = {'children': {'required': False, }}


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "id",
            "group",
            "name",
            "last_name",
            "patronymic",
            "post",
            "date_of_joining",
            "birthday_date",
            "image",
        )


