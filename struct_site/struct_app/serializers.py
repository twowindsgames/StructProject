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
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Employee
        fields = (
            "id",
            "group",
            "name",
            "post",
            "date_of_joining",
            "birthday_date",
            "image_url",
            "image",

        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)
