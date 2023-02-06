from django.core.files.storage import default_storage
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Group, Unit
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from slugify import slugify



class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.root_nodes()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

class GroupDetailView(APIView):
    def get(self, request, tree_hierarchy):
        groupId = request.query_params.get('groupId', None)
        if groupId is None:
            category_slug = tree_hierarchy.split('/')
            parent = None
            root = Group.objects.all()
            for slug in category_slug[:-1]:
                parent = root.get(parent=parent, slug=slug)

            group = root.get(parent=parent, slug=category_slug[-1])

        else:
            group = Group.objects.get(groupId)

        serializer = GroupDetailSerializer(group)
        return Response(serializer.data)
    def post(self, request, tree_hierarchy):

        query = JSONParser().parse(request)

        query['slug'] = slugify(query['title'])
        serialize_data = GroupDetailSerializer(data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")
    def put(self, request, tree_hierarchy):
        query = JSONParser().parse(request)
        query['slug'] = slugify(query['title'])
        groupId = query['id']
        group = Group.objects.get(id=groupId)
        serialize_data = GroupDetailSerializer(group, data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")
    def delete(self, request, tree_hierarchy):
        groupId = request.query_params.get('groupId', None)
        group = Group.objects.get(id=groupId)
        group.delete()
        if Group.objects.filter(id=groupId) is None:
            return Response("Delete Successfully")
        else:
            return Response("Delete Error")


class UnitsListView(APIView):
    def get(self, request):
        groupId = request.query_params.get('groupId', None)
        queryset = Unit.objects.filter(group=groupId)
        serializer = UnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        query = request.data
        file = request.FILES['image']
        file_name = default_storage.save(file.name, file)

        serialize_data = UnitSerializer(data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")

    def put(self, request):
        query = JSONParser().parse(request)
        unitId = query['id']
        unit = Unit.objects.get(id=unitId)
        serialize_data = UnitSerializer(unit, data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")

    def delete(self, request):
        unitId = request.query_params.get('id', None)
        unit = Unit.objects.get(id=unitId)
        unit.delete()
        if Group.objects.filter(id=unitId) is None:
            return Response("Delete Successfully")
        else:
            return Response("Delete Error")
