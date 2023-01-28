from rest_framework import serializers

from .models import Group, Unit


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "slug",
            "parent",
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
