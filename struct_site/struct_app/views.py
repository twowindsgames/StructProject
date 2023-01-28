from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.decorators import api_view

from .models import Group, Unit
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class GroupListView(APIView):
    def get(self, request, format=None):
        products = Group.objects.all()
        serializer = GroupSerializer(products, many=True)
        return Response(serializer.data)


class UnitsListView(APIView):
    def get(self, request, group_slug=None, format=None):
        if group_slug:
            group = Group.objects.get(slug=group_slug)
        else:
            group = request.query_params.get('group', None)

        queryset = Unit.objects.filter(group=group)
        serializer = UnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, group_slug=None):
        query = request.data
        serialize_data = UnitSerializer(data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")





















