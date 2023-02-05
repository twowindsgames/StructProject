from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Group, Unit


class GroupSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True,)

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
            "get_absolute_url",
            "children",

        )
        extra_kwargs = {'children': {'required': False, }}


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = (
            "id",
            "group",
            "employeeName",
            "employeePost",
            "dateOfJoining",
        )
