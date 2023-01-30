from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.decorators import api_view

from .models import Group, Unit
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.root_nodes()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class GroupDetailView(APIView):
    def get(self, request, tree_hierarchy, format=None):
        if tree_hierarchy:

            category_slug = tree_hierarchy.split('/')
            parent = None
            root = Group.objects.all()
            for slug in category_slug[:-1]:
                parent = root.get(parent=parent, slug=slug)


            group = Group.objects.filter(parent=parent, slug=category_slug[-1])

        else:
            group = Group.objects \
                .get(request.query_params.get('groupId', None))

        serializer = GroupDetailSerializer(group, many=True)
        return Response(serializer.data)


class UnitsListView(APIView):
    def get(self, request):
        group = request.query_params.get('group', None)
        queryset = Unit.objects.filter(group=group)
        serializer = UnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        query = request.data
        serialize_data = UnitSerializer(data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")
