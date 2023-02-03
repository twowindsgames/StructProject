from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Group, Unit


class GroupSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "slug",
            "parent",
            "get_absolute_url",
            "is_leaf_node",
            "children",
        )


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "slug",
            "parent",
            "get_absolute_url",
            "children",
        )


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = (
            "id",
            "slug",
            "group",
            "employeeName",
            "employeePost",
            "dateOfJoining",
        )
