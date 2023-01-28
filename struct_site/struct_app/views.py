from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Group, Unit
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class GroupListView(APIView):
    def get(self, request, format=None):
        products = Group.objects.all()
        serializer = GroupSerializer(products, many=True)
        return Response(serializer.data)





